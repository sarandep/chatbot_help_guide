#third-party imports
from decouple import config
from pymongo import MongoClient
from decouple import config

'''
function for connecting to databases
'''

def mongodb_connection(db_uri:str=config("DB_URI"),db_name:str=config("DB_NAME")):
    try:
        client = MongoClient(db_uri)
        db = client[db_name]
        return db
    except Exception as e:
        print('ERROR ==>',str(e))
