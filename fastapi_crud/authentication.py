from fastapi import Depends,status,Response,APIRouter,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import Basic_auth, models,schema,utils,database

router = APIRouter(
    tags=['Authentication']
)
# Authenticates user from form data and returns a JWT access token upon successful login.
@router.post("/login",status_code=status.HTTP_200_OK)
def user_login(user_credentials:OAuth2PasswordRequestForm=Depends(),
               db:Session=Depends(database.get_db)):
               
    user = db.query(models.user).filter(models.user.email == user_credentials.username).first()
    if user == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"invalid user_credentials"
        )
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid user_credentials"
        )
    access_token = Basic_auth.create_access_token(data={"user_id":user.id})

    return {
        "access_token":access_token,
        "token_type":"bearer"
    }
    
