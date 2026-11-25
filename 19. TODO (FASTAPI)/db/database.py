from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine,async_sessionmaker
from sqlalchemy.orm import mapped_column,Mapped,DeclarativeBase
from sqlalchemy import String,Date,text,DateTime,func
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime,timezone
from dotenv import load_dotenv
import os
import uuid

#loading environment variables
load_dotenv()


class Base(DeclarativeBase):
    pass

class Tasks(Base):
    __tablename__="tasks"

    id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True,server_default=text("gen_random_uuid()"))
    name:Mapped[str]=mapped_column(String,unique=True,nullable=False)
    status:Mapped[str]=mapped_column(String,nullable=False)
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),nullable=False,server_default=func.now())



async_engine=create_async_engine(os.getenv("PGASYNC"),pool_size=7,echo=True,max_overflow=10)

AsyncSessionLocal=async_sessionmaker(async_engine,expire_on_commit=False,autoflush=False)


#database initiation
async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# database connection as resource
async def get_db():
    db=AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.commit()

# database connection and table closure
async def close_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


