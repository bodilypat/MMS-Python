#app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

#-----------------------------------
# Database Engine 
#-----------------------------------
DATABASE-URL = settings.DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=False # set True for SQL query Logs (dev only))
)

#-----------------------------------
# Database Session Local
#-----------------------------------
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)


#-----------------------------------
# Base class for models
#-----------------------------------
Base = declarative_base()

#-----------------------------------
# Dependency for FastAPI routes
#-----------------------------------
def get_db():
    """ 
    Yield a database session for FastAPI routes.
     Closes the session after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
