from fastapi import FastAPI , Request ,Form , Depends , HTTPException , Response 
from fastapi.templating import Jinja2Templates
from smtplib import SMTP
from email.message import EmailMessage
import os
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import random
from starlette.middleware.sessions import SessionMiddleware
from typing import Annotated
from db import SessionLocal , User
from datetime import datetime , timezone
import secrets
from fastapi.responses import RedirectResponse

load_dotenv()

app=FastAPI()

templates=Jinja2Templates(directory='templates')

from starlette.middleware.sessions import SessionMiddleware

app.add_middleware(
    SessionMiddleware,
    secret_key=secrets.token_urlsafe(32),
    max_age=60
)


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


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
def home(request : Request ):
    return templates.TemplateResponse(request=request , name="login.html")

@app.get('/register')
def register(request : Request ):
    return templates.TemplateResponse(request=request  , name="register.html")


@app.get('/main')
def main1(request: Request):

    user_id = request.session.get("user_id")

    if not user_id:
        return RedirectResponse(url='/', status_code=303)

    return templates.TemplateResponse(
        request=request,
        name='main.html'
    )


@app.post('/main')
def main2(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='main.html'
    )


@app.post('/login')
async def login(
    request: Request,
    db: Annotated[Session, Depends(get_db)]):
    form = await request.form()

    email = form['email']
    pswd = form['pswd']

    verify = db.query(User).filter(User.email == email).first()

    if not verify:
        raise HTTPException(
            status_code=401,
            detail='Invalid Email'
        )

    if verify.password !=pswd:
        raise HTTPException(
            status_code=401,
            detail='Invalid Password'
        )

    # Generate the ID
    request.session['user_id']=verify.id
    request.session['email']=verify.email
    request.session['logged_at']=datetime.now(timezone.utc).isoformat()

    return RedirectResponse(url='/main')

