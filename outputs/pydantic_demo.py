from pydantic import BaseModel

class Student(BaseModel):

    # name: str
    name: str = 'Sidharth'

new_student = {}

student = Student(**new_student)

print(student)


# pydantic is a data validation and data parsing library for python