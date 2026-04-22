from connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute(
    "UPDATE students SET age=25 WHERE name='Alice'"
)

conn.commit()
conn.close()

print("Data updated successfully")