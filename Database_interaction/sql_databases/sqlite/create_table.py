from connection import get_connection

conn = get_connection()
cursor = conn.cursor()


cursor.execute("""
               CREATE TABLE IF NOT EXISTS students (
                   id INTEGER PRIMARY KEY,
                   name TEXT,
                   age INTEGER
               )""")

conn.commit()
conn.close()
print('table created succesfully')