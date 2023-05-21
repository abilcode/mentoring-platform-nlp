from processing.translate import to_translate
from flask import Flask, request, jsonify
import pandas as pd

### create flask app
app = Flask(__name__)

@app.route("/")
def hi():
    return 'Success'

@app.route("/translate",methods=['POST'])
def translate():
    json_      = request.json
    # translated = to_translate(json_[0]) 
    # return {'input':[i for i in translated.input],
    #         'outout':[i for i in translated.translated]
    #         }
    count = 0
    for i in json_:
        temp = json_[count]
        if 'text' in temp:
            temp['translate'] = to_translate(dest='en',data=temp['text'])
        count +=1
    return jsonify(json_)

            
            
if __name__ == "__main__":
    app.run(debug=True,port=5000)