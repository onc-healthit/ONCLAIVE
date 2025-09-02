"""
LLM Utilities Module for API interactions with Claude, Gemini, and GPT models.

This module provides a unified interface for interacting with multiple LLM APIs,
including rate limiting, error handling, and safety filter management.

Features:
- Multi-API support (Claude, Gemini, GPT, AIP)
- Automatic rate limiting and token management
- Safety filter exception handling
- Token counting utilities
- Configurable API parameters

Usage:
    from llm_utils import LLMApiClient, SafetyFilterException
    
    # Initialize client
    client = LLMApiClient()
    
    # Make a request
    response = client.make_llm_request("claude", "Your prompt here", sys_prompt="System prompt")
"""

import os
import time
import logging
import httpx
from typing import Dict, Any, Union, List
from dotenv import load_dotenv

try:
    from anthropic import Anthropic, RateLimitError
    import google.generativeai as gemini
    from openai import OpenAI
    from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type
except ImportError:
    raise ImportError("Please install required packages: pip install anthropic google-generativeai openai tenacity")

# Load environment variables
load_dotenv()

# API Configuration
API_CONFIGS = {
    "claude": {
        "model_name": "claude-sonnet-4-20250514", 
        "max_tokens": 8192,
        "temperature": 0,
        "batch_size": 10,  
        "delay_between_chunks": 0.1, 
        "delay_between_batches": 5,  
        "requests_per_minute": 3800,  
        "input_tokens_per_minute": 1900000,  
        "output_tokens_per_minute": 380000,  
        "delay_between_requests": 0.2  
    },
    "gemini": {
        "model": "models/gemini-1.5-pro",
        "max_tokens": 8192,
        "temperature": 0.3,
        "batch_size": 8,  
        "delay_between_chunks": 0.5,  
        "delay_between_batches": 2.0,  
        "requests_per_minute": 140,  # 93% of 150 RPM
        "tokens_per_minute": 1900000,  # 95% of 2M TPM (combined input+output)
        "max_requests_per_day": 9500,  # 95% of 10k daily
        "delay_between_requests": 1,  
        "timeout": 900
    },
    "gpt": {
        "model": "gpt-5-mini",
        "max_tokens": 16384,
        "temperature": 1,
        "batch_size": 20,  
        "delay_between_chunks": 0.01,   
        "delay_between_batches": 1,  
        "requests_per_minute": 9500,  # 95% of 5000 RPM
        "tokens_per_minute": 1900000,  # 95% of 800k TPM (combined input+output)
        "max_requests_per_day": 190000000,  # 95% of 100M batch TPD (very high)
        "delay_between_requests": 0.006 
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


class SafetyFilterException(Exception):
    """
    Exception raised when content is blocked by safety filters.
    
    Attributes:
        blocked_content: Sample of the content that triggered the safety filter
    """
    def __init__(self, message: str, blocked_content: str = None):
        super().__init__(message)
        self.blocked_content = blocked_content


def format_content_for_api(content: str, api_type: str) -> Union[str, List[Dict], Dict]:
    """
    Format content appropriately for each API's expected input format.
    
    Args:
        content: The text content to format
        api_type: Type of API ('claude', 'gemini', 'gpt', 'aip')
        
    Returns:
        Formatted content structure for the specific API
    """
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
    """
    Unified client for multiple LLM APIs with rate limiting and error handling.
    
    This class provides a consistent interface for interacting with Claude, Gemini, GPT,
    and AIP models while handling rate limits, token management, and safety filters.
    
    Attributes:
        config: API configuration dictionary
        clients: Dictionary of initialized API clients
        rate_limiter: Rate limiting state tracker
        safety_blocked_count: Counter for safety filter blocks
    """
    
    def __init__(self, config: Dict = None, verify_path: str = '/opt/homebrew/etc/openssl@3/cert.pem', 
                 system_prompt: str = None):
        """
        Initialize clients for each LLM service.
        
        Args:
            config: API configuration dictionary (uses default if None)
            verify_path: SSL certificate path for Claude client
            system_prompt: Default system prompt for all requests
            
        Raises:
            ImportError: If required API packages are not installed
            Exception: If client initialization fails
        """
        self.logger = logging.getLogger(__name__)
        self.config = config or API_CONFIGS
        self.clients = {}
        self.system_prompt = system_prompt
        self.safety_blocked_count = 0

        self._initialize_clients(verify_path)
        self.rate_limiter = self._create_rate_limiter(self.config)

    def _initialize_clients(self, verify_path: str) -> None:
        """Initialize all available API clients based on environment variables."""
        try:
            # Claude setup
            claude_api_key = os.getenv('ANTHROPIC_API_KEY')
            if claude_api_key:
                http_client = httpx.Client(
                    verify=verify_path if os.path.exists(verify_path) else True,
                    timeout=httpx.Timeout(900.0, connect=300.0),
                    limits=httpx.Limits(max_keepalive_connections=5, max_connections=10),
                )
                self.clients['claude'] = Anthropic(
                    api_key=claude_api_key,
                    http_client=http_client
                )
            else:
                self.logger.warning("ANTHROPIC_API_KEY not found. Claude API client will not be loaded.")
            
            # Gemini setup
            gemini_api_key = os.getenv('GEMINI_API_KEY')
            if gemini_api_key:
                gemini.configure(api_key=gemini_api_key)
                
                # Configure safety settings for technical content
                safety_settings = [
                    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
                ]
                
                self.clients['gemini'] = gemini.GenerativeModel(
                    model_name=self.config["gemini"]["model"],
                    generation_config={
                        "max_output_tokens": self.config["gemini"]["max_tokens"],
                        "temperature": self.config["gemini"]["temperature"]
                    },
                    safety_settings=safety_settings
                )
            else:
                self.logger.warning("GEMINI_API_KEY not found. Gemini API client will not be loaded.")
            
            # OpenAI setup
            openai_api_key = os.getenv('OPENAI_API_KEY')
            if openai_api_key:
                self.clients['gpt'] = OpenAI(
                    api_key=openai_api_key,
                    timeout=900.0
                )
            else:
                self.logger.warning("OPENAI_API_KEY not found. GPT API client will not be loaded.")
            
            # AIP setup
            aip_api_key = os.getenv("AIP_API_KEY")
            if aip_api_key:
                self.clients['aip'] = OpenAI(
                    base_url="https://models.k8s.aip.mitre.org/v1",
                    api_key=aip_api_key,
                    timeout=60.0
                )
            
        except Exception as e:
            self.logger.error(f"Error setting up clients: {str(e)}")
            raise

    def _create_rate_limiter(self, config: Dict) -> Dict:
        """
        Create rate limiter state dictionary for all APIs.
        
        Args:
            config: API configuration dictionary
            
        Returns:
            Dictionary containing rate limiter state for each API
        """
        limiter = {}
        for api in config.keys():
            limiter[api] = {
                'requests': [],
                'daily_requests': 0,
                'last_reset': time.time()
            }
            
            # Add token tracking based on API type
            if api == "claude":
                # Claude has separate input/output limits
                limiter[api]['input_tokens'] = []
                limiter[api]['output_tokens'] = []
            elif api in ["gemini", "gpt"]:
                # Gemini and GPT have combined token limits
                limiter[api]['tokens'] = []
        
        return limiter

    def check_rate_limits(self, api: str, input_text: str = "", requested_output_tokens: int = None) -> None:
        """
        Check and enforce rate limits for the specified API.
        
        This method implements comprehensive rate limiting including:
        - Requests per minute
        - Tokens per minute (API-specific)
        - Daily request limits (where applicable)
        - Minimum delays between requests
        
        Args:
            api: API type to check limits for
            input_text: Input text for token estimation
            requested_output_tokens: Expected output tokens (optional)
            
        Raises:
            ValueError: If API type is unknown
            Exception: If daily limits are exceeded
        """
        if api not in self.rate_limiter:
            raise ValueError(f"Unknown API: {api}")
            
        now = time.time()
        state = self.rate_limiter[api]
        config = self.config[api]
        
        # Estimate tokens based on API type
        estimated_input_tokens = len(input_text) // 4
        estimated_output_tokens = requested_output_tokens or config["max_tokens"]
        estimated_total_tokens = estimated_input_tokens + estimated_output_tokens
        
        # Reset daily counts if needed
        if now - state['last_reset'] >= 86400:  # 24 hours
            state['daily_requests'] = 0
            state['last_reset'] = now
        
        # Check daily request limit
        daily_limit = config.get('max_requests_per_day')
        if daily_limit and state['daily_requests'] >= daily_limit:
            raise Exception(f"{api} daily request limit ({daily_limit}) exceeded")
        
        # Clean old entries (older than 1 minute)
        cutoff = now - 60
        state['requests'] = [req_time for req_time in state['requests'] if req_time > cutoff]
        
        if api == "claude":
            state['input_tokens'] = [(t, tokens) for t, tokens in state['input_tokens'] if t > cutoff]
            state['output_tokens'] = [(t, tokens) for t, tokens in state['output_tokens'] if t > cutoff]
        elif api in ["gemini", "gpt"]:
            state['tokens'] = [(t, tokens) for t, tokens in state['tokens'] if t > cutoff]
        
        # Calculate required wait times
        wait_times = []
        
        # Check request limit
        current_requests = len(state['requests'])
        if current_requests >= config['requests_per_minute']:
            wait_time = 60 - (now - state['requests'][0])
            if wait_time > 0:
                wait_times.append(("requests", wait_time))
        
        # Check token limits (API-specific)
        if api == "claude":
            current_input = sum(tokens for _, tokens in state['input_tokens'])
            current_output = sum(tokens for _, tokens in state['output_tokens'])
            
            if current_input + estimated_input_tokens > config.get('input_tokens_per_minute', float('inf')):
                oldest_input = min((t for t, _ in state['input_tokens']), default=now)
                wait_time = 60 - (now - oldest_input)
                if wait_time > 0:
                    wait_times.append(("input_tokens", wait_time))
            
            if current_output + estimated_output_tokens > config.get('output_tokens_per_minute', float('inf')):
                oldest_output = min((t for t, _ in state['output_tokens']), default=now)
                wait_time = 60 - (now - oldest_output)
                if wait_time > 0:
                    wait_times.append(("output_tokens", wait_time))
        
        elif api in ["gemini", "gpt"]:
            current_tokens = sum(tokens for _, tokens in state['tokens'])
            token_limit = config.get('tokens_per_minute', float('inf'))
            
            if current_tokens + estimated_total_tokens > token_limit:
                oldest_token = min((t for t, _ in state['tokens']), default=now)
                wait_time = 60 - (now - oldest_token)
                if wait_time > 0:
                    wait_times.append(("tokens", wait_time))
        
        # Wait if necessary
        if wait_times:
            limit_type, max_wait = max(wait_times, key=lambda x: x[1])
            self.logger.info(f"{api} rate limit hit ({limit_type}), waiting {max_wait:.1f}s")
            time.sleep(max_wait)
            # Recursive call to re-check
            return self.check_rate_limits(api, input_text, requested_output_tokens)
        
        # Add minimum delay between requests
        if state['requests'] and now - state['requests'][-1] < config['delay_between_requests']:
            time.sleep(config['delay_between_requests'])
        
        # Record this request
        state['requests'].append(now)
        state['daily_requests'] += 1
        
        # Record token usage
        if api == "claude":
            state['input_tokens'].append((now, estimated_input_tokens))
            state['output_tokens'].append((now, estimated_output_tokens))
        elif api in ["gemini", "gpt"]:
            state['tokens'].append((now, estimated_total_tokens))

    @retry(
        wait=wait_exponential(multiplier=2, min=60, max=7200),
        stop=stop_after_attempt(100),
        retry=(retry_if_exception_type(RateLimitError) | 
               retry_if_exception_type(TimeoutError) | 
               retry_if_exception_type(Exception))
    )
    def make_one_llm_request(self, api_type: str, prompt: str, system_prompt: str, max_tokens: int = None) -> str:
        """
        Make a single LLM API request with retry logic and rate limiting.
        
        Args:
            api_type: Type of API ('claude', 'gemini', 'gpt', 'aip')
            prompt: User prompt text
            system_prompt: System prompt text
            max_tokens: Maximum tokens to generate (uses config default if None)
            
        Returns:
            Generated text response from the LLM
            
        Raises:
            SafetyFilterException: If content is blocked by safety filters
            Exception: For various API errors
        """
        config = self.config[api_type]
        client = self.clients[api_type]
        tokens_limit = max_tokens if max_tokens is not None else config["max_tokens"]
        
        full_input = f"{system_prompt or ''}\n{prompt}"
        self.check_rate_limits(api_type, full_input, tokens_limit)

        try:
            if api_type == "claude":
                response = client.messages.create(
                    model=config["model_name"],
                    max_tokens=tokens_limit,
                    messages=[{
                        "role": "user", 
                        "content": prompt
                    }],
                    system=system_prompt
                )
                return response.content[0].text
                
            elif api_type == "gemini":
                # Combine system prompt and user prompt for Gemini
                if system_prompt:
                    combined_prompt = f"System: {system_prompt}\n\nUser: {prompt}"
                else:
                    combined_prompt = prompt
                
                response = client.generate_content(
                    combined_prompt,
                    generation_config={
                        "max_output_tokens": tokens_limit,
                        "temperature": config["temperature"]
                    }
                )
                
                # Check for safety filter blocks
                if response.candidates and len(response.candidates) > 0:
                    candidate = response.candidates[0]
                    if candidate.finish_reason == 2:  # SAFETY
                        problematic_content = combined_prompt[:500] + ("..." if len(combined_prompt) > 500 else "")
                        raise SafetyFilterException(
                            "Gemini blocked content for safety reasons.", 
                            blocked_content=problematic_content
                        )
                
                # Extract response text
                if hasattr(response, 'text') and response.text:
                    return response.text
                elif response.candidates and len(response.candidates) > 0:
                    candidate = response.candidates[0]
                    if candidate.content and candidate.content.parts:
                        return candidate.content.parts[0].text
                    else:
                        raise ValueError("No content returned from Gemini")
                else:
                    raise ValueError("No response generated from Gemini API")
        
            elif api_type == "aip":
                response = client.chat.completions.create(
                    model=config["model"],
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=tokens_limit,
                    temperature=config["temperature"]
                )
                return response.choices[0].message.content
                
            elif api_type == "gpt":
                response = client.responses.create(
                    model=config["model"],
                    input=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": prompt}
                    ],
                    reasoning={"effort": "minimal"},
                    temperature=config["temperature"],
                    max_output_tokens=tokens_limit
                )
                return response.output_text
                
        except SafetyFilterException:
            # Re-raise safety filter exceptions without wrapping them
            raise
        except Exception as e:
            self.logger.error(f"Error in {api_type} API request: {str(e)}")
            raise


    def make_llm_request(self, api_type: str, prompt: Union[str, List[str]], sys_prompt: str = None, 
                        raise_on_error: bool = True, reformat: bool = True, max_tokens: int = None) -> Union[str, List]:
        """
        Make LLM API request with comprehensive error handling.
        
        This is the main public interface for making LLM requests. It handles:
        - Single prompts or lists of prompts
        - Safety filter exceptions
        - API formatting
        - Error handling and reporting
        
        Args:
            api_type: Type of API ('claude', 'gemini', 'gpt', 'aip')
            prompt: Single prompt string or list of prompt strings
            sys_prompt: System prompt (uses instance default if None)
            raise_on_error: Whether to raise exceptions or return error info
            reformat: Whether to reformat content for API-specific format
            max_tokens: Maximum tokens to generate
            
        Returns:
            Generated response string (for single prompt) or list of responses
            
        Raises:
            ValueError: If API type is unknown or unavailable
        """
        if api_type not in self.clients:
            raise ValueError(f"Unknown API: {api_type}. Valid API types are: {','.join(self.clients.keys())}")
        
        system_prompt = sys_prompt or self.system_prompt
            
        if isinstance(prompt, str):
            # Single prompt
            query = format_content_for_api(prompt, api_type) if reformat else prompt
            try:
                return self.make_one_llm_request(api_type, query, system_prompt, max_tokens)
            except SafetyFilterException as e:
                self.safety_blocked_count += 1
                print(f"\nSAFETY FILTER BLOCKED CONTENT #{self.safety_blocked_count}")
                print("=" * 60)
                print("BLOCKED CONTENT SAMPLE:")
                print(e.blocked_content)
                print("=" * 60)
                print("Skipping this chunk and continuing...\n")
                
                return "[CONTENT BLOCKED BY SAFETY FILTER - SKIPPED]" if raise_on_error else {
                    'error': 'safety_filter_blocked', 
                    'content_sample': e.blocked_content
                }
        else:
            # List of prompts
            responses = []
            for i, p in enumerate(prompt):
                print(f"{i+1} of {len(prompt)}", end='\r')
                query = format_content_for_api(p, api_type) if reformat else p
                
                try:
                    response = self.make_one_llm_request(api_type, query, system_prompt, max_tokens)
                    responses.append(response)
                except SafetyFilterException as e:
                    self.safety_blocked_count += 1
                    print(f"\nSAFETY FILTER BLOCKED CONTENT #{self.safety_blocked_count}")
                    print("=" * 60)
                    print("BLOCKED CONTENT SAMPLE:")
                    print(e.blocked_content)
                    print("=" * 60)
                    print("Skipping this chunk and continuing...\n")
                    
                    if raise_on_error:
                        responses.append("[CONTENT BLOCKED BY SAFETY FILTER - SKIPPED]")
                    else:
                        responses.append({'error': 'safety_filter_blocked', 'content_sample': e.blocked_content})
                except Exception as e:
                    if raise_on_error:
                        raise
                    else:
                        responses.append({'error': str(e)})
            
            return responses

    def count_tokens(self, text: str, api_type: str) -> int:
        """
        Count the number of tokens in a text string for the specified API.
        
        Args:
            text: The text to count tokens for
            api_type: The API type ('claude', 'gemini', 'gpt', 'aip')
            
        Returns:
            Estimated token count
            
        Note:
            Uses tiktoken for GPT when available, falls back to character-based 
            estimation (4 chars per token) for all APIs.
        """
        if api_type == "gpt":
            try:
                import tiktoken
                enc = tiktoken.encoding_for_model("gpt-4")
                return len(enc.encode(text))
            except (ImportError, Exception):
                pass
        
        # Default estimation for all APIs
        return len(text) // 4