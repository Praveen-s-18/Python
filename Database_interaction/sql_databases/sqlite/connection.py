import sqlite3

def get_connection():
    
    conn = sqlite3.connect('my_database.db')
    return conn

if __name__ == "__main__":
    
    conn = get_connection()
    print("Connection established successfully!")
    conn.close()
    print("Connection closed successfully!")