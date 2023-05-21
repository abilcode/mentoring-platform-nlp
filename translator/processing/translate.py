from googletrans import Translator
import pandas as pd
import json

def to_translate(data,dest='en'):
    translator = Translator()
    if isinstance(data, str) == True :
        return translator.translate(data,dest=dest).text

def read_data(data='sample.json'):
    data = data
    with open(data, 'r') as file:
        input = json.load(file)
   
    return input

if __name__=="__main__":
    data = read_data()
    print('=='*30)
    for dictionary in data:
        if 'text' in dictionary:
            dictionary['translate'] = to_translate(dest='en',data=dictionary['text'])

    for dictionary in data:
        # Print the contents of the dictionary
        for key, value in dictionary.items():
            print(f'{key}: {value}')
    
    