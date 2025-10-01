#app/schemas/appointment.py

from pydantic import BaseModel, Field, Validator
from datetime import datetime 
from typing import Optional 
from enum import Enum 

# ENUMS 
class AppointmentStatus(str, Enum):
    scheduled = "scheduled"
    completed = "completed"
    cancelled = "cancelled"
    no_show = "no_show"

class AppointmentType(str, Enum):
    consulation = "Consulation"
    follow_up = "Follow-up"
    surgery = "Surgery"
    lab_test = "Lab Test"
    emergency = "Emergency"

# BASE SCHEMA 
class AppointmentBase(BaseModel):
    patient_id: int 
    appointment_time: datetime 
    check_in_time: Optional[datetime] = None 
    check_out_time: Optional[datetime] = None 
    reason_for_visit: str = Field(..., max_length=255)
    appointment_type: AppointmentType = AppointmentType.consulation
    status: AppointmentStatus = AppointmentStatus.scheduled
    duration_minutes: Optional[str] = Field(None, gt=0)
    notes: Optional[str] = None 
    created_by: Optional[int] = None 
    updated_by: Optional[int] = None 

    @validator('check_out_time')
    def validate_check_out(cls, v, values):
        check_in = values.get('check_in_time')
        if v and check_in and v < check_in:
            raise ValueError('check_out_time must be after check_in_time')
        return v
    
# CREATE 
class AppointmentCreate(AppointmentBase):
    pass 

#UPDATE
class AppointmentUpdate(BaseModel):
    appointment_time: Optional[datetime] = None 
    check_in_time: Optional[datetime] = None 
    check_out_time: Optional[datetime] = None 
    reason_for_visit: Optional[str] = Field(None, max_length=255)
    appointment_type: Optional[AppointmentType] = None 
    status: Optional[AppointmentStatus] = None 
    duration_minutes: Optional[int] = Field(None, ge=0)
    notes: Optional[str] = None 
    updated_by: Optional[int] = None 

    @validator('check_out_time')
    def validate_check_out(cls, v, values)
        check_in = values.get('check_in_time')
        if v and check_in and v < check_in:
            raise ValueError('check_out_time must be after check_in_time')
        return v 
    
    
