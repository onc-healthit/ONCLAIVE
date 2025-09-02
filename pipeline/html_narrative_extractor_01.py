"""
HTML to Markdown Converter Module

This module provides functionality to convert HTML files to Markdown format,
with special handling for hierarchical header numbering from CSS styles.
"""

from bs4 import BeautifulSoup
import os
from pathlib import Path
from langchain_community.document_transformers import MarkdownifyTransformer
from langchain.schema import Document
import re


# Default patterns to exclude from conversion
DEFAULT_EXCLUDE_PATTERNS = [
    r'\.ttl\.html$',      # Exclude files ending with .ttl.html
    r'\.xml\.html$',      # Exclude files ending with .xml.html
    r'\.json\.html$',     # Exclude files ending with .json.html
    r'\.change\.history\.html$',    # Exclude change history files
    r'\.profile\.history\.html$',
    r'(?i)example'
]


def convert_local_html_to_markdown(
    input_dir: str, 
    output_dir: str = "markdown_output", 
    exclude_patterns: list = None, 
    verbose: bool = True
) -> dict:
    """
    Convert HTML files from a local directory to markdown, excluding files matching specific patterns.
    
    This function recursively processes all HTML files in the input directory,
    applies header numbering based on CSS styles, and converts them to Markdown format
    while preserving the directory structure.
    
    Args:
        input_dir: Path to the directory containing HTML files
        output_dir: Path to save the markdown files (default: "markdown_output")
        exclude_patterns: List of regex patterns to exclude. If None, uses DEFAULT_EXCLUDE_PATTERNS
        verbose: Whether to print progress messages
    
    Returns:
        Dictionary containing conversion summary:
            - total_files: Total HTML files found
            - processed: Number of files successfully processed
            - errors: Number of files that encountered errors
            - error_files: List of files that had errors
            
    Raises:
        FileNotFoundError: If input directory doesn't exist
        PermissionError: If unable to create output directory or write files
        
    Example:
        >>> result = convert_local_html_to_markdown('input/html', 'output/md')
        >>> print(f"Processed {result['processed']} files")
    """
    # Validate input directory
    input_path = Path(input_dir)
    if not input_path.exists():
        raise FileNotFoundError(f"Input directory not found: {input_dir}")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Use default patterns if none provided
    if exclude_patterns is None:
        exclude_patterns = DEFAULT_EXCLUDE_PATTERNS
    
    # Compile regex patterns for exclusion
    compiled_patterns = [re.compile(pattern) for pattern in exclude_patterns]
    
    # Get all HTML files in the directory
    html_files = []
    for file in input_path.glob('**/*.html'):
        file_str = str(file)
        
        # Check if the file should be excluded
        exclude = any(pattern.search(file_str) for pattern in compiled_patterns)
        if not exclude:
            html_files.append(file)
    
    if verbose:
        print(f"Found {len(html_files)} HTML files to process")
    
    # Initialize counters and transformer
    processed = 0
    errors = 0
    error_files = []
    md_transformer = MarkdownifyTransformer()
    
    # Process each HTML file
    for i, html_file in enumerate(html_files):
        try:
            # Create relative path to preserve directory structure
            rel_path = html_file.relative_to(input_path)
            output_path = Path(output_dir) / rel_path.with_suffix('.md')
            
            # Create parent directories if they don't exist
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Load and process HTML content
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # Process headers with numbering
            processed_content = _process_html_headers(html_content, html_file, verbose)
            
            # Create a LangChain Document object with the processed HTML content
            doc = Document(page_content=processed_content)
            
            # Transform to Markdown
            converted_docs = md_transformer.transform_documents([doc])
            
            # Write to output file
            if converted_docs and len(converted_docs) > 0:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(converted_docs[0].page_content)
                processed += 1
            else:
                raise ValueError("No content generated from markdown transformer")
            
            # Print progress
            if verbose and ((i + 1) % 10 == 0 or i == len(html_files) - 1):
                print(f"Processed {i + 1}/{len(html_files)} files")
                
        except Exception as e:
            if verbose:
                print(f"Error processing {html_file}: {str(e)}")
            errors += 1
            error_files.append(str(html_file))
    
    # Print summary
    if verbose:
        print(f"Conversion complete. Successfully processed {processed} files. Encountered {errors} errors.")
    
    return {
        'total_files': len(html_files),
        'processed': processed,
        'errors': errors,
        'error_files': error_files
    }


