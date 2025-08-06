from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings

#Create engine with connection string

sqlalchemy_database_URL=settings.db_uri
engine = create_engine(sqlalchemy_database_URL)

# Creates a new SQLAlchemy session factory with specific settings and binds it to the engine.
localsession =sessionmaker(autocommit=False,autoflush=False,bind=engine)


#dependancy to make connection with database and close it automatically
 
def get_db():
    db = localsession()
    try:
        yield db
    finally:
        db.close()


