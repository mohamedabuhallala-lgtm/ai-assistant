"""Main FastAPI Application Entry Point"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=os.getenv('LOG_LEVEL', 'INFO'),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="AI Assistant API",
    description="API for AI Assistant Web Platform",
    version="1.0.0"
)

# CORS Middleware
CORS_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Trusted Host Middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost", "127.0.0.1"]
)


@app.get("/")
async def read_root():
    """Root endpoint"""
    return {
        "message": "Welcome to AI Assistant API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/api/v1/models")
async def get_available_models():
    """Get list of available AI models"""
    return {
        "models": [
            {"id": "ollama", "name": "Ollama (Local)", "status": "available"},
            {"id": "huggingface", "name": "Hugging Face", "status": "available"},
            {"id": "openai", "name": "OpenAI Compatible", "status": "available"}
        ]
    }


@app.post("/api/v1/chat")
async def chat(message: dict):
    """Chat endpoint for sending messages to AI"""
    return {
        "response": "This is a placeholder response. Implement AI logic.",
        "model_used": "placeholder"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True
    )
