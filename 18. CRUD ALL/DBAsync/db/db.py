from sqlalchemy.ext.asyncio import async_sessionmaker,AsyncSession,create_async_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os

load_dotenv()

engine=create_async_engine(os.getenv("PGASYNC"),echo=True,pool_size=5,max_overflow=7)

AsyncSessionLocal=async_sessionmaker(bind=engine,autoflush=False,expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def db_init():
    async with engine.begin() as conn:
        print("Connection Initiated")
        await conn.run_sync(Base.metadata.create_all)
        print("Classes created successfully at db")


async def get_db():
    db=AsyncSessionLocal() 
    try:
        yield db

    finally:
        db.commit()
