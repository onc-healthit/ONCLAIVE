# 1. IMPORTS AND BASIC SETUP
import base64
import json
import logging
from typing import List, Dict, Tuple, Union, Optional, Any
from dataclasses import dataclass
import os
import time
import threading
from IPython.display import Image
import math
import io
import re
import pandas as pd
from json_repair import repair_json
from langchain_community.document_loaders import BSHTMLLoader
import shutil
from dotenv import load_dotenv
import httpx
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type
from anthropic import RateLimitError
from anthropic import Anthropic
import google.generativeai as gemini
from openai import OpenAI
import httpx


# Basic setup
logging.basicConfig(level=logging.INFO)
load_dotenv()

# Constants
CERT_PATH = '/Users/jrockhill/miniconda3/envs/ONCL310/lib/python3.10/site-packages/pip/_vendor/certifi/cacert.pem'

API_CONFIGS = {
    "claude": {
        "model_name": "claude-3-5-sonnet-20241022",
        "max_tokens": 8192,
        "temperature": 0.7,
        "batch_size": 5,
        "delay_between_chunks": 1,
        "delay_between_batches": 3,
        "requests_per_minute": 900,
        "max_requests_per_day": 20000,
        "delay_between_requests": 0.1
    },
    "gemini": {
        "model": "models/gemini-1.5-pro-001",
        "max_tokens": 8192,
        "temperature": 0.7,
        "batch_size": 5,  # More conservative batch size
        "delay_between_chunks": 2,
        "delay_between_batches": 5,
        "requests_per_minute": 900,
        "max_requests_per_day": 50000,
        "delay_between_requests": 0.1,
        "timeout": 60  # Longer timeout for larger content
    },
    "gpt": {
        "model": "gpt-4o",
        "max_tokens": 8192,
        "temperature": 0.7,
        "batch_size": 5,
        "delay_between_chunks": 2,
        "delay_between_batches": 5,
        "requests_per_minute": 450,
        "max_requests_per_day": 20000,
        "delay_between_requests": 0.15
    }
}

SYSTEM_PROMPTS = {
    "claude": """You are a seasoned Healthcare Integration Test Engineer 
                analyzing a FHIR Implementation Guide to extract precise testable requirements."""
}

def create_rate_limiter():
    """Create a rate limiter state dictionary for all APIs"""
    return {
        api: {
            'requests': [],
            'daily_requests': 0,
            'last_reset': time.time()
        }
        for api in API_CONFIGS.keys()
    }

def check_rate_limits(rate_limiter: dict, api: str):
    """Check and wait if rate limits would be exceeded"""
    if api not in rate_limiter:
        raise ValueError(f"Unknown API: {api}")
        
    now = time.time()
    state = rate_limiter[api]
    config = API_CONFIGS[api]
    
    # Reset daily counts if needed
    day_seconds = 24 * 60 * 60
    if now - state['last_reset'] >= day_seconds:
        state['daily_requests'] = 0
        state['last_reset'] = now
    
    # Check daily limit
    if state['daily_requests'] >= config['max_requests_per_day']:
        raise Exception(f"{api} daily request limit exceeded")
    
    # Remove old requests outside the current minute
    state['requests'] = [
        req_time for req_time in state['requests']
        if now - req_time < 60
    ]
    
    # Wait if at rate limit
    if len(state['requests']) >= config['requests_per_minute']:
        sleep_time = 60 - (now - state['requests'][0])
        if sleep_time > 0:
            time.sleep(sleep_time)
        state['requests'] = state['requests'][1:]
    
    # Add minimum delay between requests
    if state['requests'] and now - state['requests'][-1] < config['delay_between_requests']:
        time.sleep(config['delay_between_requests'])
    
    # Record this request
    state['requests'].append(now)
    state['daily_requests'] += 1

def format_content_for_api(content: Union[str, dict, list], api_type: str) -> str:
    """Format content appropriately for each API"""
    
    # Create the base requirements extraction prompt
    #base_prompt = create_prompt(content)
    
    if api_type == "claude":
        return [{
            "type": "text",
            "text": content
        }]
    
    # For other APIs, return just the text
    return content

@retry(
    wait=wait_exponential(multiplier=1, min=4, max=60),
    stop=stop_after_attempt(5),
    retry=retry_if_exception_type((RateLimitError, TimeoutError))
)
def make_api_request(client, api_type: str, content: Union[str, dict, list], rate_limit_func) -> str:
    """Make rate-limited API request with retries"""
    rate_limit_func()
    
    config = API_CONFIGS[api_type]
    formatted_content = format_content_for_api(content, api_type)
    
    try:
        if api_type == "claude":
            response = client.messages.create(
                model=config["model_name"],
                max_tokens=config["max_tokens"],
                messages=[{
                    "role": "user", 
                    "content": formatted_content
                }],
                system=SYSTEM_PROMPTS[api_type]
            )
            return response.content[0].text
            
    except Exception as e:
        logging.error(f"Error in {api_type} API request: {str(e)}")
        raise

def setup_clients():
    """Initialize clients for LLM service"""
    try:
        # Claude setup
        verify_path = CERT_PATH if os.path.exists(CERT_PATH) else True
        http_client = httpx.Client(verify=verify_path, timeout=60.0)
        claude_client = Anthropic(
            api_key=os.getenv('ANTHROPIC_API_KEY'),
            http_client=http_client
        )
        
        return {
            "claude": claude_client,
        }
        
    except Exception as e:
        logging.error(f"Error setting up clients: {str(e)}")
        raise

def process_all_content(reqs: list[str], api_type: str='claude') -> Tuple[Dict[str, Any], list]:
    """Process all content and generate requirements in Inferno format"""
    clients = setup_clients()
    client = clients[api_type]
    config = API_CONFIGS[api_type]
    rate_limiter = create_rate_limiter()
    
    responses = []
    def check_limits():
        check_rate_limits(rate_limiter, api_type)
    for req in reqs:
        try:
            response = make_api_request(client, api_type, req, check_limits)
            responses.append(response)
            
        except Exception as e:
            logging.error(f"Error processing content: {str(e)}")

    return responses