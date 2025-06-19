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

def get_filename_from_url(url):
    """Extract filename from URL and convert to markdown filename."""
    # Parse the URL and get the path
    path = urlparse(url).path
    
    # Get the last part of the path (filename)
    filename = path.split('/')[-1]
    
    # Remove .html extension if present
    filename = filename.replace('.html', '')
    
    # Convert to title case and replace special characters
    filename = filename.replace('-', '_')
    
    # Add .md extension
    return f"{filename}.md"

def convert_urls_to_markdown(urls, output_dir="PlanNet/site/markdown"):
    """Convert multiple URLs to markdown files."""
    # Initialize loaders and transformers
    loader = AsyncHtmlLoader(urls, verify_ssl=False)
    md_transformer = MarkdownifyTransformer()
    
    # Load all documents
    docs = loader.load()
    converted_docs = md_transformer.transform_documents(docs)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Process each document
    for url, doc in zip(urls, converted_docs):
        # Generate filename from URL
        filename = get_filename_from_url(url)
        
        # Create full file path
        file_path = os.path.join(output_dir, filename)
        
        # Write content to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(doc.page_content)
        
        print(f"Created: {filename}")