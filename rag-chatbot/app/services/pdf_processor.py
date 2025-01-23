from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

class PDFProcessor:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        print("[PDFProcessor] Text splitter configured")


    def process_pdf(self, file_path):
        try:
            loader = PyPDFLoader(file_path)
            print("[PDFProcessor] PDF loader created")
            
            documents = loader.load()
            print(f"[PDFProcessor] Loaded {len(documents)} pages from PDF")
            
            splits = self.text_splitter.split_documents(documents)
            print(f"[PDFProcessor] Created {len(splits)} text chunks")
            
            return splits
        except Exception as e:
            print(f"[PDFProcessor] Error processing PDF: {str(e)}")
            raise
        
