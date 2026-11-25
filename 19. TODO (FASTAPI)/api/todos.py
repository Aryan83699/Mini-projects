from fastapi import APIRouter,Depends,Path,Body,Query
from db.database import *
from typing import Annotated,List,Dict
from api.utils import *
from sqlalchemy import select 
from api.schemas import *



todosRouter=APIRouter(prefix='/api',tags=['TODOS'])


# GET Request Handling

@todosRouter.get('/alltodos',response_model=List[Todo])
async def alltodos(db:Annotated[AsyncSession,Depends(get_db)]):
    todos=await get_all(db)
    return todos

@todosRouter.get('/activetodos',response_model=List[Todo] | Todo)
async def status(db:Annotated[AsyncSession,Depends(get_db)],status:Annotated[str,Query()]):
    todos=await get_all(db,status=status)
    return todos

@todosRouter.get('/todos/{id}')
async def todo_by_id(id:Annotated[str,Path()],db:Annotated[AsyncSession,Depends(get_db)]):
    todo=await get_by_id(db=db,id=id)
    return todo

# POST Request Handling 


@todosRouter.post('/addtodos',response_model=Dict)
async def add_todo(data:Annotated[addTodo,Body()],db:Annotated[AsyncSession,Depends(get_db)]):

    id=await create_todo(db=db,data=data)
    return {"message":f"successfully added todo . id :- {id}"}


# PUT Request Handling

@todosRouter.put('/updatetodos/{id}',response_model=Dict)
async def put_todo(id:Annotated[str,Path()],data:Annotated[addTodo,Body()],db:Annotated[AsyncSession,Depends(get_db)]):
    await update_todo(db=db,data=data,id=id)
    return {"message":"successfully updated"}


# DELETE Request Handling

@todosRouter.delete('/deletetodos/{id}',response_model=Dict)
async def del_todo(id:Annotated[str,Path()],db:Annotated[AsyncSession,Depends(get_db)]):
    await delete_todo(id=id,db=db)
    return {"message":"successfully deleted todo"}
