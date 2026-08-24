from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from smtplib import SMTP
from email.message import EmailMessage
import os
import random
from dotenv import load_dotenv


load_dotenv()


app=FastAPI()


def send_messages(client_email):
    msg=EmailMessage()
    msg.set_content(str(random.random()*7))
    msg['Subject']='OTP for verification '
    msg['From']=os.getenv("EMAIL_ID")
    msg['To']=client_email

    with SMTP('smtp.gmail.com',587) as server:
        server.starttls()
        server.login(os.getenv('EMAIL_ID'),os.getenv('PSWD'))
        server.send_message(msg)


templates=Jinja2Templates(directory='templates')


@app.get('/')
def home(request:Request):
    return templates.TemplateResponse(request,'login.html')


@app.get('/register')
def register(request:Request):
    return templates.TemplateResponse(request,'register.html')



