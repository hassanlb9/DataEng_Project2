import unittest
import pickle
import numpy as np
import torch
import transformers
import json
from detoxify import Detoxify
from flask import Flask, request, jsonify, current_app
from flask_cors import CORS

app = Flask(__name__)
model=Detoxify('original')
@app.route('/post_text', methods=['GET', 'POST'])
def testPost():
    if request.method == 'POST':
       var = request.json.get('name')
       global v0
       v0=model.predict(var)
       print(model.predict(var))
       print(var)
    return json.dumps(str(v0))
    
# because backend and frontend use different ports, we have to enable cross-origin requests

@app.route('/get_text', methods=['GET', 'POST'])
def testPost1():
    
   var1 = testPost()
   
   return var1

cors = CORS(app, resources={'/*':{'origins': 'http://localhost:3002'}}) 

if __name__ == "__main__":
    app.run()