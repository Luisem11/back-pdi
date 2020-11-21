from flask import Flask, jsonify, make_response
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    response = make_response(jsonify(name="API de procesamiento de imágenes de algas", version="1.0"), 200)
    return response
@app.route('/ping')
def pong():
    return 'pong'

if __name__== '__main__':
    app.run(debug=True, port=4000)
