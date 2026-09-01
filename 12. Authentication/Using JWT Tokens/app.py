from fastapi import FastAPI,Request,Depends,HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from typing import Annotated
from database import SessionLocal,Customers,Session
from msg import send_messages
from services import hash_password,check_password,JWTtokens
from models import UserIn,Token
from jose import JWTError
from starlette.middleware.sessions import SessionMiddleware
import os 
from dotenv import load_dotenv

app=FastAPI(title='JWT Token Authentication',summary="Applying authentication using Bearer tokens without using sessions and cookies")

load_dotenv()

app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SECRET_KEY"),
    max_age=60
)

templates=Jinja2Templates(directory='templates')

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()




oauth2_scheme=OAuth2PasswordBearer(tokenUrl='/login')

@app.get('/')
def home(request:Request):
    return templates.TemplateResponse(request=request,name='login.html')


@app.get('/register')
def register(request:Request):
    return templates.TemplateResponse(request=request,name='register.html')

@app.post('/register')
async def registerV(request:Request):
    form=await request.form()

    request.session["username"]=form['username']
    request.session["password"]=form['password']

    send_messages(form['username'],request)

    return RedirectResponse(url='/otp',status_code=303)
   

@app.get('/otp')
def otp(request:Request):
    return templates.TemplateResponse(request=request,name='otp.html')


@app.get('/main')
def main(request:Request):
    return templates.TemplateResponse(request=request ,name='main.html')

@app.post("/otp-verify")
async def otp_verify(request:Request,db:Annotated[Session,Depends(get_db)]):
    form = await request.form()
    if form["otp"]==request.session.get("OTP"):
        data=db.query(Customers).filter(Customers.email==request.session.get("username"))
        if data:
            return templates.TemplateResponse(context={"message":"User already exist"},name="login.html",request=request)
        db.add(Customers(email=request.session.get("username"),hash_password=hash_password(request.session.get("password"))))
        db.commit()
        return RedirectResponse(url='/main',status_code=303)
    return templates.TemplateResponse(request=request,name='register.html',context={'message':'Invalid OTP'})


@app.post('/login')
async def login(request:Request ,db:Annotated[Session , Depends(get_db)],form_data:OAuth2PasswordRequestForm=Depends()) ->Token:
    username=form_data.username
    password=form_data.password
    jwt_token=JWTtokens()
    data= db.query(Customers).filter(Customers.email==username).first()
    if data and check_password(password,data.hash_password):
        token=jwt_token.encode(username=username)
        response = RedirectResponse(
            url="/main",
            status_code=303
        )

        response.set_cookie(
            key="access_token",
            value=token.access_token,
            httponly=True,
            secure=False,   # True in production with HTTPS
            samesite="lax"
        )

        return response

    return templates.TemplateResponse(name='register.html',request=request,context={'message':'Invalid ID or Password'})


@app.get('/home')
def home(token:Annotated[str,Depends(oauth2_scheme)],db:Annotated[Session,Depends(get_db)],request:Request):
    jwt_token=JWTtokens()
    token = request.cookies.get("access_token")

    if not token:
        return templates.TemplateResponse(request=request,context={'message':'not authenticated'},name='register.html')
    try:

        username=jwt_token.decode(token)
        data=db.query(Customers).filter(Customers.email==username).first()
        if data:
            return "Success"
        raise HTTPException(status_code=401,detail="User doesnt exist")
    except JWTError:
        raise HTTPException(status_code=502,detail='Not Authenticated')


    
            

