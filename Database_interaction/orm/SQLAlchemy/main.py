from database import engine, Base
from crud import create_student, get_student, update_student, delete_student

Base.metadata.create_all(engine)

create_student("Alice", 20)
create_student("Bob", 22)

get_students()

update_student(1, 25)
get_students()

print("\nAfter deletion")
get_students()
