from sqlalchemy.orm import mapped_column,Mapped,relationship
from db.db import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ForeignKey
import uuid


class Students(Base):
    __tablename__="students"

    id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True)
    username:Mapped[str]=mapped_column(nullable=False)
    email:Mapped[str]=mapped_column(nullable=False,unique=True)
    pswd:Mapped[str]=mapped_column(nullable=False)
    age:Mapped[int]=mapped_column(nullable=False)

    courses:Mapped[list["Courses"]]=relationship("Courses",back_populates="students",passive_deletes=True)


class Courses(Base):
    __tablename__="courses"

    id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True)
    stud_id:Mapped[uuid.UUID]=mapped_column(ForeignKey())
    name:Mapped[str]=mapped_column(nullable=False)

