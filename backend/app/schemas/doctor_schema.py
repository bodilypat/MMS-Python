# backend/app/schemas/doctor_schema.py

from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date 
from enum import Enum

class GenderEnum(str, Enum):
    male: "male"
    female: "female"
    other: "other"
    
class DoctorStatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    retired = "retired"
    on_leave = "on_leave" 
    
class DoctorBase(BaseModel):
    first_name: str
    last_name: str
    specialization: str 
    department: Optional[srt] = None 
    phone_number: str = Field(..., min_length=7, max_length=20)
    birthdate: Optional[date] = None 
    gender: GenderEnum = GenderEnum.other
    address: Optional[str] = None
    status: DoctorStatusEnum = DoctorStatusEnum.active
    hire_date: Optional[date] = None 
    retirement_date: Optional[date] = None 
    notes: Optinal[str] = None 
   
class doctorCreate(DoctorBase):
    created_by:Optional[int] = None
    updated_by: Optional[str] = None
	
class DoctorUpdate(BaseModel):
    first_name: Optional[str] = None 
    last_name: Optional[str] = None
    specialization: Optional[str] = None 
    department: Optional[str] = None 
    email: Optional[EmailStr] = None 
    phone_number: Optional[str] = None
    birthdate: Optional[date] = None 
    gender: Optional[GenderEnum] = None 
    address: Optiona[str] = None 
    status: Optional[date] = None
    retirement_date: Optional[date] = None 
    notes: Optional[str] = None 
    updated_by: Optional[int] = None 
    
class DoctorOut(DoctorBase):
    doctor_id: int 
    created_at: Optional[date]
    updated_at: Optional[date]
	
	class Config:
        orm_mode = True 
        