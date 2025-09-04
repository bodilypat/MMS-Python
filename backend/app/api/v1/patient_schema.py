# backend/app/schemas/patient_schema.py

from pydantic import BaseModel, EmailStr, field
from typing import Optional
from datetime import date, datetime
from enum import Enum

class GenderEnum(str, Enum):
    male = "male"
    female = "female"
    other = "other"
    
class PatientStatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    deceased = "deceased"
   
class PatientBase(BaseModel):
	first_name: str 
    last_name: str
    date_of_birth: date
    gender: GenderEnum
    phone_number: str = Field(..., min_length=7, max_length=20)
    email: Optional[EmailStr] = None 
    address: Optional[str] = None 
    primary_care_physical: Optional[str] = None
    medical_history: Optional[str] = None 
    allergies: Optional[str] = None
    status: Optional[PatientStatusEnum] = PatientStatusEnum.active 
	
class PatientCreate(PatientBase):
	pass

class PatientUpdate(BaseModel):
    first_name: Optional[str] = None 
    last_name: Optional[str] = None
    date_of_birth = Optional[date] = None 
    gender: Optional[GenderEnum] = None
    phone_number: Optional[str] = None 
    email: Optional[EmailStr] = None 
    address: Optional[str] = None 
    primary_care_physical: Optional[str] = None 
    medical_history: Optional[str] = None 
    allergies: Optional[str] = None
    status: Optional[PatientStatusEnum] = None
    
	
class PatientOut(PatientBase):
	id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    
	class Config:
		orm_mode = True 
		