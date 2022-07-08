import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.lej4x8e.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client["pytech"]
collection = db["students"]

students = collection.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students:
    student_id = student["student_id"]
    student_first_name = student["first_name"]
    student_last_name = student["last_name"]
    print(f"Student ID: {student_id}")
    print(f"First Name: {student_first_name}")
    print(f"Last Name: {student_last_name}")
    print()

print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
docJake = collection.find_one({"student_id": 1008})
jake_student_id = docJake["student_id"]
jake_student_first_name = docJake["first_name"]
jake_student_last_name = docJake["last_name"]
print(f"Student ID: {jake_student_id}")
print(f"First Name: {jake_student_first_name}")
print(f"Last Name: {jake_student_last_name}")
print()
