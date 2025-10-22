#app/core/config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Medical Management System"
    app_env: str = "development"
    app_debug: bool = True 
    app_port: int = 8000

    db_host: str 
    db_port: int 
    db_name: str
    db_user: str 
    db_password: str 
    database_url: str 

    secret_key: str 
    algorithm: str 
    access_token_expire_minutes: int

    backend_cors_origins: str 

    class Config:
        env_file =".env"

    settings = Settings