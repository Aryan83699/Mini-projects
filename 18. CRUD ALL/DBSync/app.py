from fastapi import FastAPI,Depends,Request,Path,HTTPException
from contextlib import asynccontextmanager,contextmanager
from db.db import get_db,get_session,init_db
from db.models import *
from sqlalchemy.orm import Session
from typing import Annotated
from pd_models import *


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
def show_students_id(id:Annotated[int,Path()],db:Session=Depends(get_session)):
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


@app.post('/addstudent')
def add_student(student:StudentsData,db:Session=Depends(get_db)):
    # username=str(StudentsData.username)
    # print(username)
    add_user=db.add(Students(username=student.username,pswd=student.pswd,email=student.email,age=student.age))
    db.commit()
   

    return {"message":"Successfully Created Resource"}

@app.post('/addcourse')
def add_student(course:CourseData,db:Session=Depends(get_session)):
    add_user=db.add(Courses(name=course.name,student_id=course.id))
    db.commit()
   

    return {"message":"Successfully Created Resource"}
    

@app.put('/updatestudent/{id}')
def update_student(id:Annotated[int,Path()],student:StudentsData,db:Session=Depends(get_db)):
    user=db.query(Students).filter(Students.id==id).first()
    if not user:
        raise HTTPException(status_code=404,detail="Student not found")

    user.username=student.username
    user.age=student.age
    user.email=student.email
    user.pswd=student.pswd

    db.commit()

    return {"message":"Successfully Updated"}

@app.put('/updatecourse/{id}')
def update_course(id:Annotated[int,Path()],course:CourseData,db:Session=Depends(get_session)):
    data=db.query(Courses).filter(Courses.id==id).first()
    if not data:
        raise HTTPException(status_code=404,detail="Student not found")

    data.name=course.name
    db.commit()

    return {"message":"Successfully Updated"}



@app.delete('/deletestudent/{id}')
def del_student(id:Annotated[int,Path()],db:Session=Depends(get_db)):
    user=db.query(Students).filter(Students.id==id).first()

    if not user:
        raise HTTPException(status_code=404,detail="Student not found")
    
    db.delete(user)
    db.commit()

    return {"message":"Record successfully deleted"}


@app.delete('/deletecourse/{id}')
def del_student(id:Annotated[int,Path()],db:Session=Depends(get_session)):
    course=db.query(Courses).filter(Courses.id==id).first()

    if not course:
        raise HTTPException(status_code=404,detail="Course not found")
    
    db.delete(course)
    db.commit()

    return {"message":"Record sucessfully delted"}

