from connection import get_database

db = get_database()

collection = db["students"]

student = {
    "name": "Alice",
    "age": 20
}

collection.insert_one(student)
print("Student inserted:", student)