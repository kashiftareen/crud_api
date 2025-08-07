from pydantic import BaseModel
#Add Pydantic model 'create_post' 
class create_post(BaseModel):

    title:str
    content:str

class response_of_createpost(create_post):
    id:int
