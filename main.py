from flask import Flask, render_template, request
import unittest
import pickle
import numpy as np
import torch
import transformers
import json
from detoxify import Detoxify

#results = Detoxify('original').predict('I love you')

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def predict_sentiment():
    results = Detoxify('original').predict('I love you')
    print(results)
    return json.dumps(str(results))



if __name__ == '__main__':
    app.run(host = "127.0.0.1", port = "5000")