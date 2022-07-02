MongoDB: find()
docs = db.collection_students.find({})

for doc in docs:
print(doc)

MongoDB: students.find_one()
doc = db.collection_students.find_one({"student_id": "1007"})
doc = db.collection_students.find_one({"student_id": "1008"})
doc = db.collection_students.find_one({"student_id": "1009"})