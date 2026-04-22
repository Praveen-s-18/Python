from connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute(
    "DELETE FROM students WHERE name=%s",
    ("",)
)

conn.commit()
conn.close()

print("Data deleted successfully")