def _process_html_headers(html_content: str, html_file: Path, verbose: bool = True) -> str:
    """
    Process HTML headers to add hierarchical numbering based on CSS styles.
    
    This function extracts header numbering patterns from CSS --heading-prefix variables
    and applies hierarchical numbering to all h1-h6 elements in the document.
    
    Args:
        html_content: The HTML content to process
        html_file: Path to the HTML file (used for error reporting)
        verbose: Whether to print warning messages for processing failures
    
    Returns:
        Processed HTML content with numbered headers, or original content if processing fails
        
    Note:
        The function looks for CSS variables in the format:
        h{level} { --heading-prefix: "1.2.3"; }
        and uses this to establish the starting numbering hierarchy.
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find the style tag with CSS heading prefix information
        style_tag = soup.find("style", attrs={'type': 'text/css'})
        
        if not (style_tag and style_tag.text):
            return html_content
            
        # Look for heading prefix pattern in CSS
        h_prefix_match = re.search(
            r'(h[0-9])\s*\{\s*--heading-prefix\s*:\s*"([0-9]+(?:\.[0-9]+)*)"', 
            style_tag.text
        )
        
        if not h_prefix_match:
            return html_content
            
        # Extract the starting header level and numbering
        starting_header_level = int(h_prefix_match.group(1)[1:])
        prev_level = starting_header_level - 1
        header_list = [int(x) for x in h_prefix_match.group(2).split('.')]
        
        # Process all headers in the document
        for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            header_level = int(header.name[1:])
            
            # Adjust header numbering based on level changes
            header_list = _update_header_numbering(header_list, header_level, prev_level)
            
            # Create the numbered header text
            header_number = ".".join(str(x) for x in header_list[:header_level])
            markdown_header = " ".join([
                "#" * header_level, 
                header_number, 
                header.get_text(strip=True)
            ])
            
            # Replace the original header with numbered version
            header.replace_with(markdown_header)
            prev_level = header_level
        
        return str(soup)
        
    except Exception as header_error:
        if verbose:
            print(f"Warning: Header processing failed for {html_file}: {str(header_error)}")
            print("Falling back to original HTML content...")
        return html_content


def _update_header_numbering(header_list: list, current_level: int, prev_level: int) -> list:
    """
    Update the header numbering list based on the current and previous header levels.
    
    Args:
        header_list: Current list of header numbers at each level
        current_level: The level of the current header (1-6)
        prev_level: The level of the previous header
        
    Returns:
        Updated header numbering list
    """
    if current_level > prev_level:
        # Going deeper - extend the list with zeros if needed
        while len(header_list) < current_level:
            header_list.append(0)
    elif current_level < prev_level:
        # Going shallower - trim the list
        header_list = header_list[:current_level]
    
    # Increment the counter at current level
    if len(header_list) >= current_level:
        header_list[current_level - 1] += 1
    else:
        header_list.append(1)
    
    return header_list


def get_html_file_count(input_dir: str, exclude_patterns: list = None) -> int:
    """
    Count HTML files that would be processed (excluding those matching patterns).
    
    This function provides a way to preview how many files would be processed
    without actually performing the conversion.
    
    Args:
        input_dir: Path to the directory containing HTML files
        exclude_patterns: List of regex patterns to exclude. If None, uses DEFAULT_EXCLUDE_PATTERNS
    
    Returns:
        Number of HTML files that would be processed
        
    Raises:
        FileNotFoundError: If input directory doesn't exist
        
    Example:
        >>> count = get_html_file_count('input/html')
        >>> print(f"Will process {count} HTML files")
    """
    input_path = Path(input_dir)
    if not input_path.exists():
        raise FileNotFoundError(f"Input directory not found: {input_dir}")
    
    if exclude_patterns is None:
        exclude_patterns = DEFAULT_EXCLUDE_PATTERNS
    
    compiled_patterns = [re.compile(pattern) for pattern in exclude_patterns]
    
    count = 0
    for file in input_path.glob('**/*.html'):
        file_str = str(file)
        exclude = any(pattern.search(file_str) for pattern in compiled_patterns)
        if not exclude:
            count += 1
    
    return count