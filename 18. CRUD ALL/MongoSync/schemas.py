from pydantic import BaseModel
from typing import List , Dict
from bson import BSON


class AllStudentsRes(BaseModel):
    id:Dict
    name:str
    email:str
    location:str
    courses:List[str]


class AddStudent(BaseModel):
    name:str
    email:str
    location:str
    courses:List[str]
    