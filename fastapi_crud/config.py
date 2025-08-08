from pydantic_settings import BaseSettings

class settings(BaseSettings):
    db_uri: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    
    class Config:
        env_file = ".env"
settings =settings()