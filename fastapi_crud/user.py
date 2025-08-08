from fastapi import Depends,status,HTTPException,APIRouter,Response
from .database import get_db
from sqlalchemy.orm import Session
from . import schema,models,utils



router = APIRouter(
    tags=['users']
)

# Creates a new user with a hashed password and saves it to the database.
@router.post("/user",status_code=status.HTTP_201_CREATED,response_model=schema.User_out)
def create_user(user:schema.Create_User,db:Session=Depends(get_db)):
    user.password =utils.hash(user.password)
    new_user = models.user(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#To get single User with path variable
@router.get("/user{id}",status_code=status.HTTP_200_OK,response_model=schema.User_out)
def get_single_user(id:int,db:Session=Depends(get_db)):
    get_user = db.query(models.user).filter(models.user.id == id).first()
    if get_user == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
            ,detail=f"user with {id} not found"
        )
    return get_user