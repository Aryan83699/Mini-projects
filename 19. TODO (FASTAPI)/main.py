from fastapi import FastAPI,Depends
from db.database import *
from contextlib import asynccontextmanager
from api.todos import todosRouter



@asynccontextmanager
async def lifespan(app:FastAPI):
    await init_db()
    yield
    await close_db()


app=FastAPI(title="TODO App",summary="TODO using FastAPI",version="1.0.0",lifespan=lifespan)


app.include_router(todosRouter)



@app.get('/')
async def home():
    return {"status":"TODO App is running......."}




