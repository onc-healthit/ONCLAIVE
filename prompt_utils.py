"""
Utility functions for loading and managing prompts from external markdown files.
"""
import os
import logging
from pathlib import Path
from typing import Dict, Any, Optional

def load_prompt(prompt_path: str, **kwargs) -> str:
    """
    Load a prompt from a markdown file and format it with the provided kwargs.
    
    Args:
        prompt_path: Path to the prompt markdown file
        **kwargs: Variables to substitute in the prompt template
        
    Returns:
        str: Formatted prompt
    """
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

def setup_prompt_environment(project_root: Path) -> Dict[str, Any]:
    """
    Setup the prompt environment by creating directories and returning paths.
    
    Args:
        project_root: Path to the project root directory
        
    Returns:
        dict: Dictionary containing prompt-related paths
    """
    # Define prompt directory
    prompt_dir = os.path.join(project_root, 'prompts')
    
    # Create prompt directory if it doesn't exist
    os.makedirs(prompt_dir, exist_ok=True)
    
    # Define paths for common prompts
    paths = {
        "prompt_dir": prompt_dir,
        "requirements_extraction_path": os.path.join(prompt_dir, 'reqs_extraction_claude.md'),
        "requirements_refinement_path": os.path.join(prompt_dir, 'requirements_refinement.md'),
        "requirements_grouping_path": os.path.join(prompt_dir, 'requirements_grouping.md'),
        "test_plan_gen_path": os.path.join(prompt_dir, 'test_plan.md'),
        "test_gen_path": os.path.join(prompt_dir, 'test_gen.md'),
        "requirement_grouping_path": os.path.join(prompt_dir, 'requirement_grouping.md')
    }
    
    logging.info(f"Prompt environment set up at: {prompt_dir}")
    return paths

def list_available_prompts(prompt_dir: str) -> Dict[str, str]:
    """
    List all available prompts in the prompt directory
    
    Args:
        prompt_dir: Path to the prompts directory
        
    Returns:
        Dictionary with prompt names as keys and file paths as values
    """
    if not os.path.exists(prompt_dir):
        logging.warning(f"Prompt directory does not exist: {prompt_dir}")
        return {}
    
    prompts = {}
    for file in os.listdir(prompt_dir):
        if file.endswith('.md'):
            prompt_name = os.path.splitext(file)[0]
            prompts[prompt_name] = os.path.join(prompt_dir, file)
    
    return prompts