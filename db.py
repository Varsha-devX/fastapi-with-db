from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()


Base=declarative_base()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set. Please add it to your .env file.")

engine = create_engine(DATABASE_URL)

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()