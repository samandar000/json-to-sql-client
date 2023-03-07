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
print(data[0])
