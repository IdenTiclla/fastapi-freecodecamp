from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
students = {
    1: {
        'name': 'john',
        'age': 14,
        'class': 'year 12'
    },
    2: {
        'name': 'tim',
        'age': 11,
        'class': 'year 11'
    },
}

class Student(BaseModel):
    name : str
    age : int
    year : str

@app.get('/')
def index():
    return {
        "name": "First Data"
    }
@app.get('/get-student/{student_id}')
def get_student(student_id: int = Path(None, description='The ID of the student you want to view', gt=0, lt=3)):
    return students[student_id]

# get-by-name?name='alex'
@app.get('/get-by-name/{student_id}')
def get_student_by_name(*, student_id : int, name: Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {"data": "Not Found."}

@app.post('/create-student/{student_id}')
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"error": "student exists"}
    students[student_id] = student
    return students[student_id]