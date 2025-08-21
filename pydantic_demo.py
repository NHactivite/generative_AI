from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str ="nik"  # nik is defult value if new_student={} then nik print
    age:Optional[int] = None 
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,default=5)


new_student={"name":"nikhil", "age":"32","email":"nik@gmail.com","cgpa":"9.8999"}

# 1. if "name":43 then give error it should be string 
# 2. pydantic is smart it behind scen do some works. one is if data is not required format then it 
# convert to required format like in above with age we pass string but it convert to number
# 3. EmailStr in pydantic provide build in email validation support
# 4. using Field we apply constraint

student=Student(**new_student)

print(student)
print(student.name)

print(student.model_dump_json()) # convert to json