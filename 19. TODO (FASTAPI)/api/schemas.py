from pydantic import BaseModel



class addTodo(BaseModel):
    name:str
    status:str

class Todo(BaseModel):
    id:str
    name:str
    status:str
    created_at:str

# class updateTodo(BaseModel):
#     id:str
#     name:str
#     status:str