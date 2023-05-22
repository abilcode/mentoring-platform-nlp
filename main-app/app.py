from flask import Flask, request, jsonify
from function.nlp_problem import *
import pandas as pd

### create flask app
app = Flask(__name__)

@app.route("/")
def hi():
    return 'Success Creating Main App'

@app.route("/translate",methods=['POST'])
def translate():
    json_      = request.json
    count = 0
    for i in json_:
        temp = json_[count]
        if 'feedback' in temp:
            temp['translate'] = to_translate(dest='en',data=temp['feedback'])
        count +=1
    return jsonify(json_)

@app.route("/sentiment",methods=['POST'])
def sentiment():
    json_      = request.json
    count = 0
    for i in json_:
        if 'feedback' in json_[count]:
            temp = json_[count]
            a = polarity_scores_roberta(temp['feedback'])[1]
            temp['sentiment'] = a['Status']
            count +=1
    return jsonify(json_)

if __name__ == "__main__":
    app.run(debug=True,port=5000)