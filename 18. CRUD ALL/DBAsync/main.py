from fastapi import FastAPI,Depends,Path,HTTPException,Body,Request
from contextlib import asynccontextmanager
from db.models import *
from db.db import db_init,get_db,AsyncSession,engine
from schemas import Students_model,Courses_model,Students_input,Courses_input
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



@app.post('/add_student')
async def add_student(request:Request,student:Annotated[Students_input,Body()],db:Annotated[AsyncSession,Depends(get_db)]):
    data=Students(username=student.username,age=student.age,email=student.email,pswd=student.pswd)
    student=db.add(data)
    await db.commit()
    return {"message":"successfully student created"}


@app.post('/add_course')
async def add_course(request:Request,course:Annotated[Courses_input,Body()],db:Annotated[AsyncSession,Depends(get_db)]):
    data=Courses(student_id=course.student_id,name=course.name)
    courses=db.add(data)
    await db.commit()
    return {"message":"successfully course created"}
    


