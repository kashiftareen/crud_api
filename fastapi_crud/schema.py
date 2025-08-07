from pydantic import BaseModel,ConfigDict,EmailStr


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