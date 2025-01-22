# RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot using Flask, MongoDB, and Llama2.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt

2. Install Ollama and pull Llama2:
```bash
ollama pull llama2

3. Set up environment variables in .env

4. Run the application:

```bash
python run.py
API Endpoints

## API Endpoints

POST /api/upload_pdf: Upload PDF file
POST /api/ask: Ask questions about the PDF content