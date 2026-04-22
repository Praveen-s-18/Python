from connection import get_database

db = get_database()

collection = db["students"]

collection.update_one({"name": "Alice"},
                      {"$set": {"age": 21}})
print("Document updated successfully")