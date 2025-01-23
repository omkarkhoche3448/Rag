from pymongo import MongoClient
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.embeddings import HuggingFaceEmbeddings
from app.config import Config

class VectorStore:
    def __init__(self):
        self.client = MongoClient(Config.MONGODB_URI)
        self.db = self.client[Config.MONGODB_DB_NAME]
        self.collection = self.db[Config.MONGODB_COLLECTION]
        print("[VectorStore] MongoDB connection established")
        
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-mpnet-base-v2"
        )
        print("[VectorStore] Embeddings model loaded")

    def create_vector_store(self, documents):
        print(f"[VectorStore] Creating vector store with {len(documents)} documents")
        try:
            vector_store = MongoDBAtlasVectorSearch.from_documents(
                documents,
                self.embeddings,
                collection=self.collection
            )
            print("[VectorStore] Vector store created successfully")
            return vector_store
        except Exception as e:
            print(f"[VectorStore] Error creating vector store: {str(e)}")
            raise

    def get_vector_store(self):
        try:
            vector_store = MongoDBAtlasVectorSearch(
                self.collection,
                self.embeddings
            )
            print("[VectorStore] Vector store retrieved successfully")
            return vector_store
        except Exception as e:
            print(f"[VectorStore] Error retrieving vector store: {str(e)}")
            raise