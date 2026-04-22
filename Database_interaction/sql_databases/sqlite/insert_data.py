from connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute(
"INSERT INTO students (name, age) VALUES ('Alice', 22)"
)

conn.commit()
conn.close()
print("data inserted successfully")