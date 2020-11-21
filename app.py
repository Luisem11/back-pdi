from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(response_value_1=1,response_value_2="value")

@app.route('/ping')
def pong():
    return 'pong'

if __name__== '__main__':
    app.run(debug=True, port=4000)
