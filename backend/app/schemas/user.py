# backend/app/schemas/user.py

from pydantic import BaseModel, EmailStr 
from typing import Optional, Literal

class UserBase(BaseModel)
	email: EmailStr
	name: str
	
class UserCreate(UserBase)
	password: str
	role: Literal["admin", "doctor","patient"]
	
class UserOut(UserBase)
	id: str 
	role: str
class UserLogin(BaseModel)
	email: EmailStr
	password: str 
	
	