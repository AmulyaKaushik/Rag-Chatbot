# ▶️ START HERE - COMPLETE SETUP WALKTHROUGH

## 🎯 YOU HAVE A COMPLETE RAG CHATBOT PROJECT!

Everything is built and ready. Follow these exact steps to get it running.

---

## 📋 CHECKLIST BEFORE YOU START

- [ ] Windows 10 or 11
- [ ] Python 3.8+ installed (check: `python --version`)
- [ ] At least 4GB free RAM (8GB recommended)
- [ ] At least 5GB free disk space
- [ ] Stable internet connection (for initial setup only)

---

## 🚀 SETUP IN 5 MINUTES

### STEP 1: Download Ollama (5 minutes)

1. **Go to**: https://ollama.ai
2. **Download**: Windows installer
3. **Install**: Follow the installation steps
4. **Verify**: Open Command Prompt and run:
```bash
ollama --version
```

✅ **Done when you see version number**

---

### STEP 2: Download an LLM Model (10-15 minutes)

**Open Command Prompt and run:**

```bash
ollama pull llama3
```

**What you'll see:**
```
pulling manifest
pulling 1...
pulling 2...
```

✅ **Done when you see 100%**

**Check it worked:**
```bash
ollama list
```

Should show: `llama3:latest`

---

### STEP 3: Create Virtual Environment (1 minute)

```bash
cd c:\Users\anura\OneDrive\Desktop\Projects\rag-chatbot

python -m venv venv

venv\Scripts\activate
```

✅ **Done when you see `(venv)` at the start of your command line**

---

### STEP 4: Install Dependencies (2-3 minutes)

```bash
pip install -r requirements.txt
```

✅ **Done when installation completes without errors**

---

### STEP 5: Start the App (2 minutes)

**Open TWO command prompts:**

**Prompt 1 - Start Ollama (KEEP THIS RUNNING):**
```bash
ollama serve
```

You should see:
```
Listening on 127.0.0.1:11434
```

**Prompt 2 - Start the App:**
```bash
cd c:\Users\anura\OneDrive\Desktop\Projects\rag-chatbot
venv\Scripts\activate
streamlit run app.py
```

✅ **Done when browser opens to http://localhost:8501**

---

## 💻 NOW YOU'RE READY!

### The Web Interface Will Show:

**Left Side:**
- 📄 PDF Upload box
- 🚀 "Process PDF" button

**Right Side:**
- 💬 Question input field
- 🔎 "Get Answer" button

---

## 🧪 TEST THE APP

1. **Find a PDF** (any document works - a research paper, manual, etc.)
2. **Click** "Choose a PDF file" on the left
3. **Click** "🚀 Process PDF" button
4. **Wait** for processing (you'll see status messages)
5. **Type a question** on the right (e.g., "What is this document about?")
6. **Click** "🔎 Get Answer"
7. **Get an answer** based on your PDF!

---

## 🔄 EVERY TIME YOU RUN IT

After the initial setup, you only need to do:

```bash
# Prompt 1
ollama serve

# Prompt 2
cd c:\Users\anura\OneDrive\Desktop\Projects\rag-chatbot
venv\Scripts\activate
streamlit run app.py
```

---

## ✅ VERIFY IT'S WORKING

Run this diagnostic before starting:

```bash
cd c:\Users\anura\OneDrive\Desktop\Projects\rag-chatbot
venv\Scripts\activate
python test_setup.py
```

**Good output looks like:**
```
✅ Streamlit
✅ LangChain
✅ FAISS
✅ Sentence-Transformers
✅ PyPDF
✅ all-MiniLM-L6-v2
✅ FAISS Vector Store
✅ Ollama is running!
✅ llama3 model found
✅ LLM Response: RAG chatbot works!

🎉 All tests passed!
```

---

## 🆘 TROUBLESHOOTING

### Problem: "Connection refused" or "Cannot connect to Ollama"

**Solution:** Ollama is not running. Open a command prompt and type:
```bash
ollama serve
```

Keep this window open while using the app.

---

### Problem: "Model 'llama3' not found"

**Solution:** Download the model:
```bash
ollama pull llama3
```

Wait for it to complete (5-10 minutes).

---

### Problem: "venv not activated" or "ImportError"

**Solution:** Make sure you're in the right directory and venv is activated:
```bash
cd c:\Users\anura\OneDrive\Desktop\Projects\rag-chatbot
venv\Scripts\activate
```

The terminal should show `(venv)` at the start.

---

### Problem: "pip install failed"

**Solution:** Upgrade pip and try again:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

### Problem: "App is very slow"

**Solution:** Use a faster model. Edit `app.py` and change line 135:

From:
```python
llm_model="llama3"
```

To:
```python
llm_model="phi"
```

Then download the model:
```bash
ollama pull phi
```

---

### Problem: "Out of Memory" error

**Solution 1:** Use a smaller model (see "App is very slow" above)

**Solution 2:** Reduce chunk retrieval. Edit `app.py` line 163:
From:
```python
result = st.session_state.rag_chain.generate_answer(query, k=5)
```
To:
```python
result = st.session_state.rag_chain.generate_answer(query, k=3)
```

---

## 📚 DETAILED DOCUMENTATION

After you get it running, read these files:

1. **SUMMARY.md** - Project overview and features
2. **README.md** - Comprehensive guide with examples
3. **COMMANDS.md** - All commands reference
4. **EXAMPLE_USAGE.py** - Programmatic usage examples

---

## 🎯 WHAT YOU GET

✅ **Complete RAG chatbot** with:
- PDF upload and processing
- Vector embeddings (sentence-transformers)
- Vector database (FAISS)
- Local LLM (Ollama)
- Web interface (Streamlit)

✅ **100% Local** - No cloud services, no API keys

✅ **Production-ready code** with:
- Error handling
- Logging
- Modular design
- Configuration management

✅ **Easy to customize** - Change models, parameters, UI

---

## 🚀 QUICK COMMANDS REFERENCE

```bash
# Setup (one time)
cd c:\Users\anura\OneDrive\Desktop\Projects\rag-chatbot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
ollama pull llama3

# Every time you want to use it
# Terminal 1:
ollama serve

# Terminal 2:
cd c:\Users\anura\OneDrive\Desktop\Projects\rag-chatbot
venv\Scripts\activate
streamlit run app.py

# Verify setup works
python test_setup.py

# Change to faster model
ollama pull phi
# Then edit app.py line 135: llm_model="phi"
```

---

## ✨ YOU'RE READY!

Everything is set up. Just follow the **5 STEPS** above and you'll have a working RAG chatbot!

**Start with:** `ollama serve` in one terminal, then `streamlit run app.py` in another.

Enjoy! 🎉

---

**Need more details?** Check README.md or COMMANDS.md files in the project folder.
