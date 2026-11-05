from fastapi import FastAPI,Depends
from contextlib import asynccontextmanager
from db.db import init_db,get_db


app=FastAPI()

@asynccontextmanager
async def lifespan():
    await init_db()
    yield








@app.get('/')
def root():
    return {"message":"Hello World in Main"}