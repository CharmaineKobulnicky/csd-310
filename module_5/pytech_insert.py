import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.lej4x8e.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client["pytech"]
collection = db["students"]


fred = {"first_name": "Fred", "last_name": "Bras", "student_id": "1007"}
jake = {"first_name": "Jake", "last_name": "Brown", "student_id": "1008"}
hanz = {"first_name": "Hanz", "last_name": "Harris", "student_id": "1009"}

print("-- INSERT STATEMENT --")
fred_student_id = collection.insert_one(fred).inserted_id
print(f"Inserted student record Fred Bras into the students collection with document id {fred_student_id}")
jake_student_id = collection.insert_one(jake).inserted_id
print(f"Inserted student record Jake Brown into the students collection with document id {jake_student_id}")
hanz_student_id = collection.insert_one(hanz).inserted_id
print(f"Inserted student record Hanz Harris into the students collection with document id {hanz_student_id}")
