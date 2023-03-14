# Import libraries
import requests
from tinydb import TinyDB
from pprint import pprint
# Define a function to get the data from the database
db = TinyDB('db.json')
# Add the data to the database through the API

# BASE_URL = 'http://localhost:8000/api/add'
# for data in db.values():
#     for idx,item in enumerate(data):
#         item['name']=item['brend'] 
#         price = item['price']        
#         item['price']=float(price[:-5].replace(' ',''))
#         response = requests.post(BASE_URL, json=item)
        
#         # Print progress to the console
#         print(f'Progress: {idx+1}/{len(data)} \t Status: {response.status_code}')
c = 0
tables = db.tables()
for table in tables:
    collection = db.table(table)
    smartphones = collection.all()
    for smartphone in smartphones:
        smartphone['price'] = float(smartphone['price'][:-5].replace(' ', ''))
        smartphone['name'] = smartphone['brend']
        smartphone['ram'] = int(smartphone['ram'])
        smartphone['memory'] = int(smartphone['memory'])
        smartphone.pop('brend')
        c += 1
        
        response = requests.post('http://127.0.0.1:8000/api/add', json=smartphone)
        print(smartphone['name'], response.status_code)
print(c)