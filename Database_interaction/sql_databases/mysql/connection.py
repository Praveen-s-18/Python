import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Praveen@2003",
        database = "python_demo"
    )
    
    return conn

if __name__ == "__main__":
    connection = get_connection()
    print("Connection established successfully!")
    connection.close()
    print("connection closed")