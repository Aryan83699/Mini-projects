from fastapi import APIRouter,Depends
from db.database import *
from typing import Annotated
from sqlalchemy import select 



todosRouter=APIRouter(prefix='/api',tags=['TODOS'])



@todosRouter.get('/alltodos')
async def alltodos(db:Annotated[AsyncSession,Depends(get_db)]):
    tasks=await db.execute(select(Tasks))    
    await db.commit()
    return tasks.scalars().all()
