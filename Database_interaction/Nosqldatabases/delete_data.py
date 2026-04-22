from connection import get_database

db = get_database()

collection = db["students"]

collection.delete_one({"name": "Alice"})
print("Document deleted successfully")