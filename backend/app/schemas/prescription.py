#app/schemas/prescription.py

from pydantic import BaseModel, Field 
from typing import Optional
from datetime import date, datetime 
from enum import Enum

# ENUMS 
class UnitEnum(str, Enum):
    mg = 'mg'
    ml = 'ml'
    units = 'untis'
    tablet = 'tablet'
    capsule = 'capsule'
    drop = 'drop'
    patch = 'patch'

class RouteEnum(str, Enum):
    oral = 'Oral'
    iv = 'IV' 
    IM = 'IM'
    topical =  'Topical'
    subcutaneous = 'Subcutaneous'
    nasal = 'Nasal'
    other = 'Other'

class StatusEnum(str, Enum):
    active = 'Active'
    completed = 'Campleted'
    expired = 'Expired'
    cancelled = 'Cancelled'

# BASE SCHEMA 
class PrescriptionBase(BaseModel):
    record_id: int 
    patient_id: int 
    doctor_id: int 
    appointment_id: Optional[int] = None 

    medical_name: str = Field(..., max_length=150)
    generic_name: Optional[str] = Field(None, max_length=150)
    dosage: str = Field(..., max_length=100)
    unit: UnitEnum = UnitEnum.mg 
    frequency: str = Field(..., max_length=100)
    route: RouteEnum = RouteEnum.oral
    duration_days: Optional[int] = None 
    start_date: date
    end_date: Optional[date] = None 

    instructions: Optional[str] = None 
    notes: Optional[str] = None 
    refill_count: Optional[int] = 0
    status: StatusEnum = StatusEnum.active 

    created_by: Optional[int] = None 
    updated_by: Optional[int] = None 

# CREATE SCHEMA 
class PrescriptionCreate(PrescriptionBase):
    pass 

# UPDATE SCHEMAS 
class PrescriptionUpdate(BaseModel):
    medical_name: Optional[str] = Field(None, max_length=150)
    generic_name: Optional[str] = Field(None, max_lenth=150)
    dosage: Optional[str] = Field(None, max_length=100)
    unit: Optional[int] = None 
    frequency: Optional[str] = Field(None, max_length=100)
    route: Optional[RouteEnum] = None 
    duration_days: Optional[int] = None 
    start_date: Optional[date] = None 
    end_date: Optional[date] = None 

    instruction: Optional[str] = None 
    notes: Optional[str] = None
    refill_count: Optional[int] = None 
    status: Optional[StatusEnum] = None 
    updated_by: Optional[int] = None 

    class Config:
        orm_mode = True 

# OUTPUT SCHEMA
class PrescriptionOut(PrescriptionBase):
    prescription_id: int
    created_at: datetime
    updated_at: datetime

    class Config: 
        orm_mode = True