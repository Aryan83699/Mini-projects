from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()


mongo_url=os.getenv("MONGOSYNC")

client=MongoClient(mongo_url)


def get_db():
    database=client["task_db"]
    db=database["students"]
    return db

print(type(client))
