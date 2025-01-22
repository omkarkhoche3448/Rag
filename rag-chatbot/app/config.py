import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGODB_URI = os.getenv('MONGODB_URI')
    MONGODB_DB_NAME = os.getenv('MONGODB_DB_NAME', 'ragdb')
    MONGODB_COLLECTION = os.getenv('MONGODB_COLLECTION', 'documents')
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'pdf'}

    def __init__(self):
        if not self.MONGODB_URI:
            raise ValueError("MONGODB_URI is not set in the environment variables.")