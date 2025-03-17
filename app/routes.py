from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para evitar problemas de conexión

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is running"})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get("message", "")
    return jsonify({"response": f"Has dicho: {message}"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
