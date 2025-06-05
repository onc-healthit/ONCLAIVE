import os
import re
import argparse
from pathlib import Path

def clean_markdown_file(file_path):
    """
    Clean a markdown file by removing the header and footer content.
    
    Args:
        file_path (str): Path to the markdown file
        
    Returns:
        str: Cleaned markdown content
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
            # Explicitly search for the footer markers
            footer_start = re.search(r'(\n\s*IG ©|\n IG ©|\n\s*Links:)', main_content)
            if footer_start:
                main_content = main_content[:footer_start.start()]
            
            # Add the title as a proper markdown heading
            cleaned_content = f"# {title}\n\n{main_content.strip()}"
            
            # Clean up excessive whitespace and escape characters
            cleaned_content = re.sub(r'\\\-', '-', cleaned_content)  # Fix escaped hyphens
            cleaned_content = re.sub(r'\\\+', '+', cleaned_content)  # Fix escaped plus signs
            cleaned_content = re.sub(r'\\\|', '|', cleaned_content)  # Fix escaped pipes
            cleaned_content = re.sub(r'\\\.', '.', cleaned_content)  # Fix escaped periods
            cleaned_content = re.sub(r'\s+\n', '\n', cleaned_content)  # Remove trailing whitespace
            cleaned_content = re.sub(r'\n{3,}', '\n\n', cleaned_content)  # Normalize multiple newlines
            
            return cleaned_content
        else:
            # If TOC pattern not found, try to find content after header in a different way
            # Find the end of the last navigation list item
            nav_end = re.search(r'\* \[[^\]]+\]\([^)]+\)\s*\n\s*\n', content)
            if nav_end:
                main_content = content[nav_end.end():]
                
                # Remove footer content
                footer_start = re.search(r'(\n\s*IG ©|\n IG ©|\n\s*Links:)', main_content)
                if footer_start:
                    main_content = main_content[:footer_start.start()]
                
                # Try to find a title
                title_match = re.search(r'## ([^\n]+)', main_content)
                title = title_match.group(1) if title_match else "Document"
                
                return f"# {title}\n\n{main_content.strip()}"
            else:
                # If all else fails, just return the content with footer removed
                footer_start = re.search(r'(\n\s*IG ©|\n IG ©|\n\s*Links:)', content)
                if footer_start:
                    content = content[:footer_start.start()]
                return content.strip()
    
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return None
    
def process_directory(input_dir, output_dir):
    """
    Process all markdown files in a directory and save cleaned versions.
    
    Args:
        input_dir (str): Directory containing markdown files
        output_dir (str): Directory to save cleaned files
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all markdown files in the input directory
    input_path = Path(input_dir)
    md_files = list(input_path.glob('*.md'))
    
    print(f"Found {len(md_files)} markdown files in {input_dir}")
    
    successful = 0
    failed = 0
    
    for file_path in md_files:
        output_path = Path(output_dir) / file_path.name
        cleaned_content = clean_markdown_file(file_path)
        
        if cleaned_content:
            with open(output_path, 'w', encoding='utf-8') as out_file:
                out_file.write(cleaned_content)
            successful += 1
            print(f"Cleaned and saved: {output_path}")
        else:
            failed += 1
    
    print(f"\nProcessing complete: {successful} files successfully cleaned, {failed} failed")
