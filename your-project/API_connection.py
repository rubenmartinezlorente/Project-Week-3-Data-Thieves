
import pandas as pd
import requests
import json


PUNKIPA = 'https://api.punkapi.com/v2/beers'
response = requests.get(PUNKIPA)
beer = response.json()
beers = pd.DataFrame(beer)


## make a pre-cleaning for one column (method) because when we save the .csv file, the data (dictionary object) saves like an string
def clean_json_temperature(dictionary):
    return dictionary['mash_temp'][0]['temp']['value']

def clean_json_duration(dictionary):
    return dictionary['mash_temp'][0]['duration']

beers['temperature'] = beers['method'].apply(clean_json_temperature)
beers['duration'] = beers['method'].apply(clean_json_duration)


beers.to_csv('NEW_DATA/punkapi.csv', index=False)

