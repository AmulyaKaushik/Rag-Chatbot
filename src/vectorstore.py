"""
Vector Store Module
Handles FAISS vector database operations
"""

import faiss
import numpy as np
import pickle
import os
import logging

logger = logging.getLogger(__name__)


class FAISSVectorStore:
    """FAISS vector database for storing and retrieving embeddings"""
    
    def __init__(self, embeddings_dim: int = 384):
        """
        Initialize FAISS vector store.
        
        Args:
            embeddings_dim: Dimension of embeddings (384 for all-MiniLM-L6-v2)
        """
        self.index = faiss.IndexFlatL2(embeddings_dim)
        self.texts = []
        self.embeddings_dim = embeddings_dim
        logger.info("FAISS vector store initialized")
    
    def add_texts(self, texts: list, embeddings: np.ndarray):
        """
        Add texts and their embeddings to the vector store.
        
        Args:
            texts: List of text chunks
            embeddings: Numpy array of embeddings
        """
        try:
            if len(texts) != len(embeddings):
                raise ValueError("Number of texts and embeddings must match")
            
            # Ensure embeddings are float32
            embeddings = embeddings.astype(np.float32)
            
            self.index.add(embeddings)
            self.texts.extend(texts)
            
            logger.info(f"Added {len(texts)} texts to vector store. Total: {len(self.texts)}")
        except Exception as e:
            logger.error(f"Error adding texts to vector store: {str(e)}")
            raise
    
    def search(self, query_embedding: np.ndarray, k: int = 5) -> list:
        """
        Search for similar texts using query embedding.
        
        Args:
            query_embedding: Embedding vector of the query
            k: Number of results to return
            
        Returns:
            list: List of most similar text chunks
        """
        try:
            query_embedding = np.array([query_embedding], dtype=np.float32)
            distances, indices = self.index.search(query_embedding, k)
            
            results = []
            for idx in indices[0]:
                if idx < len(self.texts):
                    results.append(self.texts[idx])
            
            logger.info(f"Search returned {len(results)} results")
            return results
        except Exception as e:
            logger.error(f"Error searching vector store: {str(e)}")
            raise
    
    def save(self, path: str):
        """
        Save vector store to disk.
        
        Args:
            path: Directory path to save to
        """
        try:
            os.makedirs(path, exist_ok=True)
            
            # Save FAISS index
            faiss.write_index(self.index, os.path.join(path, "faiss_index.bin"))
            
            # Save texts with pickle
            with open(os.path.join(path, "texts.pkl"), "wb") as f:
                pickle.dump(self.texts, f)
            
            logger.info(f"Vector store saved to {path}")
        except Exception as e:
            logger.error(f"Error saving vector store: {str(e)}")
            raise
    
    def load(self, path: str):
        """
        Load vector store from disk.
        
        Args:
            path: Directory path to load from
        """
        try:
            # Load FAISS index
            self.index = faiss.read_index(os.path.join(path, "faiss_index.bin"))
            
            # Load texts
            with open(os.path.join(path, "texts.pkl"), "rb") as f:
                self.texts = pickle.load(f)
            
            logger.info(f"Vector store loaded from {path}")
        except Exception as e:
            logger.error(f"Error loading vector store: {str(e)}")
            raise
    
    def is_empty(self) -> bool:
        """Check if vector store is empty"""
        return self.index.ntotal == 0
    
    def get_size(self) -> int:
        """Get number of vectors in the store"""
        return self.index.ntotal
