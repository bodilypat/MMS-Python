# app/schemas/auth.py

from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    remember_me: bool = False

class Token(BaseModel):
    access_token: str
    refresh_token: str | None
    token_type: str = "bearer"

