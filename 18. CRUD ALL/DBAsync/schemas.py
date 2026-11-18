from pydantic import BaseModel,EmailStr
from typing import List
import uuid



class Students_model(BaseModel):
    id:uuid.UUID
    username:str
    email:str
    pswd:str
    age:int


class Courses_model(BaseModel):
    id:uuid.UUID
    student_id:uuid.UUID
    name:str
