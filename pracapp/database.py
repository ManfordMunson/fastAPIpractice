from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#connects to sqlite db 
SQLALCHEMY_DATABASE_URL = "sqlite:///./pracapp/app.db"

#connect args only needed for sqlite db
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Classes inheirit this to create db models and classes
Base = declarative_base()