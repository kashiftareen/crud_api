from fastapi import APIRouter,Depends,status,Response,HTTPException
from sqlalchemy.orm import Session
from typing import List
from .database import get_db
from . import models,schema,oauth2

# Create a router instance with a prefix for all post-related endpoints
router = APIRouter(
    prefix="/post",
    tags=['POSTS']
    )

# ----------------------------- CREATE POST
@router.post("/",status_code=status.HTTP_201_CREATED
             ,response_model=schema.Response_Of_Create_Post)
def create_post(post_data:schema.Create_Post
                ,db:Session=Depends(get_db),
                crruent_user:schema.token_data=Depends(oauth2.get_crruent_user)):
    post = models.Post(**post_data.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


# ----------------------------- GET ALL POSTS
@router.get("/",status_code=status.HTTP_201_CREATED,response_model=list[schema.Response])
def get_posts(db:Session=Depends(get_db),
              crruent_user:schema.token_data=Depends(oauth2.get_crruent_user)):
    posts=db.query(models.Post).all()
    return posts

# ----------------------------- GET POST BY ID 
@router.get("/{id}", response_model=schema.Response_By_Id, status_code=status.HTTP_200_OK)
def get_post_by_id(id: int, db: Session = Depends(get_db),
                   crruent_user:schema.token_data=Depends(oauth2.get_crruent_user)):
    
    post = db.query(models.Post).filter(models.Post.id == id).first()
    # If post not found, raise 404 error
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {id} was not found."
        )

    return post

# ----------------------------- DELETE POST
@router.delete("/{id}",status_code=status.HTTP_200_OK)
def delete_post(id:int,db:Session=Depends(get_db),
                crruent_user:schema.token_data=Depends(oauth2.get_crruent_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with{id} not found"
        )
    post_query.delete(synchronize_session=False)
    db.commit()
    return {"message": f"Post with id {id} deleted successfully"}

# ----------------------------- UPDATE POST
@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=schema.Update_Respons)
def update_post(id: int, newpost: schema.new_post_data, db: Session = Depends(get_db),
                crruent_user:schema.token_data=Depends(oauth2.get_crruent_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=404, detail=f"Post with ID {id} not found")

    post_query.update(newpost.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()  


