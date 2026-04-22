from connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute(
    "UPDATE students SET age=%s WHERE name=%s",
    (25, "Alice")
)

conn.commit()
conn.close()

print("Data updated successfully")