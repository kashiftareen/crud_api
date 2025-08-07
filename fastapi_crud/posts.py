from fastapi import APIRouter,Depends,status,Response
from sqlalchemy.orm import Session
from typing import List
from .database import get_db
from . import models,schema

router = APIRouter(
    prefix="/post",
    tags=['POSTS']
    )

# To create a post in data base using ORM Sqlalchemy
@router.post("/",status_code=status.HTTP_201_CREATED
             ,response_model=schema.response_of_createpost)
def create_post(post_data:schema.create_post,db:Session=Depends(get_db)):
    post = models.Post(**post_data.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


# to get all posts from database
@router.get("/")
def get_posts(db:Session=Depends(get_db)):
    posts=db.query(models.Post).all()
    return posts
