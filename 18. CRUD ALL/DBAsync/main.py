from fastapi import FastAPI,Depends,Path,HTTPException
from contextlib import asynccontextmanager
from db.models import *
from db.db import db_init,get_db,AsyncSession,engine
from schemas import Students_model,Courses_model
from typing import Annotated,List
from sqlalchemy import select
import uuid





@asynccontextmanager
async def lifespan(app:FastAPI):
    await db_init()
    yield
    await engine.dispose()

app=FastAPI(lifespan=lifespan)



@app.get('/')
def home():
    return {"message":"Async Database API"}



@app.get('/students_all',response_model=List[Students_model])
async def get_students(db:Annotated[AsyncSession,Depends(get_db)]):
    students=await db.execute(select(Students))
    await db.commit()
    return students.scalars().all()


@app.get('/courses_all',response_model=List[Courses_model])
async def get_courses(db:Annotated[AsyncSession,Depends(get_db)]):
    courses=await db.execute(select(Courses))
    await db.commit()
    return courses.scalars().all()

@app.get('/courses/{id}', response_model=Courses_model)
async def get_courses_byID(id: Annotated[uuid.UUID, Path()],
    db: Annotated[AsyncSession, Depends(get_db)]):
    course=await db.execute(select(Courses).where(Courses.id==id))
    course = course.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


@app.get('/students/{id}', response_model=Students_model)
async def get_students_byID(id: Annotated[uuid.UUID, Path()],
    db: Annotated[AsyncSession, Depends(get_db)]):
    students=await db.execute(select(Students).where(Students.id==id))
    student = students.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student




