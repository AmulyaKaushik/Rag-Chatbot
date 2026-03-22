"""
Configuration Module
Centralized configuration for the RAG chatbot
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Ollama Configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
LLM_MODEL = os.getenv("LLM_MODEL", "llama3")

# Embedding Configuration
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
EMBEDDING_DIM = 384

# Text Processing Configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Vector Store Configuration
VECTORSTORE_PATH = os.getenv("VECTORSTORE_PATH", "./vectorstore")

# RAG Configuration
RETRIEVAL_K = 5  # Number of chunks to retrieve
LLM_TEMPERATURE = 0.7

# File Storage
DATA_PATH = "./data"
UPLOAD_FOLDER = DATA_PATH

# Logging
LOG_LEVEL = "INFO"

# Streamlit Configuration
STREAMLIT_PAGE_TITLE = "🤖 RAG Chatbot"
STREAMLIT_PAGE_ICON = "🤖"

# Create necessary directories
os.makedirs(DATA_PATH, exist_ok=True)
os.makedirs(VECTORSTORE_PATH, exist_ok=True)
