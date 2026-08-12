import streamlit as st
from sqlalchemy import create_engine,String,Date,Text,select
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase,Session
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
    category:Mapped[str]=mapped_column(String(100),nullable=False)
    date=mapped_column(Date,default=date.today())

Base.metadata.create_all(engine)



with Session(engine) as session:
    exist=session.scalar(select(Expenses).limit(1))



if exist is None:

    expenses = [
        Expenses(exp_name="Monthly Groceries", amount=2500, category="Food", date=date(2026, 8, 1)),
        Expenses(exp_name="Electricity Bill", amount=1850, category="Utilities", date=date(2026, 8, 2)),
        Expenses(exp_name="Petrol", amount=1200, category="Transport", date=date(2026, 8, 3)),
        Expenses(exp_name="Internet Bill", amount=799, category="Utilities", date=date(2026, 8, 4)),
        Expenses(exp_name="Lunch", amount=450, category="Food", date=date(2026, 8, 5)),
        Expenses(exp_name="Movie Tickets", amount=600, category="Entertainment", date=date(2026, 8, 6)),
        Expenses(exp_name="Medicine", amount=375, category="Healthcare", date=date(2026, 8, 7)),
        Expenses(exp_name="New Notebook", amount=180, category="Education", date=date(2026, 8, 8)),
        Expenses(exp_name="Cab Ride", amount=320, category="Transport", date=date(2026, 8, 9)),
        Expenses(exp_name="Coffee", amount=180, category="Food", date=date(2026, 8, 10)),
        Expenses(exp_name="Online Course", amount=1500, category="Education", date=date(2026, 8, 11)),
        Expenses(exp_name="Clothes", amount=2200, category="Shopping", date=date(2026, 8, 12)),
    ]


    with Session(engine) as session:
        session.add_all(expenses)
        session.commit()



with Session(engine) as session:
    result=session.query(Expenses).all()


# df=pd.DataFrame(columns=['id','exp_name','amount','category','date'])

whole_data=[]

for data in result:
    whole_data.append({'id':data.id,'exp_name':data.exp_name,'amount':data.amount,'category':data.category,'date':data.date})


st.title('Personal Expense Tracker')
st.dataframe(whole_data)


import streamlit as st
from datetime import date

@st.dialog("Add New Expense")
def add_expense():

    exp_name = st.text_input("Expense Name")

    amount = st.number_input(
        "Amount",
        min_value=0.0,
        step=100.0
    )

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Transport",
            "Utilities",
            "Entertainment",
            "Healthcare",
            "Education",
            "Shopping",
            "Other"
        ]
    )

    expense_date = st.date_input(
        "Date",
        value=date.today()
    )

    if st.button("Insert Expense"):

        if not exp_name:
            st.error("Please enter an expense name.")

        elif amount <= 0:
            st.error("Amount must be greater than 0.")

        else:
            with Session(engine) as session:

                new_expense = Expenses(
                    exp_name=exp_name,
                    amount=amount,
                    category=category,
                    date=expense_date
                )

                session.add(new_expense)
                session.commit()

            st.success("Expense added successfully!")

            st.rerun()


# Main page
st.title("💰 Expense Tracker")

if st.button("➕ Add Expense"):
    add_expense()