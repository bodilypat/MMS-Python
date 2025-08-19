# backend/app/schemas/medical_record_schema.py

from pydantic import BaseModel, Field 
from typing import Optional, Literal 
from datetime import datetime


# Shared field for create & update 
class MedicalRecordBase(BaseModel):
	patient_id: int
	appointment_id: int 
	diagnosis: Optional[str] = Field(None, max_length=500)
	treatment_plan: Optional[str] = None 
	note: Optional[str] = None 
	status: Literal['Active', 'Archived', 'Inactive'] = 'Active'
	attactments: Optional[str] = None
	
	created_by: Optional[int] = None 
	updated_by: Optional[int] = None 
	
# For  POST requests
class MedicalRecordCrete(MedicalRecordBase):
    pass
    
# For PATCH/PUT requests
class MedicalRecordUpdate(BaseModel):
    diagnosis: Optional[str] = Field(None, max_length=500)
    treatment_plan: Optional[str] = None
    note: Optional[str] = None 
    status: Optional[Literal['Active', 'Archived', 'Inactive']] = None 
    attactments: Optional[str] = None 
    updated_by: Optional[int] = None 
    
#For DB and API response 
class MedicalRecordInDB(MedicalRecordBase):
	record_id: int
	created_at: datetime
	updated_at: datetime
	
	class Config:
	orm_mode: True 
	