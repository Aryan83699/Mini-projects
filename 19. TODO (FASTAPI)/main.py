from fastapi import FastAPI,Depends
from db.database import *
from contextlib import asynccontextmanager
from api.todos import todosRouter
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address
from slowapi import Limiter,_rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from limiter import limiter




# lifecycle of the app
@asynccontextmanager
async def lifespan(app:FastAPI):
    await init_db()
    yield
    await close_db()





app=FastAPI(title="TODO App",summary="TODO using FastAPI",version="1.0.0",lifespan=lifespan)

#including api routers
app.include_router(todosRouter)


# limiter=Limiter(key_func=get_remote_address)
app.state.limiter=limiter
app.add_exception_handler(RateLimitExceeded,_rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)


#home route
@app.get('/')
async def home():
    return {"status":"TODO App is running......."}




