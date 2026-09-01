from sqlalchemy.orm import mapped_column,Mapped,DeclarativeBase,sessionmaker,Session
from sqlalchemy import create_engine,Integer,Date,String
from dotenv import load_dotenv
from datetime import datetime
import os


load_dotenv()



URL=os.getenv("DB_URL")

engine=create_engine(URL)

SessionLocal=sessionmaker(bind=engine,expire_on_commit=False)

class Base(DeclarativeBase):
    pass

class Customers(Base):
    __tablename__="customers"

    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    email:Mapped[str]=mapped_column(String(255),nullable=False,unique=True)
    hash_password:Mapped[str]=mapped_column(String(255),nullable=False)
    token:Mapped[str]=mapped_column(String(255),nullable=True)
    role:Mapped[str]=mapped_column(String(255),default='user')
    date:Mapped[str]=mapped_column(Date,default=datetime.now())

Base.metadata.create_all(engine)



with SessionLocal() as session:
    data=session.query(Customers).first()
    if data:
        pass
        session.close()
    else:
        session.add(
            Customers(id=2005,email='aryansingha887@gmail.com',role='admin',hash_password='$2b$12$QFXI0rpAaz411vWj53sTiOca6MtOBlvq2R7Pf1ZrIp3I5WVXIUMFG')
        )
        session.commit()
        session.close()
