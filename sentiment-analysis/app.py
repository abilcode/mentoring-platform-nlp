from flask import Flask, request, jsonify
import pandas as pd
from sentiment_score import *

### create flask app
app = Flask(__name__)

@app.route("/")
def hi():
    return 'Success'

@app.route("/sentiment",methods=['POST'])
def sentiment():
    json_      = request.json
    #sentiment  = polarity_scores_roberta(json_)
    count = 0
    for i in json_:
        if 'text' in json_[count]:
            temp = json_[count]
            a = polarity_scores_roberta(temp['text'])[1]
            #b = polarity_scores_roberta(temp['text'])[1]['Value']
            temp['sentiment'] = a['Status']
            count +=1
        
    #return count
    # Print the contents of the dictionary
    return jsonify(json_)
        
    

if __name__ == "__main__":
    app.run(debug=True,port=5000)
    
