from sqlalchemy import create_engine
from sqlalchemy.orm import (DeclarativeBase, sessionmaker)

DATABASE8_URL = "sqlite:///architect_flask.db"

engine=create_engine(DATABASE8_URL, echo=True)

## Base partage par Tous les modeles 
class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)