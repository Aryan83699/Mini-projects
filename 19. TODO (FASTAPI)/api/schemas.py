from pydantic import BaseModel
from typing import Literal
from uuid import UUID
from datetime import datetime 


class addTodo(BaseModel):
    name:str
    status:str

class Todo(BaseModel):
    id:UUID
    name:str
    status:str
    created_at:datetime

# class updateTodo(BaseModel):
#     id:str
#     name:str
#     status:str