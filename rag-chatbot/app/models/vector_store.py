from pymongo import MongoClient
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.embeddings import HuggingFaceEmbeddings
from app.config import Config

class VectorStore:
    def __init__(self):
        self.client = MongoClient(Config.MONGODB_URI)
        self.db = self.client[Config.MONGODB_DB_NAME]
        self.collection = self.db[Config.MONGODB_COLLECTION]
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-mpnet-base-v2"
        )

    def create_vector_store(self, documents):
        return MongoDBAtlasVectorSearch.from_documents(
            documents,
            self.embeddings,
            collection=self.collection
        )

    def get_vector_store(self):
        return MongoDBAtlasVectorSearch(
            self.collection,
            self.embeddings
        )