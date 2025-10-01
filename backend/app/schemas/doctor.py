#app/schemas/doctor.py

from pydantic import BaseModel, EmailStr, Field
from typing import Optional 
from datetime import date 
from enum import Enum 

#ENUMS
class GenderEnum(str, Enum):
    male = "male"
    female = "female"
    other = "other"

class DoctorStatusEnum(str, Enum):
    active = "Active"
    inactive = "inactive"
    retired = "retired"
    on_leave = "on_leave"

# BASE SCHEMA 
class DoctorBase(BaseModel):
    first_name: str = Field(..., max_length=100, description="Doctor's first name")
    last_name: str = Field(..., max_length=100, description="Doctor's last name")
    specialization: str = Field(..., max_length=100, description="Doctor's specialization or field")
    department: Optional[str] = Field(None, max_length=100, description="Department or unit")
    phone_number: str = Field(..., min_length=7, max_length=20, description="Doctor's contact number")
    birthdate: Optional[date] = None
    gender: GenderEnum = GenderEnum.other 
    email: Optional[EmailStr] = Field(None, max_length=150)
    address: Optional[str] = Field(None, max_length=255)
    status: DoctorStatusEnum = DoctorStatusEnum.active 
    hire_date: Optional[date] = None 
    note: Optional[str] = Field(None, max_length=1000)

# CREATE 
class DoctorCreate(DoctorBase):
    created_by: Optional[int] = None 
    updated_by: Optional[int] = None 

# UPDATE 
class DoctorUpdate(BaseModel):
    first_name: Optional[str] = Field(None, max_length=100)
    last_name: Optional[str] = Field(None, max_length=100)
    specialization: Optional[str] = Field(None, max_length=100)
    department: Optional[str] = Field(None, max_length=100)
    email: Optional[str] = Field(None, max_length=150)
    phone_number: Optional[str] = Field(None, min_length=7, max_length=20)
    birthdate: Optional[date] = None 
    gender: Optional[GenderEnum] = None 
    address: Optional[str] = Field(None, max_length=255)
    status: Optional[DoctorStatusEnum] = None
    hire_date: Optional[date] = None 
    retirement_date: Optional[date] = None 
    notes: Optional[str] = Field(None, max_length=1000)
    updated_by: Optional[int] = None

#OUTPUT
class DoctorOut(DoctorBase):
    doctor_id: int 
    created_at: Optional[date]
    updated_at: Optional[date]

    class Config:
        orm_mode = True

        


