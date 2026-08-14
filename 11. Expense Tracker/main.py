import streamlit as st
from sqlalchemy import create_engine, String, Date, Text, select
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, Session
from dotenv import load_dotenv
import os
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import numpy


 
# Loading environment variables


load_dotenv()

DATA = os.getenv('DATABASE_URL')

# Creating instance of database
engine = create_engine(DATA)


 
# Database Model
 

class Base(DeclarativeBase):
    pass


class Expenses(Base):
    __tablename__ = 'expenses'

    id: Mapped[int] = mapped_column(primary_key=True)
    exp_name: Mapped[str] = mapped_column(String(100), nullable=False)
    amount: Mapped[int] = mapped_column(nullable=False)
    category: Mapped[str] = mapped_column(String(100), nullable=False)
    date = mapped_column(Date, default=date.today)


Base.metadata.create_all(engine)


 
# Checking Existing Data
 

with Session(engine) as session:
    exist = session.scalar(select(Expenses).limit(1))


 
# Adding Sample Data
 

if exist is None:

    expenses = [
        Expenses(
            exp_name="Monthly Groceries",
            amount=2500,
            category="Food",
            date=date(2026, 8, 1)
        ),
        Expenses(
            exp_name="Electricity Bill",
            amount=1850,
            category="Utilities",
            date=date(2026, 8, 2)
        ),
        Expenses(
            exp_name="Petrol",
            amount=1200,
            category="Transport",
            date=date(2026, 8, 3)
        ),
        Expenses(
            exp_name="Internet Bill",
            amount=799,
            category="Utilities",
            date=date(2026, 8, 4)
        ),
        Expenses(
            exp_name="Lunch",
            amount=450,
            category="Food",
            date=date(2026, 8, 5)
        ),
        Expenses(
            exp_name="Movie Tickets",
            amount=600,
            category="Entertainment",
            date=date(2026, 8, 6)
        ),
        Expenses(
            exp_name="Medicine",
            amount=375,
            category="Healthcare",
            date=date(2026, 8, 7)
        ),
        Expenses(
            exp_name="New Notebook",
            amount=180,
            category="Education",
            date=date(2026, 8, 8)
        ),
        Expenses(
            exp_name="Cab Ride",
            amount=320,
            category="Transport",
            date=date(2026, 8, 9)
        ),
        Expenses(
            exp_name="Coffee",
            amount=180,
            category="Food",
            date=date(2026, 8, 10)
        ),
        Expenses(
            exp_name="Online Course",
            amount=1500,
            category="Education",
            date=date(2026, 8, 11)
        ),
        Expenses(
            exp_name="Clothes",
            amount=2200,
            category="Shopping",
            date=date(2026, 8, 12)
        ),
    ]

    with Session(engine) as session:
        session.add_all(expenses)
        session.commit()


 
# Getting Data
 

with Session(engine) as session:
    result = session.query(
        Expenses
    ).order_by(
        Expenses.date.desc()
    ).all()


whole_data = []

for data in result:

    whole_data.append({
        'id': data.id,
        'exp_name': data.exp_name,
        'amount': data.amount,
        'category': data.category,
        'date': data.date
    })


df = pd.DataFrame(whole_data)


 
# CSS
 

