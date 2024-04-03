from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import config


SQLALCHEMY_DATABASE_URL = config['DATABASE_URL']

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args=SQLALCHEMY_DATABASE_URL.startswith(
        'sqlite') and {"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
