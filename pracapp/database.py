from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL: str = "sqlite:///./pracapp/app.db"  # Uncomment for non testing
# SQLALCHEMY_DATABASE_URL: str = "sqlite:///test_app.db"  # Used for testing

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
