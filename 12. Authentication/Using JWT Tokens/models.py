from pydantic import BaseModel,Field
from typing import Annotated

class UserIn(BaseModel):
    username:Annotated[str,Field(title='Email Id' , description="Its takes user email id")]
    password:Annotated[str,Field(title='Users password',description='Takes users plain Password')]

class Token(BaseModel):
    access_token:Annotated[str,Field(title='JWT Token',description="Encoded bearer token")]
    type:Annotated[str,Field(title='Bearer',description='Whoever holds this grants the power of Thor')]='bearer'
