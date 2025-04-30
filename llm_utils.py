"""
LLM Utilities Module for API interactions with Claude, Gemini, and GPT models.
"""
# Imports
import os
import time
import logging
import httpx
from typing import Dict, Any, Callable

try:
    from anthropic import Anthropic, RateLimitError
    import google.generativeai as gemini
    from openai import OpenAI
    from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type
except ImportError:
    raise ImportError("Please install required packages: pip install anthropic google-generativeai openai tenacity")


# API Configuration
API_CONFIGS = {
    "claude": {
        "model_name": "claude-3-5-sonnet-20241022", 
        "max_tokens": 8192,
        "temperature": 0.3,
        "batch_size": 5,
        "delay_between_chunks": 1,
        "delay_between_batches": 3,
        "requests_per_minute": 900,
        "max_requests_per_day": 20000,
        "delay_between_requests": 0.1
    },
    "gemini": {
        "model": "models/gemini-2.5-pro-preview-03-25",
        "max_tokens": 8192,
        "temperature": 0.3,
        "batch_size": 5,
        "delay_between_chunks": 2,
        "delay_between_batches": 5,
        "requests_per_minute": 900,
        "max_requests_per_day": 50000,
        "delay_between_requests": 0.1,
        "timeout": 60
    },
    "gpt": {
        "model": "gpt-4o",
        "max_tokens": 8192,
        "temperature": 0.3,
        "batch_size": 5,
        "delay_between_chunks": 2,
        "delay_between_batches": 5,
        "requests_per_minute": 450,
        "max_requests_per_day": 20000,
        "delay_between_requests": 0.15
    }
}


# Rate Limiter Setup
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


# Helper function to create a rate limiter function for a specific API
def create_rate_limit_function(rate_limiter: dict, api: str) -> Callable[[], None]:
    """Create a rate limiter function for the specified API"""
    def rate_limit_func():
        check_rate_limits(rate_limiter, api)
    return rate_limit_func


# Setup LLM Clients
def setup_clients():
    """Initialize clients for each LLM service"""
    try:
        # Claude setup
        verify_path = '/opt/homebrew/etc/openssl@3/cert.pem'
        http_client = httpx.Client(
            verify=verify_path if os.path.exists(verify_path) else True,
            timeout=60.0
        )
        claude_client = Anthropic(
            api_key=os.getenv('ANTHROPIC_API_KEY'),
            http_client=http_client
        )
        
        # Gemini setup
        gemini_api_key = os.getenv('GEMINI_API_KEY')
        if not gemini_api_key:
            raise ValueError("GEMINI_API_KEY not found")
        gemini.configure(api_key=gemini_api_key)
        gemini_client = gemini.GenerativeModel(
            model_name=API_CONFIGS["gemini"]["model"],
            generation_config={
                "max_output_tokens": API_CONFIGS["gemini"]["max_tokens"],
                "temperature": API_CONFIGS["gemini"]["temperature"]
            }
        )
        
        # OpenAI setup
        openai_api_key = os.getenv('OPENAI_API_KEY')
        if not openai_api_key:
            raise ValueError("OPENAI_API_KEY not found")
        openai_client = OpenAI(
            api_key=openai_api_key,
            timeout=60.0
        )
        
        return {
            "claude": claude_client,
            "gpt": openai_client,
            "gemini": gemini_client
        }
        
    except Exception as e:
        logging.error(f"Error setting up clients: {str(e)}")
        raise


# Make LLM Call
@retry(
    wait=wait_exponential(multiplier=1, min=4, max=60),
    stop=stop_after_attempt(5),
    retry=retry_if_exception_type((RateLimitError, TimeoutError))
)
def make_llm_request(client, api_type: str, prompt: str, system_prompt: str, rate_limit_func) -> str:
    """Make rate-limited API request with retries"""
    rate_limit_func()
    
    config = API_CONFIGS[api_type]
    
    try:
        if api_type == "claude":
            response = client.messages.create(
                model=config["model_name"],
                max_tokens=config["max_tokens"],
                messages=[{
                    "role": "user", 
                    "content": prompt
                }],
                system=system_prompt
            )
            return response.content[0].text
            
        elif api_type == "gemini":
            response = client.generate_content(
                prompt,
                generation_config={
                    "max_output_tokens": config["max_tokens"],
                    "temperature": config["temperature"]
                }
            )
            if hasattr(response, 'text'):
                return response.text
            elif response.candidates:
                return response.candidates[0].content.parts[0].text
            else:
                raise ValueError("No response generated from Gemini API")
                    
        elif api_type == "gpt":
            response = client.chat.completions.create(
                model=config["model"],
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=config["max_tokens"],
                temperature=config["temperature"]
            )
            return response.choices[0].message.content
            
    except Exception as e:
        logging.error(f"Error in {api_type} API request: {str(e)}")
        raise
