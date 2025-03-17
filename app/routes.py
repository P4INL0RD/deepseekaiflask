from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from .summarizer import summarize_file
from .model import get_chat_response

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    response = get_chat_response(user_input)
    return jsonify({'response': response})

@app_routes.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join('uploads', filename))
        summary = summarize_file(os.path.join('uploads', filename))
        return jsonify({'summary': summary})
    return jsonify({'error': 'No file uploaded'}), 400