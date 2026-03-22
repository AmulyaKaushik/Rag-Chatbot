"""
PDF Loader Module
Handles PDF file reading and extraction
"""

from pypdf import PdfReader
import logging

logger = logging.getLogger(__name__)


def load_pdf(pdf_file_path: str) -> str:
    """
    Load and extract text from a PDF file.
    
    Args:
        pdf_file_path: Path to the PDF file
        
    Returns:
        str: Extracted text from the PDF
        
    Raises:
        FileNotFoundError: If PDF file not found
        ValueError: If PDF has no readable content
    """
    try:
        pdf_reader = PdfReader(pdf_file_path)
        
        if len(pdf_reader.pages) == 0:
            raise ValueError("PDF has no pages.")
        
        text = ""
        for page_num, page in enumerate(pdf_reader.pages):
            page_text = page.extract_text()
            if page_text:
                text += f"\n--- Page {page_num + 1} ---\n{page_text}"
        
        if not text.strip():
            raise ValueError("No text could be extracted from the PDF.")
        
        logger.info(f"Successfully loaded PDF with {len(pdf_reader.pages)} pages")
        return text
    
    except FileNotFoundError:
        logger.error(f"PDF file not found: {pdf_file_path}")
        raise FileNotFoundError(f"PDF file not found: {pdf_file_path}")
    except Exception as e:
        logger.error(f"Error loading PDF: {str(e)}")
        raise


def load_pdf_from_bytes(pdf_bytes) -> str:
    """
    Load and extract text from PDF bytes (for Streamlit file uploader).
    
    Args:
        pdf_bytes: PDF file content as bytes
        
    Returns:
        str: Extracted text from the PDF
    """
    try:
        pdf_reader = PdfReader(pdf_bytes)
        
        if len(pdf_reader.pages) == 0:
            raise ValueError("PDF has no pages.")
        
        text = ""
        for page_num, page in enumerate(pdf_reader.pages):
            page_text = page.extract_text()
            if page_text:
                text += f"\n--- Page {page_num + 1} ---\n{page_text}"
        
        if not text.strip():
            raise ValueError("No text could be extracted from the PDF.")
        
        logger.info(f"Successfully loaded PDF with {len(pdf_reader.pages)} pages")
        return text
    
    except Exception as e:
        logger.error(f"Error loading PDF from bytes: {str(e)}")
        raise
