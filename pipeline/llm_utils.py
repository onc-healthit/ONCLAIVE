"""
LLM Utilities Module for API interactions with Claude, Gemini, and GPT models.
"""
# Imports
import os
import time
import logging
import httpx
from typing import Dict, Any, Callable, Union, List
import dotenv

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
    },
    "aip": {
        'model': 'nvidia/Llama-3_3-Nemotron-Super-49B-v1',
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

dotenv.load_dotenv()

def format_content_for_api(content: Union[str, dict, list], api_type: str) -> Union[str, List[dict], dict]:
    """Format content appropriately for each API"""
    if api_type == "claude":
        return [{
            "type": "text",
            "text": content
        }]
    elif api_type == "gemini":
        return [{  
            "parts": [{
                "text": content
            }]
        }]
    return content

class LLMApiClient:
    
    
    # Rate Limiter Setup

     # Setup LLM Clients
    def __init__(self, config=API_CONFIGS, verify_path='/opt/homebrew/etc/openssl@3/cert.pem', system_prompt=None):
        """Initialize clients for each LLM service"""
        self.logger = logging.getLogger(__name__)
        self.config = config
        self.clients = {}
        self.system_prompt = system_prompt
        try:
            # Claude setup
            claude_api_key = os.getenv('ANTHROPIC_API_KEY')
            if not claude_api_key:
                self.logger.warning("ANTRHOPIC_API_KEY not found. Claude API client will not be loaded.")
            else:
                http_client = httpx.Client(
                    verify=verify_path if os.path.exists(verify_path) else True,
                    timeout=60.0
                )
                self.clients['claude'] = Anthropic(
                    api_key=claude_api_key,
                    http_client=http_client
                )
            
            # Gemini setup
            gemini_api_key = os.getenv('GEMINI_API_KEY')
            if not gemini_api_key:
                self.logger.warning("GEMINI_API_KEY not found. Gemini API client will not be loaded.")
            else:
                gemini.configure(api_key=gemini_api_key)
                self.clients['gemini'] = gemini.GenerativeModel(
                    model_name=self.config["gemini"]["model"],
                    generation_config={
                        "max_output_tokens": self.config["gemini"]["max_tokens"],
                        "temperature": self.config["gemini"]["temperature"]
                    }
                )
            
            # OpenAI setup
            openai_api_key = os.getenv('OPENAI_API_KEY')
            if not openai_api_key:
                self.logger.warning("OPENAI_API_KEY not found. GPT API client will not be loaded.")
            else:
                self.clients['gpt'] = OpenAI(
                    api_key=openai_api_key,
                    timeout=60.0
                )
            
            aip_api_key = os.getenv("AIP_API_KEY")
            if aip_api_key:
                self.clients['aip'] = OpenAI(
                    base_url="https://models.k8s.aip.mitre.org/v1",
                    api_key=aip_api_key,
                    timeout=60.0
                )
            
        except Exception as e:
            logging.error(f"Error setting up clients: {str(e)}")
            raise

        self.rate_limiter = self.create_rate_limiter(config)

    def create_rate_limiter(self, config):
        """Create a rate limiter state dictionary for all APIs"""
        return {
            api: {
                'requests': [],
                'daily_requests': 0,
                'last_reset': time.time()
            }
            for api in config.keys()
        }

    def check_rate_limits(self, api: str):
        """Check and wait if rate limits would be exceeded"""
        rate_limiter = self.rate_limiter
        if api not in rate_limiter:
            raise ValueError(f"Unknown API: {api}")
            
        now = time.time()
        state = rate_limiter[api]
        config = self.config[api]
        
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

    # Make LLM Call
    @retry(
        wait=wait_exponential(multiplier=1, min=4, max=60),
        stop=stop_after_attempt(5),
        retry=retry_if_exception_type((RateLimitError, TimeoutError))
    )
    def make_one_llm_request(self, api_type: str, prompt: str, system_prompt):
        config = self.config[api_type]
        client = self.clients[api_type]
        self.check_rate_limits(api_type)
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
            elif api_type == "aip":
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
            raise Exception(e)

    def make_llm_request(self, api_type: str, prompt: Union[str, List[str]], sys_prompt=None, raise_on_error=True, reformat=True) -> str:
        """Make rate-limited API request with retries"""
        
        if api_type not in self.clients:
            raise ValueError(f"Unknown API: {api_type}. Valid API types are: {','.join(self.clients.keys())}")
        
        
        if not sys_prompt:
            system_prompt = self.system_prompt
        else:
            system_prompt = sys_prompt
        if type(prompt) == str:
            if reformat:
                query = format_content_for_api(prompt, api_type)
            else:
                query = prompt
            return self.make_one_llm_request(api_type, query, system_prompt)
        else:
            responses = []
            for i,p in enumerate(prompt):
                print(f"{i+1} of {len(prompt)}", end='\r')
                if reformat:
                    query = format_content_for_api(p, api_type)
                else:
                    query = p
                try:
                    responses.append(self.make_one_llm_request(api_type, query, system_prompt))
                except Exception as e:
                    if raise_on_error:
                        raise Exception(e)
                    else:
                        responses.append({'error': str(e)})
            return responses


    def count_tokens(self, text: str, api_type: str) -> int:
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