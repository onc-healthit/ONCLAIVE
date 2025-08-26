
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


def convert_local_html_to_markdown(input_dir, output_dir="markdown_output", exclude_patterns=None, verbose=True):
    """
    Convert HTML files from a local directory to markdown, excluding files matching specific patterns.
    
    Args:
        input_dir (str): Path to the directory containing HTML files
        output_dir (str): Path to save the markdown files
        exclude_patterns (list, optional): List of regex patterns to exclude. 
                                         If None, uses DEFAULT_EXCLUDE_PATTERNS
        verbose (bool): Whether to print progress messages
    
    Returns:
        dict: Summary of the conversion process with keys:
            - 'total_files': Total HTML files found
            - 'processed': Number of files successfully processed
            - 'errors': Number of files that encountered errors
            - 'error_files': List of files that had errors
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Use default patterns if none provided
    if exclude_patterns is None:
        exclude_patterns = DEFAULT_EXCLUDE_PATTERNS
    
    # Compile regex patterns for exclusion
    compiled_patterns = [re.compile(pattern) for pattern in exclude_patterns]
    
    # Get all HTML files in the directory
    html_files = []
    for file in Path(input_dir).glob('**/*.html'):
        file_str = str(file)
        
        # Check if the file should be excluded
        exclude = False
        for pattern in compiled_patterns:
            if pattern.search(file_str):
                exclude = True
                break
        
        if not exclude:
            html_files.append(file)
    
    if verbose:
        print(f"Found {len(html_files)} HTML files to process")
    
    # Process each HTML file
    processed = 0
    errors = 0
    error_files = []
    md_transformer = MarkdownifyTransformer()
    
    for i, html_file in enumerate(html_files):
        try:
            # Create relative path to preserve directory structure
            rel_path = html_file.relative_to(input_dir)
            output_path = Path(output_dir) / rel_path.with_suffix('.md')
            
            # Create parent directories if they don't exist
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Load HTML content
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
    
    # Return summary
    return {
        'total_files': len(html_files),
        'processed': processed,
        'errors': errors,
        'error_files': error_files
    }


def _process_html_headers(html_content, html_file, verbose=True):
    """
    Process HTML headers to add hierarchical numbering based on CSS styles.
    
    Args:
        html_content (str): The HTML content to process
        html_file (Path): Path to the HTML file (for error reporting)
        verbose (bool): Whether to print warning messages
    
    Returns:
        str: Processed HTML content with numbered headers
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find the style tag with CSS heading prefix information
        style_tag = soup.find("style", attrs={'type': 'text/css'})
        
        if style_tag and style_tag.text:
            # Look for heading prefix pattern in CSS
            h_prefix_match = re.search(
                r'(h[0-9])\s*\{\s*--heading-prefix\s*:\s*"([0-9]+(?:\.[0-9]+)*)"', 
                style_tag.text
            )
            
            if h_prefix_match:
                # Extract the starting header level and numbering
                starting_header_level = int(h_prefix_match.group(1)[1:])
                prev_level = starting_header_level - 1
                header_list = [int(x) for x in h_prefix_match.group(2).split('.')]
                
                # Process all headers in the document
                for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
                    header_level = int(header.name[1:])
                    
                    # Adjust header numbering based on level
                    if header_level > prev_level:
                        # Going deeper - extend the list with zeros if needed
                        while len(header_list) < header_level:
                            header_list.append(0)
                    elif header_level < prev_level:
                        # Going shallower - trim the list
                        header_list = header_list[:header_level]
                    
                    # Increment the counter at current level
                    if len(header_list) >= header_level:
                        header_list[header_level - 1] += 1
                    else:
                        header_list.append(1)
                    
                    # Create the numbered header text
                    header_number = ".".join([str(x) for x in header_list[:header_level]])
                    markdown_header = " ".join([
                        "#" * header_level, 
                        header_number, 
                        header.get_text(strip=True)
                    ])
                    
                    # Replace the original header with numbered version
                    header.replace_with(markdown_header)
                    prev_level = header_level
        
        # Return the processed soup content
        return str(soup)
        
    except Exception as header_error:
        if verbose:
            print(f"Warning: Header processing failed for {html_file}: {str(header_error)}")
            print("Falling back to original HTML content...")
        return html_content


def get_html_file_count(input_dir, exclude_patterns=None):
    """
    Count HTML files that would be processed (excluding those matching patterns).
    
    Args:
        input_dir (str): Path to the directory containing HTML files
        exclude_patterns (list, optional): List of regex patterns to exclude
    
    Returns:
        int: Number of HTML files that would be processed
    """
    if exclude_patterns is None:
        exclude_patterns = DEFAULT_EXCLUDE_PATTERNS
    
    compiled_patterns = [re.compile(pattern) for pattern in exclude_patterns]
    
    count = 0
    for file in Path(input_dir).glob('**/*.html'):
        file_str = str(file)
        exclude = any(pattern.search(file_str) for pattern in compiled_patterns)
        if not exclude:
            count += 1
    
    return count