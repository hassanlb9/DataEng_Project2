from calendar import c
import unittest
import pickle
import torch
import transformers
import numpy as np
import json
from detoxify import Detoxify
from flask import Flask, request, jsonify, current_app
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
model=Detoxify('original')
CLASSES = [
    "toxicity",
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]
x=[{
      "toxicity": 0,
      "severe_toxicity":0,
      "obscene":0

  }]


@app.route('/test_text', methods=['GET', 'POST'])

def test0():
       global v0
       v0=model.predict('hello my bro')
       print(v0)
       
       return json.dumps(str(v0))


@app.route('/post_text', methods=['GET', 'POST'])
def testPost():
   if request.method == 'POST':
       var = request.json.get('name')
       global v0
       global vx
       global dic
       dic={}
       v0=model.predict(var)
       print(model.predict(var))
       k=list(v0.keys())
       for i in k:
          dic[i]=np.float64(v0[i])
       
       print(var)
       vx=[(dic)]
       print(vx)
   return json.dumps(vx)
  

    
# because backend and frontend use different ports, we have to enable cross-origin requests
@app.route('/get_text', methods=['GET', 'POST'])
def testPost1():
    
   var1 = testPost()
   
   return var1

cors = CORS(app, resources={'/*':{'origins': 'http://localhost:3000'}}) 

if __name__ == "__main__":
    app.run()
