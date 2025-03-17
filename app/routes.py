from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from .summarizer import summarize_file
from .model import get_chat_response

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return jsonify({'message': 'Chat endpoint is running'}), 200
    
    user_input = request.json.get('input')
    response = get_chat_response(user_input)
    return jsonify({'response': response})

@app_routes.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return jsonify({'message': 'Upload endpoint is running'}), 200

    file = request.files.get('file')
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join('uploads', filename))
        summary = summarize_file(os.path.join('uploads', filename))
        return jsonify({'summary': summary})

    return jsonify({'error': 'No file uploaded'}), 400

if __name__ == '__main__':
    app_routes.run(debug=True, host="0.0.0.0", port=5000)