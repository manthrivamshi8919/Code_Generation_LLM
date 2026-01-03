from groq import Groq
from typing import Optional, Dict, Any

class GroqClient:
    """Client for interacting with the Groq API"""
    
    def __init__(self, api_key: str):
        """
        Initialize the Groq client
        
        Args:
            api_key: Your Groq API key
        """
        self.client = Groq(api_key=api_key)
    
    def chat_completion(
        self,
        messages: list,
        model: str = "llama-3.3-70b-versatile",
        max_tokens: int = 4000,
        temperature: float = 0.7,
        **kwargs
    ) -> Any:
        """
        Create a chat completion using Groq API
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            model: Model to use (llama3-70b-8192, llama3-8b-8192, mixtral-8x7b-32768)
            max_tokens: Maximum tokens in response
            temperature: Sampling temperature
            **kwargs: Additional parameters
            
        Returns:
            API response object
        """
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
                **kwargs
            )
            return response
        except Exception as e:
            raise Exception(f"API request failed: {str(e)}")
    
    def generate_code(
        self,
        prompt: str,
        language: str = "Python",
        model: str = "llama-3.3-70b-versatile",
        include_comments: bool = True,
        include_tests: bool = False,
        optimize: bool = False,
        **kwargs
    ) -> str:
        """
        Generate code using Groq API
        
        Args:
            prompt: Code generation prompt
            language: Programming language
            model: Model to use
            include_comments: Whether to include comments
            include_tests: Whether to include unit tests
            optimize: Whether to optimize for performance
            **kwargs: Additional parameters
            
        Returns:
            Generated code as string
        """
        system_prompt = f"""You are a helpful code generation assistant. Generate clean, well-commented, and functional {language} code based on the user's requirements.
        
        Guidelines:
        - Write clean, readable, and maintainable code
        - Follow best practices and conventions for {language}
        - Include proper error handling where applicable
        - Use meaningful variable and function names
        """
        
        if include_comments:
            system_prompt += "- Include detailed comments explaining the code logic\n"
        
        if include_tests:
            system_prompt += "- Include unit tests for the generated code\n"
        
        if optimize:
            system_prompt += "- Optimize the code for performance\n"
        
        system_prompt += "\nProvide only the complete code solution without explanations."
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Generate {language} code for: {prompt}"}
        ]
        
        response = self.chat_completion(
            messages=messages,
            model=model,
            **kwargs
        )
        
        try:
            return response.choices[0].message.content
        except (AttributeError, IndexError):
            raise Exception("Unexpected response format from API")
    
    def get_models(self) -> list:
        """
        Get available models from Groq API
        
        Returns:
            List of available models
        """
        # Groq doesn't have a public models endpoint, so we return the known models
        return [
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant", 
            "llama-4-scout-17b-16e-instruct"
        ]
    
    def validate_api_key(self) -> bool:
        """
        Validate the API key by making a simple request
        
        Returns:
            True if API key is valid, False otherwise
        """
        try:
            # Try a simple completion to validate the API key
            response = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",  # Use smaller model for validation
                messages=[{"role": "user", "content": "Hello"}],
                max_tokens=5
            )
            return True
        except Exception:
            return False
