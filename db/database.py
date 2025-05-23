from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


SQLALCHEMY_DATABASE_URL = 'sqlite:///./sqlite.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()