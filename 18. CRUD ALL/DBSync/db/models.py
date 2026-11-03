from db.db import Base
import uuid
from sqlalchemy import ForeignKey,CheckConstraint,String
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy.dialects.postgresql import UUID


class Students(Base):
    __tablename__="students"

    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    username:Mapped[str]=mapped_column(String(50),unique=True,nullable=False)
    email:Mapped[str]=mapped_column(String(255),unique=True,nullable=False)
    pswd:Mapped[str]=mapped_column(String(255),nullable=False)
    age:Mapped[int]=mapped_column(CheckConstraint("age>18"))

    courses:Mapped[list["Courses"]]=relationship("Courses",back_populates="students")


class Courses(Base):
    __tablename__="courses"

    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    student_id:Mapped[int]=mapped_column(ForeignKey("students.id"))
    name:Mapped[str]=mapped_column(String(50),nullable=False,unique=True)

    students:Mapped[Students]=relationship("Students",back_populates="courses")

    

    