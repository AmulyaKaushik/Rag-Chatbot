"""
Embeddings Module
Handles creating embeddings using sentence-transformers
"""

from sentence_transformers import SentenceTransformer
import logging
import numpy as np

logger = logging.getLogger(__name__)


class EmbeddingModel:
    """Wrapper for sentence-transformers embedding model"""
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the embedding model.
        
        Args:
            model_name: Name of the sentence-transformers model
        """
        try:
            logger.info(f"Loading embedding model: {model_name}")
            self.model = SentenceTransformer(model_name)
            self.model_name = model_name
            logger.info(f"Embedding model loaded successfully")
        except Exception as e:
            logger.error(f"Error loading embedding model: {str(e)}")
            raise
    
    def encode(self, texts: list) -> np.ndarray:
        """
        Encode texts into embeddings.
        
        Args:
            texts: List of text strings to encode
            
        Returns:
            np.ndarray: Array of embeddings
        """
        try:
            embeddings = self.model.encode(texts, convert_to_numpy=True)
            logger.info(f"Encoded {len(texts)} texts into embeddings")
            return embeddings
        except Exception as e:
            logger.error(f"Error encoding texts: {str(e)}")
            raise
    
    def encode_single(self, text: str) -> np.ndarray:
        """
        Encode a single text string.
        
        Args:
            text: Text string to encode
            
        Returns:
            np.ndarray: Embedding vector
        """
        try:
            embedding = self.model.encode([text], convert_to_numpy=True)
            return embedding[0]
        except Exception as e:
            logger.error(f"Error encoding single text: {str(e)}")
            raise
