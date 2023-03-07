# Import libraries
import requests
from tinydb import TinyDB

# Define a function to get the data from the database
def get_data(path: str ,brand: str):
    # Get the data from the database
    db = TinyDB('db.json')
    table = db.table(brand)
    # Return the data
    return table.all()

data = get_data(path='db.json',brand='apple')

# Add the data to the database through the API

BASE_URL = 'http://localhost:8000/api/add'

for idx,item in enumerate(data):
    item['name']=item['brend'] 
    response = requests.post(BASE_URL, json=item)
    
    # Print progress to the console
    print(f'Progress: {idx+1}/{len(data)} \t Status: {response.status_code}')
    
    

