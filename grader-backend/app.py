from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="http://localhost:5173")

@app.route('/')
def default():
    return "Hello World!"

@app.route('/analyze', methods=['POST'])
def analyzeImage():
    print("Received POST request to /analyze")
    print(request.data)
    return 'Success!'
