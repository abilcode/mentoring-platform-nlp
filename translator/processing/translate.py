from googletrans import Translator
import pandas as pd

def to_translate(data,dest='en'):
    translator = Translator()
    if isinstance(data, str) == True :
        return translator.translate(data,dest=dest).text
    
    else :
        data_set = data.copy()
        #data_set = pd.DataFrame(data_set)
        translated  = []
        lang_input  = []
        lang_output = []

        for item in data_set['input'] :
            translations = translator.translate(item, dest=dest)
            translated.append(translations.text)
            lang_input.append(translations.src)
            lang_output.append(translations.dest)
            
        data_set['lang_input'] = lang_input
        data_set['translated'] = translated
        data_set['lang_output']= lang_output

        data_pd = pd.DataFrame(data_set)
        return data_pd