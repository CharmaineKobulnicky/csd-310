import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.lej4x8e.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient("mongodb+srv://admin:admin@cluster0.lej4x8e.mongodb.net/?retryWrites=true&w=majority")
db = client.pytech
print(db.list_collection_names)
