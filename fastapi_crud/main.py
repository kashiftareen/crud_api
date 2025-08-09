from fastapi import FastAPI
from . import models,database,posts,user,authentication
import uvicorn


app = FastAPI()

app.include_router(posts.router)
app.include_router(user.router)
app.include_router(authentication.router)

# Add function to create database tables from SQLAlchemy models
def create_tables():
    models.base.metadata.create_all(bind=database.engine)



def start ():
    create_tables()
    uvicorn.run("fastapi_crud.main:app",host="127.0.0.1",port=9090,reload=True)