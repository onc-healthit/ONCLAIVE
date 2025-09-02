"""
Markdown Cleaner Module

This module provides functionality to clean markdown files by removing header/footer content,
navigation elements, and fixing formatting issues from HTML-to-markdown conversions.
"""

import os
import re
from pathlib import Path
from typing import Optional


def clean_markdown_file(file_path: str) -> Optional[str]:
    """
    Clean a markdown file by removing header and footer content and fixing formatting issues.
    
    This function removes:
    - XML declarations and encoding lines
    - Table of Contents navigation
    - Footer content (IG copyright, links)
    - Excessive whitespace and escaped characters
    
    Args:
        file_path: Path to the markdown file to clean
        
    Returns:
        Cleaned markdown content as string, or None if processing fails
        
    Example:
        >>> content = clean_markdown_file('input.md')
        >>> if content:
        ...     print("File cleaned successfully")
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Remove the XML declaration and encoding line
        content = re.sub(r'xml version\=\"1\.0\" encoding\=\"UTF\-8\"\?', '', content)
        
        # Find where the main content starts (after the Table of Contents marker)
        toc_pattern = r'\* \[\*\*Table of Contents\*\*\]\(toc\.html\)\s*\n\* \*\*([^*]+)\*\*'
        match = re.search(toc_pattern, content)
        
        if match:
            # Get the title of the document (to preserve it)
            title = match.group(1).strip()
            
            # Find the position after the TOC line
            toc_end_pos = match.end()
            content_after_toc = content[toc_end_pos:]
            
            # Find the beginning of the main content (after empty lines following TOC)
            main_content_start = re.search(r'\n\s*\n', content_after_toc)
            if main_content_start:
                main_content_start_pos = main_content_start.end() + toc_end_pos
                main_content = content[main_content_start_pos:]
            else:
                main_content = content_after_toc
                
            # Remove footer content with a more specific pattern
            main_content = _remove_footer_content(main_content)
            
            # Add the title as a proper markdown heading
            cleaned_content = f"# {title}\n\n{main_content.strip()}"
            
        else:
            # If TOC pattern not found, try to find content after header in a different way
            main_content = _extract_content_fallback(content)
            
            # Try to find a title
            title_match = re.search(r'## ([^\n]+)', main_content)
            title = title_match.group(1) if title_match else "Document"
            
            cleaned_content = f"# {title}\n\n{main_content.strip()}"
        
        # Apply final cleanup
        cleaned_content = _apply_final_cleanup(cleaned_content)
        return cleaned_content
    
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return None


def _remove_footer_content(content: str) -> str:
    """
    Remove footer content from markdown text.
    
    Args:
        content: Markdown content to clean
        
    Returns:
        Content with footer removed
    """
    footer_start = re.search(r'(\n\s*IG Â©|\n IG Â©|\n\s*Links:)', content)
    if footer_start:
        return content[:footer_start.start()]
    return content


def _extract_content_fallback(content: str) -> str:
    """
    Extract main content when TOC pattern is not found.
    
    Args:
        content: Raw markdown content
        
    Returns:
        Extracted main content
    """
    # Find the end of the last navigation list item
    nav_end = re.search(r'\* \[[^\]]+\]\([^)]+\)\s*\n\s*\n', content)
    if nav_end:
        main_content = content[nav_end.end():]
        return _remove_footer_content(main_content)
    else:
        # If all else fails, just return the content with footer removed
        return _remove_footer_content(content)


def _apply_final_cleanup(content: str) -> str:
    """
    Apply final formatting cleanup to markdown content.
    
    Args:
        content: Content to clean up
        
    Returns:
        Content with formatting issues fixed
    """
    # Clean up excessive whitespace and escape characters
    content = re.sub(r'\\\-', '-', content)  # Fix escaped hyphens
    content = re.sub(r'\\\+', '+', content)  # Fix escaped plus signs
    content = re.sub(r'\\\|', '|', content)  # Fix escaped pipes
    content = re.sub(r'\\\.', '.', content)  # Fix escaped periods
    content = re.sub(r'\s+\n', '\n', content)  # Remove trailing whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)  # Normalize multiple newlines
    
    return content


def process_directory(input_dir: str, output_dir: str) -> dict:
    """
    Process all markdown files in a directory and save cleaned versions.
    
    This function finds all .md files in the input directory, cleans them using
    clean_markdown_file(), and saves the results to the output directory.
    
    Args:
        input_dir: Directory containing markdown files to process
        output_dir: Directory to save cleaned files
        
    Returns:
        Dictionary containing processing summary:
            - total_files: Total markdown files found
            - successful: Number of files successfully processed
            - failed: Number of files that failed processing
            - failed_files: List of files that failed processing
            
    Raises:
        FileNotFoundError: If input directory doesn't exist
        PermissionError: If unable to create output directory or write files
        
    Example:
        >>> result = process_directory('input_md', 'cleaned_md')
        >>> print(f"Processed {result['successful']}/{result['total_files']} files")
    """
    # Validate input directory
    input_path = Path(input_dir)
    if not input_path.exists():
        raise FileNotFoundError(f"Input directory not found: {input_dir}")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all markdown files in the input directory
    md_files = list(input_path.glob('*.md'))
    
    print(f"Found {len(md_files)} markdown files in {input_dir}")
    
    successful = 0
    failed = 0
    failed_files = []
    
    for file_path in md_files:
        output_path = Path(output_dir) / file_path.name
        cleaned_content = clean_markdown_file(str(file_path))
        
        if cleaned_content:
            try:
                with open(output_path, 'w', encoding='utf-8') as out_file:
                    out_file.write(cleaned_content)
                successful += 1
                print(f"Cleaned and saved: {output_path}")
            except Exception as e:
                print(f"Error writing {output_path}: {str(e)}")
                failed += 1
                failed_files.append(str(file_path))
        else:
            failed += 1
            failed_files.append(str(file_path))
    
    print(f"\nProcessing complete: {successful} files successfully cleaned, {failed} failed")
    
    return {
        'total_files': len(md_files),
        'successful': successful,
        'failed': failed,
        'failed_files': failed_files
    }