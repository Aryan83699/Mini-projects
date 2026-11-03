from pydantic import BaseModel,EmailStr,Field
from typing import Annotated

class StudentsData(BaseModel):
    username:str
    email:EmailStr
    pswd:str
    age:Annotated[int,Field(title="Field Check",gt=18,lt=60)]

class CourseData(BaseModel):
    name:str
    id:int