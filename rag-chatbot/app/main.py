from flask import Flask, jsonify
from app.api.routes import api
from app.config import Config
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Ensure upload folder exists
    os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)

    # Register blueprints
    app.register_blueprint(api, url_prefix='/api')

    @app.route('/')
    def root():
        return jsonify({
            'message': 'Welcome to RAG Chatbot',
            'api_prefix': '/api'
        })

    return app