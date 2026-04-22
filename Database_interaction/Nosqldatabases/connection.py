from pymongo import MongoClient

def get_database():
    
    client = MongoClient("mongodb://localhost:27017/")
    db = client["students_db"]
    return db

if __name__ == "__main__":
    
    db = get_database()
    print("Connected to MongoDB:", db.name)