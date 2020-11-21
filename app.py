from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>API para generar rutas temáticas</h1>'

@app.route('/ping')
def pong():
    return 'pong'

if __name__== '__main__':
    app.run(debug=True, port=4000)
