from flask import  Flask, request, jsonify, send_file
from flask_cors import CORS
import io
import cv2
from PIL import Image
import numpy as np
import pytesseract as tess

app = Flask(__name__)
CORS(app, origins="http://localhost:5173")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

@app.route('/')
def default():
    return "Hello World!"

@app.route('/analyze', methods=['POST'])
def analyzeImage():
    """
    #test
    test_raw_img = cv2.imread('test_sheet.jpg', cv2.IMREAD_GRAYSCALE)
    #tresh, binary_img = cv2.threshold(test_raw_img, 127, 255, cv2.THRESH_BINARY)
    binary_img = cv2.adaptiveThreshold(test_raw_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 19, 4)
    success, reencoded_img = cv2.imencode('.jpg', binary_img)
    """
    
    print("Received POST request to /analyze")
    
    #image taken from frontend
    received_image = request.files['image']
    image_data = received_image.read()

    #process/ decode image
    numpy_converted = np.frombuffer(image_data, np.uint8)
    analysis_base = cv2.imdecode(numpy_converted, cv2.IMREAD_GRAYSCALE)
    #tresh, binary_img = cv2.threshold(analysis_base, 127, 255, cv2.THRESH_BINARY) # converts to image to black/ white - might need to look into adaptive thresholding so lighting doesn't matter as much
    
    blurred_img = cv2.GaussianBlur(analysis_base, (5, 5), 0)
    binary_img = cv2.adaptiveThreshold(blurred_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    ocr_img = cv2.cvtColor(binary_img, cv2.COLOR_GRAY2RGB)

    extracted_text = tess.image_to_string(ocr_img)

    success, reencoded_img = cv2.imencode('.jpg', contour_image)

    return jsonify({'extracted_text': extracted_text})
   #return send_file(io.BytesIO(reencoded_img), mimetype='image/jpeg')

    
    

    # min_area = 1000 #for filtering purposes of contours, minimum area
    # max_area = 4000

    # contours, hierarchy = cv2.findContours(binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # answers = []

    # filtered_contours = []
    # for cnt in contours:
    #     if cv2.contourArea(cnt) > min_area and cv2.contourArea(cnt) < max_area:
    #         filtered_contours.append(cnt)

    # # Draw bounding boxes for all filtered contours
    # contour_image = cv2.cvtColor(analysis_base.copy(), cv2.COLOR_GRAY2BGR)
    # for cnt in filtered_contours:
    #     x, y, w, h = cv2.boundingRect(cnt)
    #     cv2.rectangle(contour_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    #returns encoded image - reality don't need this
    




    return send_file(io.BytesIO(reencoded_img), mimetype='image/jpeg')
    #return 'Success!'
