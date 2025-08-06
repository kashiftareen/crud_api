from fastapi import FastAPI
import uvicorn



app = FastAPI()


def start ():
    uvicorn.run("fastapi_crud.main:app",host="127.0.0.1",port=5656,reload=True)