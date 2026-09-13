"""Base AI Provider Interface"""

from abc import ABC, abstractmethod
from typing import Optional, List


class AIProvider(ABC):
    """Abstract base class for AI providers"""
    
    def __init__(self, config: dict):
        self.config = config
    
    @abstractmethod
    async def initialize(self) -> None:
        """Initialize the provider"""
        pass
    
    @abstractmethod
    async def generate_response(self, prompt: str, **kwargs) -> str:
        """Generate response from the AI model"""
        pass
    
    @abstractmethod
    async def list_models(self) -> List[str]:
        """List available models"""
        pass
    
    @abstractmethod
    async def health_check(self) -> bool:
        """Check if provider is healthy"""
        pass
