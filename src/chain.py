"""
RAG Chain Module
Handles the complete RAG pipeline with LLM
"""

import logging
from langchain_community.llms import Ollama
from .embeddings import EmbeddingModel
from .vectorstore import FAISSVectorStore

logger = logging.getLogger(__name__)


class RAGChain:
    """Complete RAG pipeline combining retrieval and generation"""
    
    def __init__(
        self,
        vectorstore: FAISSVectorStore,
        embedding_model: EmbeddingModel,
        llm_model: str = "llama3",
        ollama_base_url: str = "http://localhost:11434"
    ):
        """
        Initialize RAG chain.
        
        Args:
            vectorstore: FAISSVectorStore instance
            embedding_model: EmbeddingModel instance
            llm_model: Name of Ollama model to use
            ollama_base_url: Base URL for Ollama API
        """
        self.vectorstore = vectorstore
        self.embedding_model = embedding_model
        self.llm_model = llm_model
        
        try:
            logger.info(f"Initializing Ollama with model: {llm_model}")
            self.llm = Ollama(
                model=llm_model,
                base_url=ollama_base_url,
                temperature=0.7
            )
            logger.info(f"Ollama LLM initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing LLM: {str(e)}")
            raise
    
    def retrieve_context(self, query: str, k: int = 5) -> list:
        """
        Retrieve relevant context from the vector store.
        
        Args:
            query: User question/query
            k: Number of chunks to retrieve
            
        Returns:
            list: List of relevant text chunks
        """
        try:
            # Encode the query
            query_embedding = self.embedding_model.encode_single(query)
            
            # Search vector store
            relevant_chunks = self.vectorstore.search(query_embedding, k=k)
            
            logger.info(f"Retrieved {len(relevant_chunks)} relevant chunks")
            return relevant_chunks
        except Exception as e:
            logger.error(f"Error retrieving context: {str(e)}")
            raise
    
    def _create_prompt(self, query: str, context: list) -> str:
        """
        Create a prompt with context for the LLM.
        
        Args:
            query: User question
            context: List of relevant text chunks
            
        Returns:
            str: Formatted prompt
        """
        context_text = "\n".join(context)
        
        prompt = f"""Based on the following context, answer the question. 
If the answer is not in the context, say "I don't have enough information to answer this question."

Context:
{context_text}

Question: {query}

Answer:"""
        
        return prompt
    
    def generate_answer(self, query: str, k: int = 5) -> dict:
        """
        Generate an answer for the query using RAG.
        
        Args:
            query: User question
            k: Number of chunks to retrieve
            
        Returns:
            dict: Contains 'answer' and 'sources' (the chunks used)
        """
        try:
            # Retrieve relevant chunks
            context = self.retrieve_context(query, k=k)
            
            if not context:
                return {
                    "answer": "No relevant information found in the document.",
                    "sources": []
                }
            
            # Create prompt
            prompt = self._create_prompt(query, context)
            
            # Generate answer using LLM
            logger.info("Generating answer using LLM")
            answer = self.llm.invoke(prompt)
            
            return {
                "answer": answer,
                "sources": context
            }
        
        except Exception as e:
            logger.error(f"Error generating answer: {str(e)}")
            raise
