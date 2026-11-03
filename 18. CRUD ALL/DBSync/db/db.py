from sqlalchemy.orm import Session,sessionmaker,DeclarativeBase
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

url=os.getenv("MYSYNC")

print(url)


engine=create_engine(url=url,pool_size=5,max_overflow=8,echo=True)
SessionLocal=sessionmaker(bind=engine,autoflush=False,expire_on_commit=False)


class Base(DeclarativeBase):
    pass



async def init_db():
    with engine.connect() as temp:
        print("started")
        Base.metadata.create_all(bind=engine)
        print("executed")


def get_session():
    with SessionLocal() as session:
        yield session


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

