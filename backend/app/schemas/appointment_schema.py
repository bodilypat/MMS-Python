# backend/app/schemas/appointment_schema.py

from typing import Optional, Literal
from datetime import datetime 
from pydantic import BaseModel, Field, validator 

class AppointmentBase(BaseModel):
	patient_id: int
	doctor_id: Optional[int] = None
	appointment_date: datetime 
	check_in_time: Optional[datetime] = None 
	check_out_time: Optional[datetime] = None 
	reason_for_visit: str = Field(..., max_length=255)
    
	appointment_type: Literal['Consultation', 'Follow-up', 'Surgery', 'Lab Test', 'Emergency'] = 'Consultation'
	status: Literal["scheduled', 'Checked-In', 'Cancelled', 'No-Show' ] = 'Scheduled'
    
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
        
    class AppointmentUpdate(BaseModel):
        appointment_date: Optional[datetime] = None
        check_in_time: Optionl[datetime] = None 
        check_out_time: Optional[datetime] = None 
        reason_for_visit: Optional[str] = Field(None, max_length=255)
        
        appointment_type: Optional[Literal['Consulation', 'Follow-up', 'Surgery', 'Lab Test', 'Emergency']] = None
        status: Optional[Literal['Scheduled', 'Checked-In', 'Cancelled', 'No-show']] = None 
        
        duration_minutes: Optional[int] = Field(None, ge=0)
        notes: Optional[str] = None
        updated_by: Optional[int] = None 
        
    class AppointmentInDB(appointmentBase):
        appointment_id: int
        created_at: datetime 
        updated_at: datetime 
    
    class config:
        orm_mode: True 
        
    class AppointmentOut(AppointmentInDB):
        pass 
        
        