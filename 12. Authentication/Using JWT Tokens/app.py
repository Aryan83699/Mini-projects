from fastapi import FastAPI,Request,Depends,Form
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from typing import Annotated
from database import SessionLocal,Customers
from msg import send_messages


app=FastAPI(title='JWT Token Authentication',summary="Applying authentication using Bearer tokens without using sessions and cookies")


templates=Jinja2Templates(directory='templates')


oauth2_scheme=OAuth2PasswordBearer(tokenUrl='/login')

@app.get('/login')
def login():
    return {'success'}

@app.get('/register')
def register(request:Request):
    return templates.TemplateResponse(name='register.html',request=request)

@app.post('/register')
def register2(request:Request,form_data:OAuth2PasswordRequestForm=Depends()):
    return {form_data.username,form_data.password}

