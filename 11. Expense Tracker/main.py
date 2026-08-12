import streamlit as st
from sqlalchemy import create_engine,String,Date
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase
from dotenv import load_dotenv
import os
from datetime import date
import pandas as pd

#loading environment variables

load_dotenv()

DATA=os.getenv('DATABASE_URL')

#creating instance of database
engine=create_engine(DATA)

class Base(DeclarativeBase):
    pass

class Expenses(Base):
    __tablename__='expenses'
    id:Mapped[int]=mapped_column(primary_key=True)
    exp_name:Mapped[str]=mapped_column(String(100),nullable=False)
    amount:Mapped[int]=mapped_column(nullable=False)
    date=mapped_column(Date,default=date.today())

Base.metadata.create_all(engine)

