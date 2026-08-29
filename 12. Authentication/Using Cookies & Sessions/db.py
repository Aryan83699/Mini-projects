from sqlalchemy import create_engine,Integer,String,Date
from sqlalchemy.orm import mapped_column,Session,sessionmaker,DeclarativeBase
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

# URL=os.getenv("DB_URL")

engine=create_engine(os.getenv("DB_URL"))

SessionLocal=sessionmaker(bind=engine,expire_on_commit=False)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__="users"

    id=mapped_column(Integer,primary_key=True)
    email=mapped_column(String(255) , nullable=False, unique=True)
    password=mapped_column(String(255),nullable=False,unique=False)
    role=mapped_column(String(255),nullable=False,unique=False)
    created_date=mapped_column(Date,default=datetime.now())

Base.metadata.create_all(engine)

with SessionLocal() as session:
    data=session.query(User).first()
    if data :
        pass
    else:
        session.add(
            User(id=3007,email='aryansingha887@gmail.com',password='Aryan@2005',role='admin')
        )
        session.commit()



