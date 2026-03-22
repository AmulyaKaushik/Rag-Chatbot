# 🚀 COMPLETE COMMAND GUIDE - RAG Chatbot

## 📋 Quick Command Reference

### On Windows:

#### 1. First Time Setup (Run ONCE)
```bash
# Navigate to project folder
cd c:\Users\anura\OneDrive\Desktop\Projects\rag-chatbot

# Run the setup script (creates venv + installs deps)
setup.bat
```

#### 2. Every Time You Want to Run the App

**Terminal 1 - Start Ollama (Keep Running)**
```bash
ollama serve
```

**Terminal 2 - Start the App**
```bash
cd c:\Users\anura\OneDrive\Desktop\Projects\rag-chatbot
venv\Scripts\activate
streamlit run app.py
```

---

## 📦 OLLAMA MODELS

### Download Model (Choose ONE)

#### Option A: Llama3 (RECOMMENDED - 4.7GB, best quality)
```bash
ollama pull llama3
```
- **Pros**: Best answers, powerful, good for complex questions
- **Cons**: Slower, needs ~8GB RAM
- **Performance**: 5-30 sec per answer

#### Option B: Phi (2.6GB, lightweight)
```bash
ollama pull phi
```
- **Pros**: Fast, small, good for limited RAM
- **Cons**: Less capable, shorter context
- **Performance**: 2-10 sec per answer

#### Option C: Mistral (5.6GB, fast & capable)
```bash
ollama pull mistral
```
- **Pros**: Good balance, fairly fast, capable
- **Cons**: Medium size
- **Performance**: 3-15 sec per answer

#### Option D: Neural-Chat (3.1GB)
```bash
ollama pull neural-chat
```
- **Pros**: Optimized for chat, fast
- **Cons**: Smaller model

### Check Downloaded Models
```bash
ollama list
```

### Delete a Model (if running out of space)
```bash
ollama rm llama3
```

---

## 🔧 STEP-BY-STEP SETUP (Detailed)

### Step 1: Download Ollama
```bash
# Download from: https://ollama.ai
# Install and follow instructions
# Windows: Installer is available
# macOS: brew install ollama
# Linux: Download from website
```

### Step 2: Download an LLM
```bash
# Open command prompt/terminal
ollama pull llama3

# Wait for download to complete (might take 5-10 min depending on internet)
# You'll see progress like: ████████████████░░░░ 75%
```

### Step 3: Create Python Virtual Environment
```bash
# Create venv
python -m venv venv

# Activate venv (Windows)
venv\Scripts\activate

# Activate venv (macOS/Linux)
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Start Ollama Service
```bash
# In a dedicated terminal (keep it running)
ollama serve

# You should see:
# Listening on 127.0.0.1:11434
```

### Step 6: Run the App
```bash
# In another terminal (with venv activated)
streamlit run app.py

# Browser opens automatically to:
# http://localhost:8501
```

---

## 🔍 DIAGNOSTICS & TESTING

### Check if Ollama is Running
```bash
curl http://localhost:11434/api/tags
```

### Check Available Models
```bash
ollama list
```

### Test LLM Response
```bash
# Direct Ollama test
ollama run llama3 "Say hello"
```

### Run Setup Verification Test
```bash
python test_setup.py
```

This tests:
- ✅ All Python packages installed
- ✅ Embedding model loads
- ✅ FAISS works
- ✅ Ollama connectivity
- ✅ LangChain integration

### Check Python Version
```bash
python --version
# Should be 3.8 or higher
```

### Check Virtual Environment
```bash
# Windows
where python
# Should show: venv\Scripts\python.exe

# macOS/Linux
which python
# Should show: /path/venv/bin/python
```

---

## 📊 RESOURCE REQUIREMENTS

| Model | Size | RAM | Speed | Quality |
|-------|------|-----|-------|---------|
| phi | 2.6GB | 4GB | ⚡⚡⚡ Fast | ⭐⭐ Fair |
| mistral | 5.6GB | 6GB | ⚡⚡ Medium | ⭐⭐⭐⭐ Good |
| llama3 | 4.7GB | 8GB | ⚡ Slow | ⭐⭐⭐⭐⭐ Best |

---

## ⚡ PERFORMANCE TUNING

### Make it Faster

Edit `app.py` line 129:
```python
# Change from:
chunks = split_text(text, chunk_size=1000, overlap=200)

