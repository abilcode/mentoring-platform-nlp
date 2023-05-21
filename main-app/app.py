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
    translated = to_translate(json_[0]) 
    return {'input':[i for i in translated.input],
            'outout':[i for i in translated.translated]
            }

@app.route("/sentiment",methods=['POST'])
def sentiment():
    json_      = request.json
    #sentiment  = polarity_scores_roberta(json_)
    count = 0
    for i in json_:
        if 'text' in json_[count]:
            temp = json_[count]
            a = polarity_scores_roberta(temp['text'])[1]
            temp['sentiment'] = a['Status']
            count +=1
        
    return jsonify(json_)

if __name__ == "__main__":
    app.run(debug=True,port=5000)