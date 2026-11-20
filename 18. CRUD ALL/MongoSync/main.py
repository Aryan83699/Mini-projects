from fastapi import FastAPI,HTTPException,Depends,Path
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from db.db import get_db,client
from typing import Annotated,List
import json
from bson import json_util,ObjectId
from schemas import *


@asynccontextmanager
async def lifespan(app:FastAPI):
    try:
        client.admin.command("ping")
        collection=client["task_db"]
        collection["students"].insert_one({"name":"Aryan Singh","email":"aryan@gmail.com","location":"India","courses":["c","cpp","java","py"]})
        yield
    finally:
        collection["students"].delete_many({})
        client.close()






app=FastAPI(title="CRUD Using Mongo Synchoronous Client ",version="1.0.0",lifespan=lifespan)





@app.get('/')
def home():
    return {"message":"MongoDB Synchronous CRUD "}




@app.get('/allStudents',response_model=List[AllStudentsRes])
def get_students(db=Depends(get_db)):
    results = list(db.find({}))
    return JSONResponse(
        content=json.loads(json_util.dumps(results))
    )

@app.get('/getStudID/{id}')
def get_stud_by_id(id:Annotated[str,Path()],db=Depends(get_db)):
    results=db.find_one({"_id":ObjectId(id)})

    # print(results)
    if not results:
        return HTTPException(status_code=404,detail={"message":"Student not found"})

    return JSONResponse(
        content=json.loads(json_util.dumps(results))
    )