#app/schemas/patient.py

from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, datetime 
from enum import Enum

# ENUM
class GenderEnum(str, Enum):
    male = "male"
    female= "female"
    other = "other"

class PatientStatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    deceased = "deceased"

# BASE SCHEM 
class PatientBase(BaseModel):
    first_name: str = Field(..., max_length=100, description="Patient's first name")
    last_name: str = Field(..., max_length=100, description="Patient's last name")
    date_of_birth: date 
    gender: GenderEnum
    phone_number: str = Field(..., min_length=7, max_length=20)
    email: Optional[EmailStr] = None 
    address: Optional[str] = Field(None, max_length=255)
    primary_care_physician: Optional[str] = Field(None, max_length=100)
    medical_history: Optional[str] = None 
    allergies: Optional[str] = None
    status: Optional[PatientStatusEnum] = PatientStatusEnum.active

# CREATE 

class PatientCreate(PatientBase):
    pass 

# UPDATE 
class PatientUpdate(BaseModel):
    first_name: Optional[str] = Field(None, max_length=100)
    last_name: Optional[str] = Field(None, max_length=100)
    date_of_birth: Optional[date] = None 
    gender: Optional[GenderEnum]
    phone_number: Optional[str] =Field(None, min_length=7, max_length=20)
    email: Optional[EmailStr] = None 
    address: Optional[str] = Field(None, max_length=255)
    primary_care_physician: Optional[str] = Field(None, max_length=100)
    medical_history: Optional[str] = None 
    status: Optional[PatientStatusEnum] = None

# OUTPUT SCHEMA 
class PatientOut(PatientBase):
    patient_id: int
    created_at: Optional[datetime] = None 
    updated_at: Optional[datetime] = None 

    class Config:
        orm_mode = True 

        