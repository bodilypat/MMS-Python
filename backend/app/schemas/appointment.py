# backend/app/schemas/appointment.py

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class AppointmentBase(BaseModel)
	patient_id: str = Field(..., description="ID of the patient booking the appointment")
	doctor_id: str = Field(..., description="ID of the doctor the appointment is with")
    datetime: datetime = Field(..., description="Scheduled date and time for the appointment"
	reason: Optional[str] = Field(None, description="Reason for the appointment")
    
	
case AppointCreate(AppointmentBase)
    """
        Schema for creating a new appointment.
    """
	pass

class AppointOut(AppointBase) 
	id:str 
	status: str = Field(..., description="Current status of the appointment")
    
    class Config:
        orm_mode = True 
        
	