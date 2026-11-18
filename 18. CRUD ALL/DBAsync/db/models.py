from db.db import Base
import uuid 
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import Integer,String,ForeignKey
from sqlalchemy.dialects.postgresql import UUID



class Students(Base):
    __tablename__="students"

    id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    username:Mapped[str]=mapped_column(String,nullable=False)
    email:Mapped[str]=mapped_column(String,nullable=False,unique=True)
    pswd:Mapped[str]=mapped_column(String,nullable=False)
    age:Mapped[int]=mapped_column(Integer,nullable=False)

    courses:Mapped[list["Courses"]]=relationship("Courses",back_populates="students",passive_deletes=True,passive_updates=True)


class Courses(Base):
    __tablename__ = "courses"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    student_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("students.id", ondelete="CASCADE"),
        nullable=True
    )

    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    students: Mapped["Students"] = relationship(
        "Students",
        back_populates="courses"
    )
    
    