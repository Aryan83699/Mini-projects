from db.database import *
from typing import Annotated
from sqlalchemy import select,delete
from fastapi import HTTPException



async def get_all(db,status=None):
    if status in ['active','completed','inactive']:
        tasks=await db.execute(select(Tasks).where(Tasks.status==status))
        return tasks.scalars().all()

    elif status is None:
        tasks=await db.execute(select(Tasks))
        return tasks.scalars().all()
    else:
        raise HTTPException(status_code=422,detail="incorrect status")


async def create_todo(db,data):
    todos=Tasks(name=data.name,status=data.status)
    db.add(todos)
    await db.commit()
    await db.refresh(todos)

    return todos.id

async def get_by_id(db,id):
    todo=await db.execute(select(Tasks).where(Tasks.id==id))
    return todo.scalar_one_or_none()

async def update_todo(db,data,id):
    todo=await db.execute(select(Tasks).where(Tasks.id==id))
    if not todo:
        raise HTTPException(status_code=404,detail="todo not found")
    todo = todo.scalar_one_or_none()
    todo.name=data.name
    todo.status=data.status
    await db.commit()
    await db.refresh(todo)

async def delete_todo(db,id):
    todo=await db.execute(select(Tasks).where(Tasks.id==id))
    if not todo:
        raise HTTPException(status_code=404,detail="todo not found")
    await db.execute(delete(Tasks).where(Tasks.id==id))
    await db.commit()
