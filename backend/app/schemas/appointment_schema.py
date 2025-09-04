# backend/app/schemas/appointment_schema.py

from typing import Optional
from datetime import datetime 
from pydantic import BaseModel, Field, validator 
from enum import Enum

# Enum
class AppointmentStatus(str, Enum)
    scheduled = "scheduled"
    completed = "completed"
    cancelled = "cancelled"
    no_show = "no_show"
    
    
class AppointmentType(str, Enum)
    consulation = "Consulation"
    follow_up = "Follow-up"
    surgery = "Surgery"
    lab_test = "Lab Test"
    emergency = "Emergency" 
    
# Base schema
class AppointmentBase(BaseModel):
	patient_id: int
	doctor_id: Optional[int] = None
	appointment_date: datetime 
	check_in_time: Optional[datetime] = None 
	check_out_time: Optional[datetime] = None 
	reason_for_visit: str = Field(..., max_length=255)   
	appointment_type: AppointmentType = AppointmentType.consulation
	status: AppointmentStatus = AppointmentStatus.scheduled
	duration_minutes: Optional[int] = Field(None, gt=0)
	notes: Optional[str] = None 
	created_by: Optional[int] = None 
	updated_by: Optional[int] = None 
	
	@validator('check_out_time')
	def validate_check_out(cls, v, values):
        check_in = values.get('check_in_time')
        if v and check_in and v < check_in:
            raise ValueError('check_out_time must be after check_in_time')
        return v
        
class AppointmentCreate(AppointmentBase):
        pass
     
# Update schema     
class AppointmentUpdate(BaseModel):
    appointment_time: Optional[datetime] = None
    check_in_time: Optionl[datetime] = None 
    check_out_time: Optional[datetime] = None 
    reason_for_visit: Optional[str] = Field(None, max_length=255)
        
    appointment_type: Optional[AppointType] = None
    status: Optional[AppointmentStatus] = None 
        
    duration_minutes: Optional[int] = Field(None, ge=0)
    notes: Optional[str] = None
    updated_by: Optional[int] = None 
    
    @validate('check_out_time')
    def validate_check_out('check_in_time')
    if v and check_in and v < check_in:
        raise ValueError('check_out_time must be after check_in_time')
    return v
        
class AppointmentOut(AppointmentBase):
    id: int
    created_at: Optiona[datetime] = None
    created_at: Optional[datetime] = None    
    
    class Config:
        orm_mode = True 
   