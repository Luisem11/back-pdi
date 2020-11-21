from flask import Flask, jsonify, make_response, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    response = make_response(jsonify(name="API de procesamiento de imágenes de algas", version="1.0"), 200)
    return response

@app.route('/process', methods=['POST'])
def process():
    img =  request.json['img']
    response = make_response(jsonify(process_img=img), 200)
    return response
    
    
def readb64(base64_string):
    sbuf = StringIO()
    sbuf.write(base64.b64decode(base64_string))
    pimg = Image.open(sbuf)
    return cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

if __name__== '__main__':
    app.run(debug=True, port=4000)
