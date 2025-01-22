from flask import Blueprint, request, jsonify
from app.services.pdf_processor import PDFProcessor
from app.services.qa_chain import QAChain
from app.models.vector_store import VectorStore
from app.api.utils import allowed_file, save_file
import os

api = Blueprint('api', __name__)
vector_store = VectorStore()
pdf_processor = PDFProcessor()

@api.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type'}), 400

    try:
        file_path = save_file(file)
        documents = pdf_processor.process_pdf(file_path)
        vector_store.create_vector_store(documents)
        os.remove(file_path)  # Clean up uploaded file
        return jsonify({'message': 'PDF processed successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    if not data or 'question' not in data:
        return jsonify({'error': 'No question provided'}), 400

    try:
        vs = vector_store.get_vector_store()
        qa_chain = QAChain(vs)
        answer = qa_chain.get_answer(data['question'])
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500