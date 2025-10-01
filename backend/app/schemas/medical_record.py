#app/schemas/medical_record.py

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum 

# ENUM
class MedicalRecordStatus(str, Enum):
    active = "Active"
    archived = "Archived"
    inactive = "Inactive"

# BASE SCHEMA 
class MedicalRecordBase(BaseModel):
    patient_id: int 
    appointment_id: int 
    diagnosis: Optional[str] = Field(None, max_length=500)
    treatment_plan: Optional[str] = None 
    note: Optional[str] = None
    status: MedicalRecordStatus = MedicalRecordStatus.active 
    attachment: Optional[str] = Field(None, max_length=255)

    created_by: Optional[int] = None 
    updated_by: Optional[int] = None 

# CREATE SCHEMA 
class MedicalRecordCreate(MedicalRecordBase):
    pass 

#UPDATE 
class MedicalRecordUpdate(BaseModel):
    diagnosis: Optional[str] = Field(None, max_length=500)
    treatment_plan: Optional[str] = None 
    note: Optional[str] = None 
    status: Optional[MedicalRecordStatus] = None 
    attachments: Optional[str] = Field(None, max_length=255)
    updated_by: Optional[int] = None 

# RESPONSE SCHEMA 
class MedicalRecordOut(MedicalRecordBase):
    medical_record_id: int 
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True 
        