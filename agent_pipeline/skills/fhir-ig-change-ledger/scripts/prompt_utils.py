"""
Utility functions for loading and managing prompts from external markdown files.
"""
import os
import logging
from pathlib import Path
import path_helpers
from typing import Dict, Any, Optional

def load_prompt(artifacts_dir: str, filename: str, **kwargs) -> str:
    """
    Load a prompt from a markdown file and format it with the provided kwargs.
    
    Args:
        prompt_path: Path to the prompt markdown file
        **kwargs: Variables to substitute in the prompt template
        
    Returns:
        str: Formatted prompt
    """
    prompt_path = Path(artifacts_dir) / 'prompts' / filename
    if not prompt_path.is_file():
        prompt_path = Path(path_helpers.PROJECT_ROOT) / 'default_prompts' / filename

    logging.info(f"Using prompt at: {prompt_path}")
    try:
        with open(prompt_path, 'r') as f:
            prompt_template = f.read()
            
        # Format the prompt with provided variables
        formatted_prompt = prompt_template.format(**kwargs)
        return formatted_prompt
    except FileNotFoundError:
        logging.error(f"Prompt file not found: {prompt_path}")
        raise
    except KeyError as e:
        logging.error(f"Missing parameter in prompt template: {e}")
        raise
    except Exception as e:
        logging.error(f"Error loading prompt from {prompt_path}: {str(e)}")
        raise
