from pydantic_settings import BaseSettings

class settings(BaseSettings):
    db_uri :str
    
    class Config:
        env_file = ".env"
settings =settings()