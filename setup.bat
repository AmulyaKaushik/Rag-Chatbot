@echo off
REM Quick Start Script for RAG Chatbot on Windows

echo.
echo ======================================
echo   RAG Chatbot - Quick Start
echo ======================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created.
) else (
    echo Virtual environment already exists.
)

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Checking/Installing dependencies...
pip install -r requirements.txt

echo.
echo ======================================
echo   Setup Complete!
echo ======================================
echo.
echo Next steps:
echo 1. Make sure Ollama is running:
echo    - Open another terminal
echo    - Run: ollama serve
echo.
echo 2. Download a model (if not already done):
echo    - ollama pull llama3
echo.
echo 3. Start the Streamlit app:
echo    - streamlit run app.py
echo.
echo ======================================
echo.
pause
