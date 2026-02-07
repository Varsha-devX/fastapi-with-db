from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()


base=declarative_base()

DATABASE_URL = os.getenv("DATABASE_URL")
print("DATABASE_URL", DATABASE_URL)

engine = create_engine(DATABASE_URL,connect_args={"check_same_thread":False})

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()