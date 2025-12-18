#app/core/config.py

from pydantic import BaseSettings, Field

class Settings(BaseSettings):
#----------------------------------
# Application settings
#----------------------------------
    APP_NAME: str = "Medical Management System"
    APP_VERSION: str = "development"
    DEBUG_MODE: bool = True

#----------------------------------
# Database settings
#----------------------------------
    DB_HOST: str = Field(..., env="DB_HOST")
    DB_PORT: int = Field(..., env="DB_PORT")
    DB_USER: str = Field(..., env="DB_USER")
    DB_PASSWORD: str = Field(..., env="DB_PASSWORD")
    DB_NAME: str = Field(..., env="DB_NAME")

#----------------------------------
# Security settings
#----------------------------------
    SECRET_KEY: str = Field(
        default="chanage_this_secret_key_in",
        env="SECRET_KEY"
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

#----------------------------------
# CORS settings
#----------------------------------
    CORS_ORIGINS: list[str] = Field(
        default=["http://localhost", "http://localhost:8000"],
        env="CORS_ORIGINS"
    )

#----------------------------------
# Global settings
#----------------------------------
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


        