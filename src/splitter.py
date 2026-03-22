"""
Text Splitter Module
Handles splitting text into manageable chunks
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter
import logging

logger = logging.getLogger(__name__)


def split_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> list:
    """
    Split text into chunks with overlap for better context.
    
    Args:
        text: Raw text to split
        chunk_size: Size of each chunk in characters
        overlap: Number of overlapping characters between chunks
        
    Returns:
        list: List of text chunks
    """
    try:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap,
            separators=["\n\n", "\n", " ", ""]
        )
        
        chunks = splitter.split_text(text)
        logger.info(f"Split text into {len(chunks)} chunks")
        
        return chunks
    
    except Exception as e:
        logger.error(f"Error splitting text: {str(e)}")
        raise
