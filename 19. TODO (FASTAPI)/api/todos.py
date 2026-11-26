from fastapi import APIRouter,Depends,Path,Body,Query,Request
from db.database import *
from typing import Annotated,List,Dict
from api.utils import *
from sqlalchemy import select 
from api.schemas import *
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from slowapi import Limiter,_rate_limit_exceeded_handler
from limiter import limiter


todosRouter=APIRouter(prefix='/api',tags=['TODOS'])


# GET Request Handling

@todosRouter.get('/alltodos',response_model=List[Todo])
@limiter.limit('15/minute')
async def alltodos(request:Request,db:Annotated[AsyncSession,Depends(get_db)]):
    todos=await get_all(db)
    return todos

@todosRouter.get('/activetodos',response_model=List[Todo] | Todo)
@limiter.limit('10/minute')
async def status(request:Request,db:Annotated[AsyncSession,Depends(get_db)],status:Annotated[str,Query()]):
    todos=await get_all(db,status=status)
    return todos

@todosRouter.get('/todos/{id}')
@limiter.limit('10/minute')
async def todo_by_id(request:Request,id:Annotated[str,Path()],db:Annotated[AsyncSession,Depends(get_db)]):
    todo=await get_by_id(db=db,id=id)
    return todo

# POST Request Handling 


@todosRouter.post('/addtodos',response_model=Dict,status_code=201)
@limiter.limit('5/minute')
async def add_todo(request:Request,data:Annotated[addTodo,Body()],db:Annotated[AsyncSession,Depends(get_db)]):

    id=await create_todo(db=db,data=data)
    return {"id":f"{id}"}


# PUT Request Handling

@todosRouter.put('/updatetodos/{id}',response_model=Dict)
@limiter.limit('5/minute')
async def put_todo(request:Request,id:Annotated[str,Path()],data:Annotated[addTodo,Body()],db:Annotated[AsyncSession,Depends(get_db)]):
    await update_todo(db=db,data=data,id=id)
    return {"message":"successfully updated"}


# DELETE Request Handling

@todosRouter.delete('/deletetodos/{id}',response_model=Dict)
@limiter.limit('5/minute')
async def del_todo(request:Request,id:Annotated[str,Path()],db:Annotated[AsyncSession,Depends(get_db)]):
    await delete_todo(id=id,db=db)
    return {"message":"successfully deleted todo"}

