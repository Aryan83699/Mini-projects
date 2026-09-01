from email.message import EmailMessage
from smtplib import SMTP
import secrets
import os
from dotenv import load_dotenv
from jose import jwt
from passlib.context import CryptContext


load_dotenv()


pswd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password):
    return pswd_context.hash(password)

def check_password(plain_pswd:str,hash_pswd:str):
    return pswd_context.verify(plain_pswd,hash_pswd)


pswd="Aryan"
print(hash_password(pswd))
print(check_password(pswd,hash_password(pswd)))


def send_messages(user_email:str):
    otp="".join(str(secrets.randbelow(10)) for i in range(6))
    msg=EmailMessage()
    msg['Subject']='OTP Verification'
    msg['From']=os.getenv("EMAIL")
    msg["To"]=user_email
    msg.set_content(f"Your current OTP is {otp}")
    print(msg)

    with SMTP(host='smtp.gmail.com',port=587) as smtp:
        smtp.starttls()
        smtp.login(user=os.getenv("EMAIL") , password=os.getenv("PSWD"))
        smtp.send_message(msg)


