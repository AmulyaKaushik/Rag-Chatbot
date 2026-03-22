# 🤖 RAG Chatbot - Complete Setup Guide

## 📋 Project Overview

A **Retrieval-Augmented Generation (RAG) Chatbot** that:
- ✅ Accepts PDF uploads
- ✅ Extracts and chunks text
- ✅ Creates embeddings using sentence-transformers
- ✅ Stores embeddings in FAISS vector database
- ✅ Uses Ollama for local LLM inference
- ✅ Provides conversational interface via Streamlit

**No external APIs. No paid services. 100% Local.**

---

## 🛠️ SETUP INSTRUCTIONS

### STEP 1: Install Ollama

1. **Download Ollama** from [ollama.ai](https://ollama.ai)
2. **Install** and follow the installation guide
3. **Start Ollama** (it runs as a background service)

### STEP 2: Download LLM Model

**Option A: Use Llama3 (Recommended, ~4.7GB)**
```bash
ollama pull llama3
```

**Option B: Use Phi (Smaller, ~2.6GB - if you have limited storage)**
```bash
ollama pull phi
```

**Option C: Use Mistral (Fast, ~5.6GB)**
```bash
ollama pull mistral
```

After pulling, verify the model is available:
```bash
ollama list
```

### STEP 3: Create Python Virtual Environment

```bash
# Navigate to project directory
cd c:\Users\anura\OneDrive\Desktop\Projects\rag-chatbot

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### STEP 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- **streamlit** - Web UI framework
- **langchain** - LLM orchestration
- **langchain-community** - Ollama integration
- **faiss-cpu** - Vector database
- **sentence-transformers** - Embedding model
- **pypdf** - PDF reading
- **python-dotenv** - Environment variables

---

## 🚀 RUN THE APPLICATION

### Step 1: Ensure Ollama is Running

Check if Ollama is running:
```bash
curl http://localhost:11434/api/tags
```

If not running, start it:
```bash
ollama serve
```

Or on Windows, Ollama runs as a service automatically.

### Step 2: Start the Streamlit App

```bash
# Make sure virtual environment is activated
streamlit run app.py
```

The app will open in your browser at: **http://localhost:8501**

### Step 3: Use the Application

1. **Upload PDF**: Click "Choose a PDF file" and select your document
2. **Process PDF**: Click "🚀 Process PDF" button
3. **Ask Questions**: Type a question and click "🔎 Get Answer"
4. **View Sources**: Expand "📚 Source Chunks" to see relevant document excerpts

---

## 📁 Project Structure

```
rag-chatbot/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── README.md             # This file
├── src/
│   ├── __init__.py       # Package initialization
│   ├── loader.py         # PDF text extraction
│   ├── splitter.py       # Text chunking
│   ├── embeddings.py     # Sentence-transformers wrapper
│   ├── vectorstore.py    # FAISS vector database
│   └── chain.py          # RAG pipeline orchestration
├── data/                 # Store uploaded PDFs (created at runtime)
└── vectorstore/          # FAISS index storage (created at runtime)
```

---

## 🔧 TROUBLESHOOTING

### Issue: "Connection refused to Ollama at http://localhost:11434"
**Solution:**
```bash
# Verify Ollama is running
ollama serve

# In another terminal, test connection
curl http://localhost:11434/api/tags
```

### Issue: "Model 'llama3' not found"
**Solution:**
```bash
# Download the model
ollama pull llama3

# Check available models
ollama list
```

### Issue: "FAISS module not found"
**Solution:**
```bash
# Make sure virtual environment is activated
pip install faiss-cpu

# If it still fails, try:
pip install --upgrade faiss-cpu
```

### Issue: "No module named 'sentence_transformers'"
**Solution:**
```bash
pip install sentence-transformers
```

### Issue: "PDF has no pages" or "No text extracted"
**Solution:**
- Check if PDF is corrupted
- Try a different PDF file
- Ensure PDF is text-based (not scanned image)

### Issue: "Streamlit app is very slow"
**Solution:**
- Reduce `chunk_size` in `src/splitter.py` (default 1000, try 500)
- Use smaller model: `ollama pull phi` instead of `llama3`
- Check available RAM (should have at least 4GB free)

### Issue: "Out of Memory" error
**Solution:**
```bash
# Use a smaller model
ollama pull phi

# Edit in app.py, change:
llm_model="llama3"
# To:
llm_model="phi"
```

---

## ⚙️ CONFIGURATION

### Change LLM Model

Edit `app.py` line 135:
```python
st.session_state.rag_chain = RAGChain(
    vectorstore=st.session_state.vectorstore,
    embedding_model=st.session_state.embedding_model,
    llm_model="llama3"  # Change to: "phi", "mistral", etc.
)
```

### Change Chunk Size

Edit `app.py` line 129:
```python
chunks = split_text(text, chunk_size=1000, overlap=200)
# Increase chunk_size for longer context (e.g., 2000)
# Decrease chunk_size for more precise chunks (e.g., 500)
```

### Change Number of Retrieved Chunks

Edit `app.py` line 163:
```python
result = st.session_state.rag_chain.generate_answer(query, k=5)
# Increase k for more context (e.g., 10)
# Decrease k for faster responses (e.g., 3)
```

---

## 📊 QUICK START CHECKLIST

- [ ] Downloaded and installed Ollama
- [ ] Pulled LLM model (`ollama pull llama3`)
- [ ] Created Python virtual environment
- [ ] Activated virtual environment
- [ ] Installed dependencies (`pip install -r requirements.txt`)
- [ ] Started Ollama (`ollama serve`)
- [ ] Started Streamlit app (`streamlit run app.py`)
- [ ] Uploaded a PDF
- [ ] Clicked "Process PDF"
- [ ] Asked a question

---

## 🎯 EXAMPLE WORKFLOW

1. **Terminal 1 - Start Ollama:**
```bash
ollama serve
# Output: Listening on 127.0.0.1:11434
```

2. **Terminal 2 - Start App:**
```bash
cd c:\Users\anura\OneDrive\Desktop\Projects\rag-chatbot
venv\Scripts\activate
streamlit run app.py
```

3. **Browser:**
- Navigate to http://localhost:8501
- Upload: `research_paper.pdf`
- Click: "🚀 Process PDF"
- Ask: "What are the main conclusions?"
- Get answer in seconds!

---

## 🎓 TECH DETAILS

### Pipeline Flow
```
PDF → Text Extraction → Text Chunking → Embeddings → FAISS Store
                                          ↓
Query → Embedding → FAISS Search → Retrieved Chunks → LLM Prompt → Answer
```

### Key Components

1. **Loader (loader.py)**
   - Extracts text from PDF using pypdf
   - Preserves page information

2. **Splitter (splitter.py)**
   - Uses RecursiveCharacterTextSplitter
   - Default: 1000 char chunks with 200 overlap

3. **Embeddings (embeddings.py)**
   - Uses "all-MiniLM-L6-v2" model (384-dim embeddings)
   - Runs locally, fast inference

4. **Vector Store (vectorstore.py)**
   - FAISS IndexFlatL2 for similarity search
   - Persistent disk storage
   - Standalone, no external DB needed

5. **Chain (chain.py)**
   - Orchestrates RAG pipeline
   - Integrates Ollama LLM
   - Creates context-aware prompts

---

## 📝 PERFORMANCE NOTES

- **PDF Processing**: ~5-10 seconds per 50 pages (depends on text density)
- **Embedding**: ~1 second per 100 chunks
- **Vector Search**: ~100ms
- **LLM Answer**: ~5-30 seconds (depends on model size)

### Optimization Tips

1. Use smaller model for speed: `phi` instead of `llama3`
2. Reduce chunk_size for faster embeddings
3. Increase overlap for better context
4. Use k=3 instead of k=5 for faster retrieval

---

## 🏗️ PRODUCTION CONSIDERATIONS

For production deployment:

1. **Add authentication** (for multi-user setup)
2. **Database persistence** (save vectorstore to cloud)
3. **Error monitoring** (add Sentry or similar)
4. **Rate limiting** (limit API calls)
5. **Caching** (cache embeddings)
6. **Multi-document support** (manage multiple KBs)
7. **Async processing** (handle large PDFs)

---

## 📚 REFERENCES

- [Ollama Documentation](https://ollama.ai)
- [LangChain Documentation](https://python.langchain.com)
- [FAISS GitHub](https://github.com/facebookresearch/faiss)
- [Sentence-Transformers](https://www.sbert.net)
- [Streamlit Documentation](https://docs.streamlit.io)

---

## 🤝 SUPPORT

If you encounter issues:

1. Check the **TROUBLESHOOTING** section above
2. Verify Ollama is running: `curl http://localhost:11434/api/tags`
3. Check Python dependencies: `pip list`
4. Review logs in the Streamlit terminal

---

**Happy building! 🚀**
