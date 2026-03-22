"""
RAG Chatbot Streamlit Application
Complete web interface for the RAG chatbot
"""

import streamlit as st
import os
import tempfile
import logging
from pathlib import Path

from src.loader import load_pdf_from_bytes
from src.splitter import split_text
from src.embeddings import EmbeddingModel
from src.vectorstore import FAISSVectorStore
from src.chain import RAGChain

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🤖 RAG Chatbot")
st.markdown("Upload a PDF and ask questions about its content!")


# Initialize session state
if 'initialized' not in st.session_state:
    st.session_state.vectorstore = None
    st.session_state.embedding_model = None
    st.session_state.rag_chain = None
    st.session_state.initialized = False
    st.session_state.pdf_processed = False
    st.session_state.chat_history = []


def initialize_models():
    """Initialize embedding model and other components"""
    if not st.session_state.initialized:
        with st.spinner("Loading embedding model..."):
            try:
                st.session_state.embedding_model = EmbeddingModel("all-MiniLM-L6-v2")
                st.session_state.vectorstore = FAISSVectorStore(embeddings_dim=384)
                st.session_state.initialized = True
                logger.info("Models initialized successfully")
            except Exception as e:
                st.error(f"Error initializing models: {str(e)}")
                logger.error(f"Initialization error: {str(e)}")
                raise


def process_pdf(uploaded_file) -> bool:
    """
    Process uploaded PDF file and populate vector store.
    
    Args:
        uploaded_file: Streamlit uploaded file
        
    Returns:
        bool: True if processing successful
    """
    try:
        # Load PDF
        with st.spinner("📖 Loading PDF..."):
            text = load_pdf_from_bytes(uploaded_file)
            st.success(f"✅ PDF loaded successfully ({len(text)} characters)")
        
        # Split text
        with st.spinner("✂️ Splitting text into chunks..."):
            chunks = split_text(text, chunk_size=1000, overlap=200)
            st.info(f"📊 Created {len(chunks)} chunks")
        
        # Create embeddings
        with st.spinner("🧠 Creating embeddings..."):
            embeddings = st.session_state.embedding_model.encode(chunks)
            st.success(f"✅ Embeddings created successfully")
        
        # Add to vector store
        with st.spinner("💾 Adding to vector store..."):
            st.session_state.vectorstore.add_texts(chunks, embeddings)
            st.success(f"✅ Vector store populated with {st.session_state.vectorstore.get_size()} vectors")
        
        # Initialize RAG chain
        with st.spinner("🚀 Initializing RAG chain..."):
            st.session_state.rag_chain = RAGChain(
                vectorstore=st.session_state.vectorstore,
                embedding_model=st.session_state.embedding_model,
                llm_model="llama3"
            )
            st.success("✅ RAG chain ready!")
        
        st.session_state.pdf_processed = True
        return True
    
    except Exception as e:
        st.error(f"❌ Error processing PDF: {str(e)}")
        logger.error(f"PDF processing error: {str(e)}")
        return False


def answer_question(query: str) -> dict:
    """
    Answer a question using RAG.
    
    Args:
        query: User's question
        
    Returns:
        dict: Answer and sources
    """
    try:
        with st.spinner("🔍 Searching and generating answer..."):
            result = st.session_state.rag_chain.generate_answer(query, k=5)
            return result
    except Exception as e:
        st.error(f"❌ Error generating answer: {str(e)}")
        logger.error(f"Answer generation error: {str(e)}")
        return None


# Main app layout
col1, col2 = st.columns(2)

# Left column: PDF Upload
with col1:
    st.header("📄 PDF Upload")
    st.divider()
    
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type="pdf",
        help="Upload a PDF document to create a knowledge base"
    )
    
    if uploaded_file is not None:
        st.info(f"Selected file: **{uploaded_file.name}** ({uploaded_file.size / 1024:.1f} KB)")
        
        if st.button("🚀 Process PDF", use_container_width=True, type="primary"):
            initialize_models()
            process_pdf(uploaded_file)


# Right column: Chat Interface
with col2:
    st.header("💬 Ask Questions")
    st.divider()
    
    if not st.session_state.pdf_processed:
        st.warning("⚠️ Please upload and process a PDF first to ask questions.")
    else:
        st.success(f"✅ Document processed! Vector store has {st.session_state.vectorstore.get_size()} embeddings")
        
        # Question input
        question = st.text_input(
            "Ask a question about the document:",
            placeholder="What is this document about?",
            help="Enter your question here"
        )
        
        if st.button("🔎 Get Answer", use_container_width=True, type="primary"):
            if not question.strip():
                st.error("Please enter a question.")
            else:
                result = answer_question(question)
                
                if result:
                    st.markdown("### 📝 Answer")
                    st.markdown(result['answer'])
                    
                    with st.expander("📚 Source Chunks"):
                        for i, source in enumerate(result['sources'], 1):
                            st.markdown(f"**Source {i}:**")
                            st.text(source[:500] + "..." if len(source) > 500 else source)
                            st.divider()


# Footer
st.divider()
st.markdown("""
---
**How it works:**
1. 📄 Upload a PDF document
2. 🔄 Click "Process PDF" to extract text and create embeddings
3. 💬 Ask questions about the document
4. 🤖 Get answers based on the document content

**Tech Stack:** Streamlit • LangChain • FAISS • Sentence-Transformers • Ollama
""")
