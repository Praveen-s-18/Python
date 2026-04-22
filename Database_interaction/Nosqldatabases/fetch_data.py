from connection import get_database

db = get_database()

collection = db["students"]

documents = collection.find()

for doc in documents:
    print(doc)