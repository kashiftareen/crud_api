from pydantic import BaseModel,ConfigDict,EmailStr
from datetime import datetime


# reponse modele to get_all_posts
class Response(BaseModel):
    title:str
    content:str
    model_config = ConfigDict(from_attributes=True)



#Add Pydantic model 'create_post' 
class Create_Post(BaseModel):

    title:str
    content:str

class Response_Of_Create_Post(Create_Post):
    id:int
    model_config = ConfigDict(from_attributes=True)


# pydantic model to respone a single post
class Response_By_Id(Response_Of_Create_Post):

    model_config = ConfigDict(from_attributes=True)


# To update a post with its path variable
class new_post_data(BaseModel):
    title:str
    content:str
    

# response model of update_post
class Update_Respons(BaseModel):
    id:int
    title:str
    content:str
    model_config=ConfigDict(from_attributes=True)


# To create new user in database 
class Create_User(BaseModel):
    email:EmailStr
    password:str

# respones model for user
class User_out(BaseModel):
    id:int
    email:EmailStr
    model_config=ConfigDict(from_attributes=True)

class U_out(BaseModel):
    id:int
    email:EmailStr
    model_config=ConfigDict(from_attributes=True)

class token_data(BaseModel):
    id:int