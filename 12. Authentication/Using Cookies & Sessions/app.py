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
from fastapi.staticfiles import StaticFiles




load_dotenv()

app=FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


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


def send_otp(user_email,request):
    msg=EmailMessage()
    user_otp=str(round(random.random()*10000))
    request.session['user_otp']=user_otp
    msg['Subject']='Email Verification'
    msg['From']=os.getenv('EMAIL_ID')
    msg['To']=user_email
    msg.set_content(f"Your OTP is {user_otp}")



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


@app.post('/register')
async def register_verify(request : Request):
    form = await request.form()
    email=form['email']
    pswd1=form['ps_text']
    pswd2=form['pswd']

    

    if pswd1 != pswd2 :
        return templates.TemplateResponse(request=request , name='register.html' ,context={'message':'Password doesnt match !!!'})

    request.session['email']=email
    request.session['password']=pswd2
    request.session['purpose']='register'

    send_otp(email,request)
    return RedirectResponse(url='/otp',status_code=303)

    


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

    if not verify or verify.password != pswd:
        return templates.TemplateResponse(
            request=request,
            name='login.html',
            context={
                'message': 'Invalid Email or Password'
            }
        )


    # Generate the ID
    request.session['user_id']=verify.id
    request.session['email']=verify.email
    request.session['logged_at']=datetime.now(timezone.utc).isoformat()

    return RedirectResponse(url='/main')


@app.get('/otp')
def otp(request : Request):
    return templates.TemplateResponse(request=request,name='otp.html')


@app.post('/verify-otp')
async def verify_otp(request:Request , db:Annotated[Session,Depends(get_db)]):
    temp_otp=request.session.get('user_otp')
    form = await request.form()
    get_otp=form['otp']
    

    if temp_otp != get_otp:
        return templates.TemplateResponse(request=request , name='register.html' ,context={'message':'Incorrect OTP !!!'})

    if request.session.get('purpose')=='forgotten':
        return RedirectResponse(url='/forgot-otp',status_code=303)

    request.session['user_id']=random.random()*1000

    db.add(
        User(id=request.session.get('user_id'),email=request.session.get('email'),password=request.session.get('password'),role='user')
    )
    db.commit()

    return templates.TemplateResponse(request=request , name='main.html')

@app.post('/forgot')
async def forgot(request:Request , db:Annotated[Session,Depends(get_db)]):
    form=await request.form()
    email=form['email']
    password=form['pswd']

    user=db.query(User.email==email).first()

    if not user:
        return templates.TemplateResponse(request=request,name='register.html',context={'message':'User not found'})

    request.session['email']=email
    request.session['password']=password 
    request.session['purpose']='forgotten'
    send_otp(email,request)
    return RedirectResponse(url='/otp',status_code=303)


@app.get('/forgot-otp')
async def forgot_otp(request : Request , db:Annotated[Session,Depends(get_db)]):
    user_obj=db.query(User).filter(User.email==request.session.get('email')).first()
    user_obj.password=request.session.get('password')
    db.add(user_obj)
    db.commit()
    return templates.TemplateResponse(request=request,name='main.html')

    