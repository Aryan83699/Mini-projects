from pydantic import BaseModel
from typing import List , Dict
from bson import BSON


class AllStudentsRes(BaseModel):
    id:Dict
    name:str
    email:str
    location:str
    courses:List


# class StudentID(BaseModel):
#     id:str