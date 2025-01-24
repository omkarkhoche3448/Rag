# RAG Chatbot

A **Retrieval-Augmented Generation (RAG)** chatbot built using **Flask**, **MongoDB**, and **Llama2**, designed for answering questions from uploaded PDF documents.

---

## Setup Instructions

### 1. Install Dependencies
Make sure you have Python installed. Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. Install Ollama and Pull Llama2 Model
Download and set up the **Llama2** model using Ollama:

```bash
ollama pull llama2
```

### 3. Configure Environment Variables
Create a `.env` file in the project directory and define the necessary environment variables (e.g., database URI, secret keys, etc.).

### 4. Run the Application
Start the Flask server by running:

```bash
python run.py
```

---

## API Endpoints

### 1. **Upload PDF File**
Uploads a PDF file to the server for processing.

- **Endpoint**: `/api/upload_pdf`  
- **Method**: `POST`  
- **Body**:  
  - `file` (form-data): The PDF file to upload.  

- **Response**:  
  - Success: `{ "message": "PDF uploaded successfully", "data": ... }`  
  - Failure: `{ "error": "Error message" }`  

---

### 2. **Ask Questions**
Allows users to query the content of the uploaded PDF.

- **Endpoint**: `/api/ask`  
- **Method**: `POST`  
- **Body**:  
  - `question` (string): The question you want to ask.  

- **Response**:  
  - Success: `{ "answer": "Generated response from the chatbot" }`  
  - Failure: `{ "error": "Error message" }`  

---

## Technologies Used
- **Backend**: Flask
- **Database**: MongoDB
- **Model**: Llama2 via Ollama
- **Programming Language**: Python
