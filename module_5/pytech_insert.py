import pymongo
from pymongo import MongoClient
from pymongo import MongoDB
from pymongo import insert_one
from pymongo import students

client = pymongo.MongoClient ("mongodb+srv://admin:admin@cluster0.lej4x8e.mongodb.net/?retryWrites=true&w=majority")
db = client ["pytech"]
collection = db ["students"]

MongoDB: insert_one()
fred = {
    "first_name": "Fred"
},
student_id = {
    "student_id": "1007"
}
jake = {
    "first_name": "Jake"
},
student_id = {
    "student_id": "1008"
}
hanz = {
    "first_name": "Hanz"
},
student_id = {
    "student_id": "1009"
}

fred_student_id = students.insert_one(fred).inserted_id
jake_student_id = students.insert_one(jake).inserted_id
hanz_student_id = students.insert_one(hanz).inserted_id

print(fred_student_id)
print(jake_student_id)
print(hanz_student_id)
