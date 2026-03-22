"""
Test script to verify RAG chatbot setup
Run this to diagnose any issues before starting the app
"""

import sys
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def test_imports():
    """Test if all required packages are installed"""
    print("\n" + "="*50)
    print("Testing Imports...")
    print("="*50)
    
    packages = {
        'streamlit': 'Streamlit',
        'langchain': 'LangChain',
        'faiss': 'FAISS',
        'sentence_transformers': 'Sentence-Transformers',
        'pypdf': 'PyPDF',
        'dotenv': 'python-dotenv'
    }
    
    failed = []
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"✅ {name}")
        except ImportError:
            print(f"❌ {name} - NOT INSTALLED")
            failed.append(package)
    
    if failed:
        print(f"\n⚠️  Missing packages: {', '.join(failed)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("\n✅ All packages installed!")
    return True


def test_models():
    """Test if models can be loaded"""
    print("\n" + "="*50)
    print("Testing Model Loading...")
    print("="*50)
    
    try:
        from sentence_transformers import SentenceTransformer
        print("Loading embedding model (all-MiniLM-L6-v2)...")
        model = SentenceTransformer("all-MiniLM-L6-v2")
        print("✅ Embedding model loaded successfully")
        
        # Test encoding
        test_text = "This is a test sentence."
        embedding = model.encode([test_text])
        print(f"✅ Embedding shape: {embedding.shape}")
        
    except Exception as e:
        print(f"❌ Error loading embedding model: {str(e)}")
        return False
    
    return True


def test_faiss():
    """Test FAISS functionality"""
    print("\n" + "="*50)
    print("Testing FAISS Vector Store...")
    print("="*50)
    
    try:
        import numpy as np
        import faiss
        
        # Create index
        index = faiss.IndexFlatL2(384)
        
        # Create mock embeddings
        embeddings = np.random.rand(10, 384).astype(np.float32)
        index.add(embeddings)
        
        print(f"✅ FAISS index created with {index.ntotal} vectors")
        
        # Test search
        query = np.random.rand(1, 384).astype(np.float32)
        distances, indices = index.search(query, 5)
        print(f"✅ Search returned {len(indices[0])} results")
        
    except Exception as e:
        print(f"❌ Error with FAISS: {str(e)}")
        return False
    
    return True


def test_ollama():
    """Test Ollama connectivity"""
    print("\n" + "="*50)
    print("Testing Ollama Connection...")
    print("="*50)
    
    try:
        import requests
        
        url = "http://localhost:11434/api/tags"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            models = response.json().get('models', [])
            print(f"✅ Ollama is running!")
            print(f"Available models: {len(models)}")
            
            model_names = [m.get('name', 'unknown') for m in models]
            for model in model_names[:5]:  # Show first 5
                print(f"  - {model}")
            
            # Check for llama3 or alternative
            has_llama3 = any('llama3' in m.lower() for m in model_names)
            has_phi = any('phi' in m.lower() for m in model_names)
            
            if has_llama3:
                print("\n✅ llama3 model found - Recommended!")
                return True
            elif has_phi:
                print("\n⚠️  phi model found (lighter weight - will work)")
                print("   To use llama3 instead: ollama pull llama3")
                return True
            else:
                print("\n❌ No LLM models found!")
                print("   Download a model:")
                print("   - ollama pull llama3 (recommended)")
                print("   - ollama pull phi (lighter)")
                print("   - ollama pull mistral")
                return False
        else:
            print(f"❌ Ollama API error: {response.status_code}")
            return False
    
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Ollama at http://localhost:11434")
        print("\n   Ollama is not running!")
        print("\n   To start Ollama:")
        print("   1. Open a terminal")
        print("   2. Run: ollama serve")
        print("   3. Keep it running in the background")
        return False
    except Exception as e:
        print(f"❌ Error connecting to Ollama: {str(e)}")
        return False


def test_langchain_ollama():
    """Test LangChain Ollama integration"""
    print("\n" + "="*50)
    print("Testing LangChain + Ollama Integration...")
    print("="*50)
    
    try:
        from langchain_community.llms import Ollama
        
        print("Initializing Ollama LLM...")
        llm = Ollama(model="llama3", base_url="http://localhost:11434")
        
        print("Testing simple prompt...")
        response = llm.invoke("Say 'RAG chatbot works!' in exactly 3 words.")
        
        print(f"✅ LLM Response: {response}")
        return True
    
    except Exception as e:
        print(f"❌ Error with LangChain Ollama: {str(e)}")
        print("\n   Make sure Ollama is running and model exists")
        return False


def main():
    """Run all tests"""
    print("\n")
    print("╔" + "="*48 + "╗")
    print("║" + " "*10 + "RAG Chatbot Setup Verification" + " "*8 + "║")
    print("╚" + "="*48 + "╝")
    
    results = {
        "Imports": test_imports(),
        "Models": test_models(),
        "FAISS": test_faiss(),
        "Ollama": test_ollama(),
    }
    
    # Only test LangChain integration if Ollama is available
    if results["Ollama"]:
        results["LangChain+Ollama"] = test_langchain_ollama()
    
    # Summary
    print("\n" + "="*50)
    print("Summary")
    print("="*50)
    
    all_passed = all(results.values())
    
    for test_name, passed in results.items():
        status = "✅" if passed else "❌"
        print(f"{status} {test_name}")
    
    if all_passed:
        print("\n" + "🎉 "*20)
        print("\n✅ All tests passed! You're ready to run the app:")
        print("\n   streamlit run app.py\n")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
