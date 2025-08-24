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
        "model_name": "claude-sonnet-4-20250514", 
        "max_tokens": 8192,
        "temperature": 0.3,
        "batch_size": 10,  
        "delay_between_chunks": 0.2, 
        "delay_between_batches": 1.0,  
        "requests_per_minute": 990,
        "max_requests_per_day": 20000,
        "delay_between_requests": 0.05  
    },
    "gemini": {
        "model": "models/gemini-2.5-pro",
        "max_tokens": 8192,
        "temperature": 0.3,
        "batch_size": 8,  
        "delay_between_chunks": 0.5,  
        "delay_between_batches": 2.0,  
        "requests_per_minute": 900,
        "max_requests_per_day": 50000,
        "delay_between_requests": 0.05,  
        "timeout": 60
    },
    "gpt": {
        "model": "gpt-4o",
        "max_tokens": 8192,
        "temperature": 0.3,
        "batch_size": 8,  
        "delay_between_chunks": 0.5,   
        "delay_between_batches": 2.0,  
        "requests_per_minute": 3000,
        "max_requests_per_day": 20000,
        "delay_between_requests": 0.08  
    }
}

# Gemini Safety Settings - ADD THIS NEW SECTION
GEMINI_SAFETY_SETTINGS = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH", 
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH"  # Keep some protection for truly dangerous content
    }
]


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
        
        gemini_api_key = os.getenv('GEMINI_API_KEY')
        if not gemini_api_key:
            raise ValueError("GEMINI_API_KEY not found")
        gemini.configure(api_key=gemini_api_key)
        gemini_client = gemini.GenerativeModel(
            model_name=API_CONFIGS["gemini"]["model"],
            generation_config={
                "max_output_tokens": API_CONFIGS["gemini"]["max_tokens"],
                "temperature": API_CONFIGS["gemini"]["temperature"]
            },
            safety_settings=GEMINI_SAFETY_SETTINGS  # ADD THIS LINE
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
            # Combine system prompt with user prompt for Gemini
            combined_prompt = f"System: {system_prompt}\n\nUser: {prompt}"
            
            response = client.generate_content(
                combined_prompt,
                generation_config={
                    "max_output_tokens": config["max_tokens"],
                    "temperature": config["temperature"]
                },
                safety_settings=GEMINI_SAFETY_SETTINGS  # ADD THIS LINE
            )
            
            # Improved response handling
            if hasattr(response, 'text') and response.text:
                return response.text
            elif hasattr(response, 'candidates') and response.candidates:
                # Try to extract text from candidates
                for candidate in response.candidates:
                    if hasattr(candidate, 'content') and candidate.content:
                        if hasattr(candidate.content, 'parts') and candidate.content.parts:
                            for part in candidate.content.parts:
                                if hasattr(part, 'text') and part.text:
                                    return part.text
                
                # If we get here, check finish_reason
                if response.candidates:
                    finish_reason = getattr(response.candidates[0], 'finish_reason', None)
                    if finish_reason == 2:  # SAFETY
                        logging.warning(f"Gemini response blocked by safety filters. Finish reason: {finish_reason}")
                        # Return a fallback response
                        return "// Test generation was blocked by content filters. Please review the requirement manually."
                    elif finish_reason == 3:  # RECITATION
                        logging.warning(f"Gemini response blocked due to recitation. Finish reason: {finish_reason}")
                        return "// Response blocked due to potential copyright content."
                    else:
                        logging.warning(f"Gemini response incomplete. Finish reason: {finish_reason}")
                        return f"// Gemini response incomplete with finish reason: {finish_reason}"
            
            # If we get here, something went wrong
            logging.error("Gemini response contained no valid text content")
            return "// Gemini response contained no valid text content"
                    
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


def count_tokens(text: str, api_type: str) -> int:
    """
    Count the number of tokens in a text string for the specified API.
    
    Args:
        text: The text to count tokens for
        api_type: The API type (claude, gemini, gpt)
        
    Returns:
        Estimated token count
    """
    if api_type == "claude":
        # Claude uses roughly 4 characters per token as a rough estimate
        return len(text) // 4
    elif api_type == "gemini":
        # Gemini uses roughly 4 characters per token as a rough estimate
        return len(text) // 4
    elif api_type == "gpt":
        # GPT uses tiktoken for accurate counts, but as a fallback:
        try:
            import tiktoken
            enc = tiktoken.encoding_for_model("gpt-4")
            return len(enc.encode(text))
        except (ImportError, Exception):
            # Fallback to rough estimate if tiktoken not available
            return len(text) // 4
    else:
        # Default rough estimate
        return len(text) // 4