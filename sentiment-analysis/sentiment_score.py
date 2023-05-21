import pandas as pd
import numpy as np
import json 

from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax

MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

## Function polarity scores
def polarity_scores_roberta(data):
    ### Loading Pre-trained roberta model
    
    encoded_text = tokenizer(data, return_tensors='pt')
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    scores_dict = {
        'negative' : scores[0],
        'neutral'  : scores[1],
        'positive' : scores[2]
    }

    max_value = max(scores_dict, key=lambda k: scores_dict[k])
    value     = scores_dict[max_value]
    sentiment = {'Status':max_value,
                 'Value':value}
    return scores_dict , sentiment

def read_data(data='../sentiment-analysis/sample.json'):
    data = data
    with open(data, 'r') as file:
        input = json.load(file)
    input = data
    for dictionary in input:
    # Print the contents of the dictionary
        if 'text' in dictionary:
            _ , dictionary['sentiment'] = polarity_scores_roberta(dictionary['text'])
    return input
    

if __name__=="__main__":
    
    # data = read_data()
    # for dictionary in data:
    # # Print the contents of the dictionary
    #     for key, value in dictionary.items():
    #         print(f'{key}: {value}')
    
    
    print(polarity_scores_roberta('I Hate u')[1]['Status'])

   