from fastapi import FastAPI,Depends,Request,Path,HTTPException
from contextlib import asynccontextmanager,contextmanager
from db.db import get_db,get_session,init_db
from db.models import *
from sqlalchemy.orm import Session
from typing import Annotated


@asynccontextmanager
async def lifespan(app:FastAPI):
    await init_db()
    yield

app=FastAPI(
    lifespan=lifespan
)


@app.get('/')
def root():
    return {'message':'Hello world'}


# Performing CRUD

@app.get('/students')
def show_students(db:Session=Depends(get_db)):
    users=db.query(Students).order_by("id").all()
    db.commit()

    return users

@app.get('/courses')
def show_courses(db:Session=Depends(get_session)):
    courses=db.query(Courses).order_by("id").all()
    db.commit()

    return courses

@app.get('/course/{id}')
def show_students_id(id:Annotated[int,Path()],db:Session=Depends(get_db)):
    course=db.query(Courses).filter(Courses.id==id).first()

    if course:
        return course

    raise HTTPException(status_code=404,detail="Course doesn't exists'")

@app.get('/student/{id}')
def show_students_id(id:Annotated[int,Path()],db:Session=Depends(get_db)):
    users=db.query(Students).filter(Students.id==id).first()

    if users:
        return users

    raise HTTPException(status_code=404,detail="Students doesn't exists'")

