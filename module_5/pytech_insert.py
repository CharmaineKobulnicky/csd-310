from pymongo import insert_one

MongoDB: insert_one()
students = {
"first_name": "Charmaine"
}

MongoDB: insert_one()
student_id = {
    "student_id": "1007, 1008, 1009"
}

charmaine_student_id = students.insert_one(1007, 1008, 1009).inserted_id

print (charmaine_student_id)
