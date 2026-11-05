from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy import select,ForeignKey,CheckConstraint
from sqlalchemy.orm import relationship,mapped_column,Mapped,DeclarativeBase
from dotenv import load_dotenv
import os

load_dotenv()

url=os.getenv("PGASYNC")

class Base(DeclarativeBase):
    pass

async_engine=create_async_engine(url=url,pool_size=5,max_overflow=8,echo=True)
SessionLocal=async_sessionmaker(bind=async_engine,expire_on_commit=False,autoflush=False)

async def init_db():
    with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all())


async def get_db():
    with SessionLocal() as session:
        yield session
        

