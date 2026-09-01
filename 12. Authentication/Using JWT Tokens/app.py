from fastapi import FastAPI,Request,Depends,HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from typing import Annotated
from database import SessionLocal,Customers,Session
from msg import send_messages
from services import hash_password,check_password,JWTtokens
from models import UserIn,Token
from jose import JWTError



app=FastAPI(title='JWT Token Authentication',summary="Applying authentication using Bearer tokens without using sessions and cookies")


# templates=Jinja2Templates(directory='templates')

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()




oauth2_scheme=OAuth2PasswordBearer(tokenUrl='/login')

# @app.get('/')
# def home(request:Request):
#     return templates.TemplateResponse(request=request,name='login.html')

@app.post('/login')
async def login(db:Annotated[Session , Depends(get_db)],form_data:OAuth2PasswordRequestForm=Depends()) ->Token:
    username=form_data.username
    password=form_data.password
    jwt_token=JWTtokens()
    data= db.query(Customers).filter(Customers.email==username).first()
    if data and check_password(password,data.hash_password):
        token=jwt_token.encode(username=username)
        return token

    raise HTTPException(status_code=401,detail="Username or Password is incorrect")


@app.get('/home')
def home(token:Annotated[str,Depends(oauth2_scheme)],db:Annotated[Session,Depends(get_db)]):
    jwt_token=JWTtokens()
    try:
        username=jwt_token.decode(token)
        data=db.query(Customers).filter(Customers.email==username).first()
        if data:
            return "Success"
        raise HTTPException(status_code=401,detail="User doesnt exist")
    except JWTError:
        raise HTTPException(status_code=502,detail='Not Authenticated')


    
            

