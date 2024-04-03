from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import config

_db_url = config['DATABASE_URL']
_engine = create_engine(
    _db_url,
    connect_args=_db_url
    .startswith('sqlite://') and {'check_same_thread': False},
)
session = sessionmaker(autocommit=False, autoflush=False, bind=_engine)
Base = declarative_base()
