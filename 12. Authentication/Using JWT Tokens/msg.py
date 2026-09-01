from email.message import EmailMessage
from smtplib import SMTP
import secrets
import os
from dotenv import load_dotenv
from fastapi import Request


load_dotenv()




def send_messages(user_email:str,request:Request):
    otp="".join(str(secrets.randbelow(10)) for i in range(6))
    msg=EmailMessage()
    msg['Subject']='OTP Verification'
    msg['From']=os.getenv("EMAIL")
    msg["To"]=user_email
    msg.set_content(f"Your current OTP is {otp}")

    with SMTP(host='smtp.gmail.com',port=587) as smtp:
        smtp.starttls()
        smtp.login(user=os.getenv("EMAIL") , password=os.getenv("PSWD"))
        smtp.send_message(msg)

    request.session["OTP"]=otp

