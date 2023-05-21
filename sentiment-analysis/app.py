from flask import Flask, request, jsonify
import pandas as pd
from sentiment_score import *

### create flask app
app = Flask(__name__)

@app.route("/")
def hi():
    return 'Success'

@app.route("/sentiment")
def sentiment():
    return 'Success'

if __name__ == "__main__":
    #app.run(debug=True,port=5000)
    print("App run Succesfully")
