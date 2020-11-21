from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    response = app.response_class(
        response=jsonify(name="API de procesamientod de imágenes de algas",version="1.0"),
        status=200,
        mimetype='application/json'
    )
    return response
@app.route('/ping')
def pong():
    return 'pong'

if __name__== '__main__':
    app.run(debug=True, port=4000)
