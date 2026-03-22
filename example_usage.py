"""
Quick example script showing how to use the RAG chatbot programmatically
(Not just through the Streamlit UI)
"""

import sys
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def example_usage():
    """
    Example of using the RAG chatbot without Streamlit
    """
    
    print("\n" + "="*60)
    print(" RAG Chatbot - Programmatic Usage Example")
    print("="*60)
    
    # Check if test PDF exists
    test_pdf_path = Path("sample.pdf")
    
    if not test_pdf_path.exists():
        print("\n⚠️  sample.pdf not found!")
        print("\nTo run this example:")
        print("1. Download a PDF and save it as 'sample.pdf'")
        print("2. Or modify this script to use your own PDF path\n")
        return
    
    try:
        from src.loader import load_pdf
        from src.splitter import split_text
        from src.embeddings import EmbeddingModel
        from src.vectorstore import FAISSVectorStore
        from src.chain import RAGChain
        
        print("\n📖 Loading PDF...")
        text = load_pdf(str(test_pdf_path))
        print(f"✅ Loaded {len(text)} characters")
        
        print("\n✂️  Splitting text into chunks...")
        chunks = split_text(text, chunk_size=1000, overlap=200)
        print(f"✅ Created {len(chunks)} chunks")
        
        print("\n🧠 Loading embedding model...")
        embedding_model = EmbeddingModel("all-MiniLM-L6-v2")
        print("✅ Model loaded")
        
        print("\n📊 Creating embeddings...")
        embeddings = embedding_model.encode(chunks)
        print(f"✅ Created {len(embeddings)} embeddings")
        
        print("\n💾 Creating vector store...")
        vectorstore = FAISSVectorStore(embeddings_dim=384)
        vectorstore.add_texts(chunks, embeddings)
        print(f"✅ Vector store has {vectorstore.get_size()} vectors")
        
        print("\n🚀 Initializing RAG chain...")
        rag_chain = RAGChain(
            vectorstore=vectorstore,
            embedding_model=embedding_model,
            llm_model="llama3"
        )
        print("✅ RAG chain ready")
        
        # Example questions
        questions = [
            "What is this document about?",
            "What are the main points?",
            "Can you summarize the key findings?"
        ]
        
        print("\n" + "="*60)
        print(" Asking Questions")
        print("="*60)
        
        for i, question in enumerate(questions, 1):
            print(f"\n📝 Question {i}: {question}")
            
            try:
                result = rag_chain.generate_answer(question, k=5)
                
                print(f"\n🤖 Answer:")
                print(result['answer'])
                
                print(f"\n📚 Sources ({len(result['sources'])} chunks):")
                for j, source in enumerate(result['sources'][:2], 1):
                    print(f"\n  Source {j}:")
                    preview = source[:200].replace('\n', ' ')
                    print(f"  {preview}...")
            
            except Exception as e:
                print(f"❌ Error: {str(e)}")
        
        print("\n" + "="*60)
        print(" Example Complete")
        print("="*60 + "\n")
    
    except ImportError as e:
        print(f"❌ Import error: {str(e)}")
        print("\nMake sure all dependencies are installed:")
        print("pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


if __name__ == "__main__":
    example_usage()