# To:
chunks = split_text(text, chunk_size=500, overlap=100)
```

Also edit `app.py` line 163:
```python
# Change from:
result = st.session_state.rag_chain.generate_answer(query, k=5)

# To:
result = st.session_state.rag_chain.generate_answer(query, k=3)
```

Use faster model:
```python
# Change from:
llm_model="llama3"

# To:
llm_model="phi"
```

### Make it Better Quality

Use slower model:
```python
llm_model="llama3"  # Best quality
```

Increase retrieved chunks:
```python
# Change from:
result = st.session_state.rag_chain.generate_answer(query, k=5)

# To:
result = st.session_state.rag_chain.generate_answer(query, k=10)
```

Increase chunk size:
```python
# Change from:
chunks = split_text(text, chunk_size=1000, overlap=200)

# To:
chunks = split_text(text, chunk_size=1500, overlap=300)
```

---

## 🛠️ TROUBLESHOOTING COMMANDS

### Problem: Ollama not found
```bash
# Verify Ollama is in PATH
ollama --version

# If not, add to PATH or use full path
"C:\Users\YourName\AppData\Local\Programs\Ollama\ollama.exe" serve
```

### Problem: Model download failed
```bash
# Try downloading again
ollama pull llama3

# Check disk space
# Make sure you have enough free disk space
```

### Problem: Python dependency error
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Then reinstall requirements
pip install --upgrade -r requirements.txt
```

### Problem: Streamlit not found
```bash
# Verify venv is activated
# On Windows: venv\Scripts\activate should show (venv) in terminal

# If still missing:
pip install streamlit==1.28.1
```

### Problem: Import errors
```bash
# Make sure venv is activated
venv\Scripts\activate

# Verify you're in the right directory
cd c:\Users\anura\OneDrive\Desktop\Projects\rag-chatbot

# Then run
python -c "import streamlit; print('OK')"
```

---

## 🎯 COMMON WORKFLOWS

### Workflow 1: Basic Usage
```bash
# Terminal 1
ollama serve

# Terminal 2
cd c:\Users\anura\OneDrive\Desktop\Projects\rag-chatbot
venv\Scripts\activate
streamlit run app.py

# Browser: Upload PDF → Process → Ask question
```

### Workflow 2: Use Different Model
```bash
# Terminal 1
ollama pull phi
ollama serve

# Terminal 2
# Edit app.py line 135: change llm_model="llama3" to llm_model="phi"
streamlit run app.py
```

### Workflow 3: Test without Streamlit
```bash
# Terminal
cd c:\Users\anura\OneDrive\Desktop\Projects\rag-chatbot
venv\Scripts\activate

# Verify setup
python test_setup.py

# Run example
python example_usage.py  # (requires sample.pdf)
```

---

## 💾 SAVING & LOADING VECTORSTORE

The vectorstore is automatically saved to `./vectorstore/` folder:
- `faiss_index.bin` - The vector index
- `texts.pkl` - The text chunks

To reset the vectorstore:
```bash
# Delete the vectorstore folder
rmdir /s /q vectorstore

# Or manually delete:
# Windows Explorer → rag-chatbot → vectorstore → Delete
```

The app will recreate it when you process a new PDF.

---

## 🔐 SECURITY NOTE

This chatbot runs 100% locally. No data is sent to any cloud service.
- PDFs stay on your machine
- Embeddings stay on your machine
- LLM runs locally
- No internet connection required (after downloading models)

---

## 📈 NEXT STEPS AFTER SETUP

1. **Test with sample PDF**: Use a simple, short PDF first (5-10 pages)
2. **Try different questions**: See how the RAG pipeline works
3. **Experiment with models**: Try phi vs llama3 to see difference
4. **Tune parameters**: Change chunk_size and k to optimize
5. **Production deployment**: See README.md for enterprise considerations

---

## 🆘 LAST RESORT TROUBLESHOOTING

If nothing works:

```bash
# Nuclear option: Restart everything
# 1. Close all terminals and Streamlit
# 2. Kill Ollama:
taskkill /IM ollama.exe /F

# 3. Delete virtual environment
rmdir /s /q venv

# 4. Start fresh
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# 5. Download model again
ollama pull llama3

# 6. Start Ollama
ollama serve

# 7. In another terminal:
streamlit run app.py
```

---

**Still stuck? Check the README.md for more detailed explanations!** 📚
