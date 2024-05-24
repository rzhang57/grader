from flask import  Flask, request, jsonify, send_file
from flask_cors import CORS
import io
from PIL import Image



app = Flask(__name__)
CORS(app, origins="http://localhost:5173")

@app.route('/')
def default():
    return "Hello World!"

@app.route('/analyze', methods=['POST'])
def analyzeImage():
    print("Received POST request to /analyze")
    
    received_image = request.files['image']
    image_data = received_image.read()
    image_stream = io.BytesIO(image_data)
    return send_file(image_stream, mimetype='image/jpeg')
    #return 'Success!'