st.markdown(
    """
    <style>

    /* ------------------------------
       Main Page
    ------------------------------ */




    /* ------------------------------
       Main Title
    ------------------------------ */

    h1 {
        color: #1e293b;
        font-size: 42px !important;
        font-weight: 700 !important;
        margin-bottom: 25px;
    }


    /* ------------------------------
       Buttons
    ------------------------------ */

    div.stButton > button {

        width: 85%;
        height: 42px;

        background-color: #2563eb;
        color: white;

        font-size: 15px;
        font-weight: 600;

        border-radius: 8px;
        border: none;

        margin-bottom: 8px;

        transition: all 0.2s ease;
    }


    /* Button Hover */

    div.stButton > button:hover {

        background-color: #1d4ed8;
        color: white;

        border: none;

        transform: translateY(-1px);

        box-shadow:
            0px 4px 10px
            rgba(37, 99, 235, 0.25);
    }


    /* ------------------------------
       Dataframe
    ------------------------------ */

    div[data-testid="stDataFrame"] {

        width: 100%;

        border-radius: 10px;

        overflow: hidden;

        border: 1px solid #dbe3ef;

        box-shadow:
            0px 3px 12px
            rgba(0, 0, 0, 0.06);
    }


    /* Make table wider */

    div[data-testid="stDataFrame"] > div {

        width: 100%;
    }


    /* Table Header */

    div[data-testid="stDataFrame"]
    [role="columnheader"] {

        font-weight: 700;
    }


    /* ------------------------------
       Tabs
    ------------------------------ */

    button[data-baseweb="tab"] {

        font-size: 17px;

        font-weight: 600;

        color: #475569;
    }


    button[data-baseweb="tab"][aria-selected="true"] {

        color: #2563eb;
    }


    /* ------------------------------
       Input Boxes
    ------------------------------ */

    div[data-baseweb="input"] {

        border-radius: 8px;
    }


    /* ------------------------------
       Select Boxes
    ------------------------------ */

    div[data-baseweb="select"] > div {

        border-radius: 8px;
    }


    /* ------------------------------
       Success/Error Messages
    ------------------------------ */

    div[data-testid="stAlert"] {

        border-radius: 10px;
    }


    /* ------------------------------
       Dialog
    ------------------------------ */

    div[role="dialog"] {

        border-radius: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


 
# Dialog Boxes
 


 
# Adding Expenses
 

@st.dialog("Add Expenses")
def add_expense():

    exp_name = st.text_input("Enter Product")

    amount = st.number_input(
        "Enter Amount",
        min_value=1
    )

    category = st.selectbox(
        "Select Cateogry",
        options=[
            'Food',
            'Utilities',
            'Transport',
            'Entertainment',
            'Healthcare',
            'Education',
            'Shopping'
        ]
    )

    date = st.date_input("Pick date")


    if st.button('Add item'):

        if not all(
            (
                exp_name.strip(),
                amount,
                category,
                date
            )
        ):

            st.error(
                "Error!!! All values must be filled"
            )

        else:

            with Session(engine) as session:

                try:

                    session.add(
                        Expenses(
                            exp_name=exp_name,
                            amount=amount,
                            category=category,
                            date=date
                        )
                    )

                    session.commit()

                except:

                    st.error("Invalid Data")


            st.session_state["expense_added"] = True

            st.rerun()


if st.session_state.get("expense_added"):

    st.success(
        "Expense added successfully!"
    )

    st.session_state["expense_added"] = False


 
# Removal of Expenses
 

@st.dialog("Remove Expenses")
def remove_exp():

    expense_id = st.number_input(
        'Enter valid ID',
        min_value=1
    )

    category = st.selectbox(
        "Select Cateogry",
        options=[
            'Food',
            'Utilities',
            'Transport',
            'Entertainment',
            'Healthcare',
            'Education',
            'Shopping'
        ]
    )


    if st.button('Remove Item'):

        if not all([id, category]):

            st.error(
                'Error !!! All values must be filled'
            )

        else:

            with Session(engine) as session:

                del_expense = session.get(
                    Expenses,
                    expense_id
                )


                if del_expense:

                    session.delete(
                        del_expense
                    )

                    session.commit()

                    st.session_state[
                        "expense_remove"
                    ] = True

                    st.rerun()

                else:

                    st.error(
                        "Invalid Expense Id"
                    )


if st.session_state.get("expense_remove"):

    st.success(
        "Expense removed successfully!"
    )

    st.session_state[
        "expense_remove"
    ] = False


 
# Update Expense
 

def update(
    choice,
    expense_id,
    change
):

    with Session(engine) as session:

        product = session.query(
            Expenses
        ).filter(
            Expenses.id == expense_id
        ).first()


        if st.button('Update Expense'):

            if product:

                setattr(
                    product,
                    choice,
                    change
                )

                session.commit()

                st.session_state[
                    "expense_update"
                ] = True

                st.rerun()

            else:

                st.error(
                    'Expense record doesnt exist'
                )


 
# Updating Expense Details
 

@st.dialog('Update Expense')
def update_exp():

    expense_id = st.number_input(
        "Enter Id"
    )

    choice = st.selectbox(
        "What do you want to update",
        options=[
            'exp_name',
            'amount',
            'category',
            'date'
        ]
    )


    if choice == 'category':

        category = st.selectbox(
            'Choose New Category',
            options=[
                'Food',
                'Utilities',
                'Transport',
                'Entertainment',
                'Healthcare',
                'Education',
                'Shopping'
            ]
        )

        update(
            choice,
            expense_id,
            category
        )


    elif choice == 'amount':

        amount = st.number_input(
            'Enter New Amount',
            min_value=1
        )

        update(
            choice,
            expense_id,
            amount
        )


    elif choice == 'date':

        date = st.date_input(
            'Enter new Date'
        )

        update(
            choice,
            expense_id,
            date
        )


    else:

        exp_name = st.text_input(
            'Enter Name'
        )

        update(
            choice,
            expense_id,
            exp_name
        )


if st.session_state.get("expense_update"):

    st.success(
        "Expense updated successfully!"
    )

    st.session_state[
        "expense_update"
    ] = False


 
# Main Page
 

st.title(
    'Personal Expense Tracker'
)


section = st.container()


with section:

    # Table gets more space than buttons

    col1, col2 = st.columns(
        [1.8, 1]
    )


    # =====================================================
    # Expense Table
    # =====================================================

    with col1:

        st.dataframe(
            whole_data,

            use_container_width=True,

            hide_index=True,

            height=500
        )


    # =====================================================
    # Buttons
    # =====================================================

    with col2:

        if st.button(
            "Remove Expense",
            use_container_width=True
        ):

            remove_exp()


        if st.button(
            "Add Expense",
            use_container_width=True
        ):

            add_expense()


        if st.button(
            "Change Expense",
            use_container_width=True
        ):

            update_exp()


 
# Analysis Tabs
 

tab1, tab2 = st.tabs(
    [
        'Category Wise Analysis',
        'Date Wise Analysis'
    ]
)


 
# Category Wise Analysis
 

with tab1:

    fig, ax = plt.subplots(
        1,
        2,
        figsize=(20, 8)
    )

    ax = ax.flatten()


    temp = df.groupby(
        'category'
    )['amount'].mean().reset_index()


    # Bar Chart

    ax[1].bar(
        temp['category'],
        temp['amount'],
        color='#2563eb'
    )

    ax[1].set_xlabel(
        'Category'
    )

    ax[1].set_ylabel(
        'Average Spent'
    )

    ax[1].set_title(
        'Expenses by Category'
    )

    ax[1].tick_params(
        axis='x',
        rotation=45
    )


    # Pie Chart

    ax[0].pie(
        temp['amount'],
        labels=temp['category'],
        autopct='%1.1f%%'
    )

    ax[0].set_title(
        'Expenses by Category'
    )


    st.pyplot(fig)


 
# Date Wise Analysis
 

with tab2:

    fig = plt.subplots(
        figsize=(12, 6)
    )


    temp = df.groupby(
        'date'
    )['amount'].mean().reset_index()


    plt.plot(
        temp['date'],
        temp['amount'],
        marker='o',
        color='#2563eb'
    )


    plt.xlabel(
        'Date'
    )

    plt.ylabel(
        'Average Spent'
    )

    plt.title(
        'Expenses by Category'
    )

    plt.xticks(
        rotation=45
    )


    st.pyplot(plt)