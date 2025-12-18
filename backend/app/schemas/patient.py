#app/schemas/patient.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime

#---------------------------------------
# Patient Base Schema (shared fields)
#---------------------------------------
class PatientBase(BaseModel):
    first_name: str
    last_name: str
    gender: str
    date_of_birth: date
    email: EmailStr
    phone_number: Optional[str] = None
    address: Optional[str] = None
    blood_group: Optional[str] = None
    allergies: Optional[str] = None
    emergency_contact: Optional[str] = None
    medical_history: Optional[str] = None
    current_medications: Optional[str] = None
    is_active: bool = True
    is_deleted: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

#---------------------------------------
# Patient Create Schema
#---------------------------------------
class PatientCreate(PatientBase):
    user_id: Optional[int] = None

#---------------------------------------
# Patient Update Schema details
#---------------------------------------
class PatientUpdate(PatientBase):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[date] = None
    phone_number: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    blood_group: Optional[str] = None
    allergies: Optional[str] = None
    emergency_contact: Optional[str] = None
    medical_history: Optional[str] = None
    current_medications: Optional[str] = None
    is_active: Optional[bool] = None
    is_deleted: Optional[bool] = None
    updated_at: Optional[datetime] = None
    user_id: Optional[int] = None

#---------------------------------------
# Patient Response Schema patient info
#---------------------------------------
class PatientResponse(PatientBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True


