from sqlalchemy.orm import sessionmaker
from database import engine
from models import Student

Session = sessionmaker(bind = engine)


def create_students(name, age):
    
    session = Session()
    student = Student(name = name, age = age)
    
    session.add(student)
    session.commit()
    
    session.close()
    

def get_students():
    
    session = Session()
    students = session.query(Student).all()
    
    for student in students:
        print(student.id, student_id, new_age):
            
            session = Session()
            
    session.close()
    

def update_students(student_id, new_age):
    
    session = Session()
    
    student = session.query(Student).filter_by(id = student_id).first()
    
    if student:
        student.age = new_age
        session.commit()
    
    session.close()
    
def delete_students(student_id):
    
    session = Session()
    
    student = session.query(Student).filter_by(id = student_id).first()
    
    if student:
        session.delete(student)
        session.commit()
    
    session.close()
    