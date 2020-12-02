# from flask import Flask, jsonify, make_response, request
# import os
# import base64
# import numpy as np
# import cv2 
# from io import StringIO

# app = Flask(__name__)

# @app.route('/')
# def home():
#     response = make_response(jsonify(name="API de procesamiento de imágenes de algas", version="1.0"), 200)
#     return response

# @app.route('/process', methods=['POST'])
# def process():
#     img = readB64(request.json['img'])
#     auximg = img
#     auximg[:,:,1] = 0    
#     auximg[:,:,2] = 0    
#     img = toB64(auximg)
#     response = make_response(jsonify(process_img=img), 200)
#     return response
    
    
# def readB64(base64_string):    
#     im_bytes = base64.b64decode(base64_string)
#     im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
#     return cv2.imdecode(im_arr, flags=cv2.COLOR_RGB2BGR)

# def toB64(img):
#     _, im_arr = cv2.imencode('.jpg', img)  # im_arr: image in Numpy one-dim array format.
#     im_bytes = im_arr.tobytes()
#     im_b64 = base64.b64encode(im_bytes)

# if __name__== '__main__':
#     app.run(debug=True, port=4000)
