"""Ollama AI Provider Implementation"""

import aiohttp
from typing import List
import logging
from .base import AIProvider

logger = logging.getLogger(__name__)


class OllamaProvider(AIProvider):
    """Provider for Ollama (Local LLM)"""
    
    async def initialize(self) -> None:
        """Initialize Ollama connection"""
        self.base_url = self.config.get('base_url', 'http://localhost:11434')
        self.model = self.config.get('model', 'llama2')
        logger.info(f"Initialized Ollama provider with model: {self.model}")
    
    async def generate_response(self, prompt: str, **kwargs) -> str:
        """Generate response using Ollama"""
        try:
            async with aiohttp.ClientSession() as session:
                url = f"{self.base_url}/api/generate"
                payload = {
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                }
                
                async with session.post(url, json=payload) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        return data.get('response', 'No response')
                    else:
                        raise Exception(f"Ollama error: {resp.status}")
        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            raise
    
    async def list_models(self) -> List[str]:
        """List available models in Ollama"""
        try:
            async with aiohttp.ClientSession() as session:
                url = f"{self.base_url}/api/tags"
                async with session.get(url) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        return [model['name'] for model in data.get('models', [])]
                    return []
        except Exception as e:
            logger.error(f"Error listing models: {str(e)}")
            return []
    
    async def health_check(self) -> bool:
        """Check Ollama service health"""
        try:
            async with aiohttp.ClientSession() as session:
                url = f"{self.base_url}/api/tags"
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as resp:
                    return resp.status == 200
        except Exception as e:
            logger.error(f"Health check failed: {str(e)}")
            return False
