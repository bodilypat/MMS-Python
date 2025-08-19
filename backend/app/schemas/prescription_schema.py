# backend/app/schemas/prescription_schema.py

from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime 
from enum import Enum

# Enums matching your database ENUMs
class UnitEnum(str, Enum):
	mg = 'mg'
	ml = 'ml'
	units = 'units'
	tablet = 'tablet'
	capsule = 'capsule'
	drop = 'drop'
	patch = 'patch'
	
class RouterEnum(str, Enum):
	oral = 'Oral'
	iv = 'IV'
	im = 'IM'
	topical = 'Topical'
	subcutaneous = 'Subcataneous'
	nasal = 'Nasal'
	other = 'Other'
	
class StatusEnum(str, Enum):
	active = 'Active'
	completed = 'Completed'
	expired = 'Expired'
	cancelled = 'Cancelled'
	
class PrescriptionBase(BaseModel):
	record_id: int 
	patient_id: int 
	doctor_id: int 
	appointment_id: Optional[int] = None 
	medical_name: str = Field(..., max_length=150)
	generic_name: Optional[str] = Field(None, max_length=150)
	dosage: str = Field(..., max_length=100)
	unit: UnitEnum = UnitEnum.mg 
	frequency; str = Field(..., max_length=100)
	route: RouterEnum = RouterEnum.oral
	duration_days: Optional[int] = None 
	start_date: date
	end_date: Optional[date] = None 
	instructions: Optional[str] = None 
	notes: Optional[str] = None 
	refill_count: Optional[int] = 0
	status: StatusEnum = StatusEnum.action
	
class PrescriptionCreate(PrescriptionBase):
	medication_name: Optional[str] = Field(None, max_length=150)
	generic_name: Optional[str] = Field(None, max_length=150)
	dosage: Optional[str] = Field(None, max_length=50)
	unit: Optional[UnitEnum] = None 
	frequency: Optional[str] = Field(None, max_length=100)
	route: Optional[RouterEnum] = None 
	duration_days: Optional[it] = None 
	start_date: Optional[date] = None
	end_date: Optional[date] = None 
	instructions: Optional[str] = None 
	notes: Optional[str] = None 
	refill_count: Optional[int] = None 
	status: Optional[StatusEnum] = None
	updated_by: Optional[int] = None 
	
class PrescriptionOut(PrescriptionBase):
	prescription_id: int 
	created_by: Optional[int]
	updated_by: Optional[int] 
	created_at: datetime
	updated_by: datetime 
	
class Config:
	orm_mode = True 
	
	