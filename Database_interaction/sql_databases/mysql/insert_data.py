from connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.executemany(
    "INSERT INTO students (name, age) VALUES (%s, %s)",
    [
        ("Alice", 22),
        ("Bob", 21),
        ("Charlie", 23)
    ]
)

conn.commit()
conn.close()
print("Data inserted successfully!")