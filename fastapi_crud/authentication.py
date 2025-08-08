from fastapi import Depends,status,Response,APIRouter,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import models,schema,utils,database,oauth2

router = APIRouter(
    tags=['Authentication']
)
# Authenticates user from form data and returns a JWT access token upon successful login.
@router.post("/login",status_code=status.HTTP_201_CREATED)
def user_login(user_credentials:OAuth2PasswordRequestForm=Depends()
               ,db:Session=Depends(database.get_db)):
    user = db.query(models.user).filter(models.user.email == user_credentials.username).first()
    if user == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
            ,detail=f"invalid user_credentials"
        )
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="invalid user_credentials"
        )
    access_tonken = oauth2.create_access_token(data={"user_id":user.id})

    return {
        "access_tonken":access_tonken,
        "token type":"bearer"
    }
    
