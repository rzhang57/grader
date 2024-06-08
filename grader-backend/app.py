from flask import  Flask, request, jsonify, send_file
from flask_cors import CORS
import io
import cv2
from PIL import Image
import numpy as np



app = Flask(__name__)
CORS(app, origins="http://localhost:5173")

@app.route('/')
def default():
    return "Hello World!"

@app.route('/analyze', methods=['POST'])
def analyzeImage():
    print("Received POST request to /analyze")

    """
    
    #image taken from frontend
    received_image = request.files['image']
    image_data = received_image.read()
    #process/ decode image
    numpy_converted = np.frombuffer(image_data, np.uint8)
    analysis_base = cv2.imdecode(numpy_converted, cv2.IMREAD_GRAYSCALE)
    #tresh, binary_img = cv2.threshold(analysis_base, 127, 255, cv2.THRESH_BINARY) # converts to image to black/ white - might need to look into adaptive thresholding so lighting doesn't matter as much
    binary_img = cv2.adaptiveThreshold(analysis_base, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 19, 4)
    success, reencoded_img = cv2.imencode('.jpg', binary_img)

    if not success:
        return "Encoding image failed", 500
        """


    #test
    test_raw_img = cv2.imread('test_sheet.jpg', cv2.IMREAD_GRAYSCALE)
    #tresh, binary_img = cv2.threshold(test_raw_img, 127, 255, cv2.THRESH_BINARY)
    binary_img = cv2.adaptiveThreshold(test_raw_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 19, 4)
    success, reencoded_img = cv2.imencode('.jpg', binary_img)


    return send_file(io.BytesIO(reencoded_img), mimetype='image/jpeg')
    #return 'Success!'
