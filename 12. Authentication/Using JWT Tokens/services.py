from jose import jwt ,JWTError
from passlib.context import CryptContext
import os 
from dotenv import load_dotenv
from models import Token
from fastapi import HTTPException
from datetime import datetime , timezone , timedelta


load_dotenv()


pswd_context=CryptContext(schemes=['bcrypt'],deprecated="auto")



def hash_password(password:str) -> str:
    return pswd_context.hash(password)


def check_password(plain_pswd:str,hash_pswd:str) -> str:
    return pswd_context.verify(plain_pswd,hash_pswd)


class JWTtokens():
    def __init__(self):
        self.SECRET=os.getenv("SECRET_KEY")
        self.ALGORITHM="HS256"


    def encode(self,username) -> Token:
        token=jwt.encode({'sub':username ,'exp':datetime.now(timezone.utc)+timedelta(minutes=5)},self.SECRET,self.ALGORITHM)
        return Token(access_token=token,token_type="bearer")


    def decode(self,token):
            payload=jwt.decode(token,self.SECRET,algorithms=[self.ALGORITHM])
            username=payload.get('sub')
            return username