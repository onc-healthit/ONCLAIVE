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
        "model_name": "claude-sonnet-4-20250514", 
        "max_tokens": 8192,
        "temperature": 0.3,
        "batch_size": 10,  
        "delay_between_chunks": 0.2, 
        "delay_between_batches": 1.0,  
        "requests_per_minute": 900,  
        "input_tokens_per_minute": 425000,  
        "output_tokens_per_minute": 85000,  
        "delay_between_requests": 1  
    },
    "gemini": {
        "model": "models/gemini-2.5-pro",
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
        "model": "gpt-4.1",
        "max_tokens": 8192,
        "temperature": 0.3,
        "batch_size": 8,  
        "delay_between_chunks": 0.5,   
        "delay_between_batches": 2.0,  
        "requests_per_minute": 4750,  # 95% of 5000 RPM
        "tokens_per_minute": 760000,  # 95% of 800k TPM (combined input+output)
        "max_requests_per_day": 95000000,  # 95% of 100M batch TPD (very high)
        "delay_between_requests": 0.5 
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

# Custom exception for safety filter blocks
class SafetyFilterException(Exception):
    """Exception raised when content is blocked by safety filters"""
    def __init__(self, message, blocked_content=None):
        super().__init__(message)
        self.blocked_content = blocked_content


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
        self.safety_blocked_count = 0

        try:
            # Claude setup
            claude_api_key = os.getenv('ANTHROPIC_API_KEY')
            if not claude_api_key:
                self.logger.warning("ANTRHOPIC_API_KEY not found. Claude API client will not be loaded.")
            else:
                http_client = httpx.Client(
                    verify=verify_path if os.path.exists(verify_path) else True,
                    timeout=httpx.Timeout(900.0, connect=300.0),  # 15 minutes total, 5 minutes connect
                    limits=httpx.Limits(max_keepalive_connections=5, max_connections=10),  # Reduced connections
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
                
                # Configure safety settings for technical content
                safety_settings = [
                    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}#, 
                    #{"category": "HARM_CATEGORY_CIVIC_INTEGRITY", "threshold": "BLOCK_NONE"}
                ]
                
                self.clients['gemini'] = gemini.GenerativeModel(
                    model_name=self.config["gemini"]["model"],
                    generation_config={
                        "max_output_tokens": self.config["gemini"]["max_tokens"],
                        "temperature": self.config["gemini"]["temperature"]
                    },
                    safety_settings=safety_settings
                )
            
            # OpenAI setup
            openai_api_key = os.getenv('OPENAI_API_KEY')
            if not openai_api_key:
                self.logger.warning("OPENAI_API_KEY not found. GPT API client will not be loaded.")
            else:
                self.clients['gpt'] = OpenAI(
                    api_key=openai_api_key,
                    timeout=900.0
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

    def check_rate_limits(self, api: str, input_text: str = "", requested_output_tokens: int = None):
        """Check and wait if rate limits would be exceeded - supports all models"""
        rate_limiter = self.rate_limiter
        if api not in rate_limiter:
            raise ValueError(f"Unknown API: {api}")
            
        now = time.time()
        state = rate_limiter[api]
        config = self.config[api]
        
        # Estimate tokens based on API type
        if api == "claude":
            estimated_input_tokens = len(input_text) // 4
            estimated_output_tokens = requested_output_tokens or config["max_tokens"]
            estimated_total_tokens = estimated_input_tokens + estimated_output_tokens
        elif api in ["gemini", "gpt"]:
            # For Gemini/GPT, estimate total tokens (input + output)
            estimated_input_tokens = len(input_text) // 4
            estimated_output_tokens = requested_output_tokens or config["max_tokens"]
            estimated_total_tokens = estimated_input_tokens + estimated_output_tokens
        else:
            estimated_input_tokens = 0
            estimated_output_tokens = 0
            estimated_total_tokens = 0
        
        # Reset daily counts if needed
        day_seconds = 24 * 60 * 60
        if now - state['last_reset'] >= day_seconds:
            state['daily_requests'] = 0
            state['last_reset'] = now
        
        # Check daily request limit (Gemini only has this)
        daily_limit = config.get('max_requests_per_day')
        if daily_limit and state['daily_requests'] >= daily_limit:
            raise Exception(f"{api} daily request limit ({daily_limit}) exceeded")
        
        # Remove old entries outside the current minute
        cutoff = now - 60
        state['requests'] = [req_time for req_time in state['requests'] if req_time > cutoff]
        
        # Clean token tracking based on API type
        if api == "claude":
            state['input_tokens'] = [(t, tokens) for t, tokens in state['input_tokens'] if t > cutoff]
            state['output_tokens'] = [(t, tokens) for t, tokens in state['output_tokens'] if t > cutoff]
        elif api in ["gemini", "gpt"]:
            state['tokens'] = [(t, tokens) for t, tokens in state['tokens'] if t > cutoff]
        
        # Check limits and calculate wait times
        wait_times = []
        
        # 1. Request limit (all APIs have this)
        current_requests = len(state['requests'])
        if current_requests >= config['requests_per_minute']:
            wait_time = 60 - (now - state['requests'][0])
            if wait_time > 0:
                wait_times.append(("requests", wait_time))
        
        # 2. Token limits (API-specific)
        if api == "claude":
            # Claude: separate input/output limits
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
            # Gemini/GPT: combined token limit
            current_tokens = sum(tokens for _, tokens in state['tokens'])
            token_limit = config.get('tokens_per_minute', float('inf'))
            
            if current_tokens + estimated_total_tokens > token_limit:
                oldest_token = min((t for t, _ in state['tokens']), default=now)
                wait_time = 60 - (now - oldest_token)
                if wait_time > 0:
                    wait_times.append(("tokens", wait_time))
        
        # Wait for the longest required time
        if wait_times:
            limit_type, max_wait = max(wait_times, key=lambda x: x[1])
            self.logger.info(f"{api} rate limit hit ({limit_type}), waiting {max_wait:.1f}s")
            
            # Log current usage for debugging
            if api == "claude":
                current_input = sum(tokens for _, tokens in state['input_tokens'])
                current_output = sum(tokens for _, tokens in state['output_tokens'])
                self.logger.info(f"Usage: {current_requests} req, {current_input} in_tokens, {current_output} out_tokens")
            elif api in ["gemini", "gpt"]:
                current_tokens = sum(tokens for _, tokens in state['tokens'])
                self.logger.info(f"Usage: {current_requests} req, {current_tokens} tokens")
            
            time.sleep(max_wait)
            # Recursive call to re-check
            return self.check_rate_limits(api, input_text, requested_output_tokens)
        
        # Add minimum delay between requests
        if state['requests'] and now - state['requests'][-1] < config['delay_between_requests']:
            time.sleep(config['delay_between_requests'])
        
        # Record this request
        state['requests'].append(now)
        state['daily_requests'] += 1
        
        # Record token usage based on API type
        if api == "claude":
            state['input_tokens'].append((now, estimated_input_tokens))
            state['output_tokens'].append((now, estimated_output_tokens))
        elif api in ["gemini", "gpt"]:
            state['tokens'].append((now, estimated_total_tokens))
        
        # Periodic usage logging
        if len(state['requests']) % 20 == 0:
            if api == "claude":
                current_input = sum(tokens for _, tokens in state['input_tokens'])
                current_output = sum(tokens for _, tokens in state['output_tokens'])
                self.logger.info(f"{api} usage: {current_requests + 1} req, {current_input} in, {current_output} out")
            elif api in ["gemini", "gpt"]:
                current_tokens = sum(tokens for _, tokens in state['tokens'])
                self.logger.info(f"{api} usage: {current_requests + 1} req, {current_tokens} tokens")


    def extract_problematic_content(self, prompt: str) -> str:
        """Extract a sample of the content that might have triggered safety filters"""
        return prompt


    # Make LLM Call
    @retry(
        wait=wait_exponential(multiplier=2, min=60, max=7200),
        stop=stop_after_attempt(100),
        retry=(retry_if_exception_type(RateLimitError) | 
               retry_if_exception_type(TimeoutError) | 
               retry_if_exception_type(Exception))
    )
    def make_one_llm_request(self, api_type: str, prompt: str, system_prompt, max_tokens=None):
        """Enhanced version with max_tokens parameter"""
        config = self.config[api_type]
        client = self.clients[api_type]
        tokens_limit = max_tokens if max_tokens is not None else config["max_tokens"]
        
        # AUTO-STREAMING LOGIC: Decide if should stream
        # if api_type == "claude":
        #     # Estimate request size
        #     full_input = f"{system_prompt or ''}\n{prompt}"
        #     estimated_input_tokens = len(full_input) // 4
        #     estimated_output_tokens = tokens_limit

        #     should_stream = (
        #         estimated_input_tokens > 30000 or  # Large input
        #         estimated_output_tokens > 8000 or  # Large output  
        #         (estimated_input_tokens + estimated_output_tokens) > 40000  # Large combined
        #     )
            
        #     if should_stream:
        #         logging.info(f" Auto-streaming: {estimated_input_tokens} input + {estimated_output_tokens} output tokens")
        #         return self.make_one_llm_request_streaming(api_type, prompt, system_prompt, max_tokens)
    
        
        full_input = f"{system_prompt or ''}\n{prompt}"
        self.check_rate_limits(api_type, full_input, tokens_limit)

        try:
            if api_type == "claude":
                response = client.messages.create(
                    model=config["model_name"],
                    max_tokens=tokens_limit,  # Use the tokens_limit variable
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
                        "max_output_tokens": tokens_limit,  # Use the tokens_limit variable
                        "temperature": config["temperature"]
                    }
                )
                
                # Check for safety filter blocks FIRST
                if response.candidates and len(response.candidates) > 0:
                    candidate = response.candidates[0]
                    if candidate.finish_reason == 2:  # SAFETY
                        problematic_content = combined_prompt[:500] + ("..." if len(combined_prompt) > 500 else "")
                        raise SafetyFilterException(
                            "Gemini blocked content for safety reasons.", 
                            blocked_content=problematic_content
                        )
                
                # Then try to get the text
                try:
                    if hasattr(response, 'text') and response.text:
                        return response.text
                    elif response.candidates and len(response.candidates) > 0:
                        candidate = response.candidates[0]
                        if candidate.content and candidate.content.parts:
                            return candidate.content.parts[0].text
                        else:
                            raise ValueError(f"No content returned from Gemini")
                    else:
                        raise ValueError("No response generated from Gemini API")
                except AttributeError:
                    if response.candidates and len(response.candidates) > 0:
                        return response.candidates[0].content.parts[0].text
                    else:
                        raise ValueError("Unable to extract text from Gemini response")
        
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
                # Prepare the request parameters
                request_params = {
                    "model": config["model"],
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": config["temperature"]
                }
                
                # Use the correct token parameter based on the model
                #model_name = config["model"]
                #if "gpt-4o" in model_name or "gpt-4-turbo" in model_name or "gpt-5" in model_name:
                    # Newer models use max_completion_tokens
                request_params["max_completion_tokens"] = tokens_limit
                #else:
                    # Older models use max_tokens
                    #request_params["max_tokens"] = tokens_limit
                
                #try:
                response = client.chat.completions.create(**request_params)
                return response.choices[0].message.content
                #except Exception as e:
                    # If we get the parameter error, try switching the parameter
                    #if "max_tokens" in str(e) and "max_completion_tokens" in str(e):
                        #logging.info("Switching GPT token parameter due to API error")
                        #if "max_tokens" in request_params:
                            #request_params["max_completion_tokens"] = request_params.pop("max_tokens")
                        #elif "max_completion_tokens" in request_params:
                            #request_params["max_tokens"] = request_params.pop("max_completion_tokens")
                        
                        # Retry with the corrected parameter
                        #response = client.chat.completions.create(**request_params)
                        #return response.choices[0].message.content
                    #else:
                        #raise e
                
        except SafetyFilterException:
            # Re-raise safety filter exceptions without wrapping them
            raise
        except Exception as e:
            logging.error(f"Error in {api_type} API request: {str(e)}")
            raise Exception(e)
        

    def make_one_llm_request_streaming(self, api_type: str, prompt: str, system_prompt, max_tokens=None):
        """Streaming version of make_one_llm_request (Claude only)"""
        
        if api_type != "claude":
            # Fall back to regular method for non-Claude APIs
            return self.make_one_llm_request(api_type, prompt, system_prompt, max_tokens)
        
        config = self.config[api_type]
        client = self.clients[api_type]
        tokens_limit = max_tokens if max_tokens is not None else config["max_tokens"]
        
        full_input = f"{system_prompt or ''}\n{prompt}"
        self.check_rate_limits(api_type, full_input, tokens_limit)
        
        try:
            logging.info("🌊 Using streaming for large request...")
            
            # Use Anthropic SDK's built-in streaming
            with client.messages.stream(
                model=config["model_name"],
                max_tokens=tokens_limit,
                messages=[{
                    "role": "user", 
                    "content": prompt
                }],
                system=system_prompt
            ) as stream:
                # Collect all text chunks
                full_response = ""
                chunk_count = 0
                
                for text in stream.text_stream:
                    full_response += text
                    chunk_count += 1
                    
                    # Progress indicator every 100 chunks
                    if chunk_count % 100 == 0:
                        logging.info(f"📥 Received {len(full_response)} characters so far...")
                
                logging.info(f"✅ Streaming complete: {len(full_response)} characters, {chunk_count} chunks")
                return full_response
                
        except Exception as e:
            logging.error(f"Streaming error in {api_type}: {e}")
            # Fall back to regular request if streaming fails
            logging.info("🔄 Falling back to regular request...")
            return self.make_one_llm_request(api_type, prompt, system_prompt, max_tokens)



    def make_llm_request(self, api_type: str, prompt: Union[str, List[str]], sys_prompt=None, 
                     raise_on_error=True, reformat=True, max_tokens=None) -> str:
        """Make rate-limited API request with retries - enhanced with max_tokens"""
        
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
            try:
                return self.make_one_llm_request(api_type, query, system_prompt, max_tokens)
            except SafetyFilterException as e:
                self.safety_blocked_count += 1
                print(f"\n⚠️  SAFETY FILTER BLOCKED CONTENT #{self.safety_blocked_count}")
                print("=" * 60)
                print("BLOCKED CONTENT SAMPLE:")
                print(e.blocked_content)
                print("=" * 60)
                print("Skipping this chunk and continuing...\n")
                
                if raise_on_error:
                    return "[CONTENT BLOCKED BY SAFETY FILTER - SKIPPED]"
                else:
                    return {'error': 'safety_filter_blocked', 'content_sample': e.blocked_content}
        else:
            responses = []
            for i,p in enumerate(prompt):
                print(f"{i+1} of {len(prompt)}", end='\r')
                if reformat:
                    query = format_content_for_api(p, api_type)
                else:
                    query = p
                try:
                    responses.append(self.make_one_llm_request(api_type, query, system_prompt, max_tokens))
                except SafetyFilterException as e:
                    self.safety_blocked_count += 1
                    print(f"\n⚠️  SAFETY FILTER BLOCKED CONTENT #{self.safety_blocked_count}")
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