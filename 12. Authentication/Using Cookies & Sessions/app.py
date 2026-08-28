from fastapi import FastAPI 
from fastapi.templating import Jinja2Templates
from smtplib import SMTP
from email.message import EmailMessage
import os
from dotenv import load_dotenv
import random

load_dotenv()

app=FastAPI()





def send_otp():
    msg=EmailMessage()
    msg['Subject']='Email Verification'
    msg['From']=os.getenv('EMAIL_ID')
    msg['To']=os.getenv('EMAIL_ID')
    msg.set_content(str(round(random.random()*10000)))



    with SMTP('smtp.gmail.com',port=587) as server:
        server.starttls()
        server.login(
            user=os.getenv('EMAIL_ID'),
            password=os.getenv('PSWD')
        )
        server.send_message(msg)



@app.get('/')
def home():
    return {'Welcome'}

@app.get('/email')
def email():
    send_otp()
    return 'Daddys Home'