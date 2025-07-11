from bs4 import BeautifulSoup
import os
from pathlib import Path
from IPython.display import display, HTML
from bs4.element import Tag
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_loaders import BSHTMLLoader
from langchain_community.document_loaders import UnstructuredHTMLLoader
from langchain_community.document_transformers import MarkdownifyTransformer
from urllib.parse import urlparse
from langchain.schema import Document
import re


# Define patterns to exclude
EXCLUDE_PATTERNS = [
    r'\.ttl\.html$',  # Exclude files ending with .ttl.html
    r'\.xml\.html$',  # Exclude files ending with .xml.html
    r'\.json\.html$'  # Also exclude .json.html files
]


def convert_local_html_to_markdown(input_dir, output_dir="markdown_output", exclude_patterns=EXCLUDE_PATTERNS):
    """
    Convert HTML files from a local directory to markdown, excluding files matching specific patterns.
    
    Args:
        input_dir (str): Path to the directory containing HTML files
        output_dir (str): Path to save the markdown files
        exclude_patterns (list): List of regex patterns to exclude
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Compile regex patterns for exclusion if provided
    if exclude_patterns:
        compiled_patterns = [re.compile(pattern) for pattern in exclude_patterns]
    else:
        compiled_patterns = [re.compile(r'\.ttl\.html$'), re.compile(r'\.xml\.html$')]
    
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
    
    print(f"Found {len(html_files)} HTML files to process")
    
    # Process each HTML file
    processed = 0
    errors = 0
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
            
            soup = BeautifulSoup(html_content)
            styletag = soup.find("style", attrs={'type':'text/css'}).text
            h_prefix_match = re.match(r'(h[0-9]){--heading-prefix:\"([0-9]+\S[0-9]+)\"', styletag)

            prev_level = int(h_prefix_match.group(1)[1:]) - 1 
            header_list = [int(x) for x in h_prefix_match.group(2).split('.')]
            for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
                header_level = int(header.name[1:])
                if header_level > prev_level:
                    header_list.extend([0]*(header_level-len(header_list)+1))
                elif header_level < prev_level:
                    header_list = header_list[:header_level]
                header_list[-1] += 1
                header.replace_with(".".join([str(x) for x in header_list]) + " " + header.text)
            # Create a LangChain Document object with the HTML content

            doc = Document(page_content=str(soup))
            
            # Transform to Markdown
            converted_docs = md_transformer.transform_documents([doc])
            
            # Write to output file
            if converted_docs and len(converted_docs) > 0:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(converted_docs[0].page_content)
                processed += 1
            
            # Print progress
            if (i + 1) % 10 == 0 or i == len(html_files) - 1:
                print(f"Processed {i + 1}/{len(html_files)} files")
                
        except Exception as e:
            print(f"Error processing {html_file}: {str(e)}")
            errors += 1
    
    print(f"Conversion complete. Successfully processed {processed} files. Encountered {errors} errors.")