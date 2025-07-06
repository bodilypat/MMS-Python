# backend/app/schemas/appointment.py

from pydantic import BaseModel, Field, validator
from typing import Optional, Literal
from datetime import datetime
from enum import Enum

class AppointmentBase(str, Enum)
    Consultation = "Consulation"
    FollowUp = "Follow-up"
    Surgery = "Surgery"
    LabTest = "Lab Test"
    Emergency = "Emergency"
    
class AppointmentStatus(str, Enum)
    Scheduled = "Scheduled"
    CheckedIn = "Checked-In"
    Cancelled = "Cancelled"
    NoShow = "No-Show" 
    
class AppointmentBase(BaseModel):
    patient_id: str = Field(..., description="ID of the patient")
    doctor_id: str = Field(..., description="ID of the doctor")
    appointment_date: datetime = Field(..., description="Date and time of the appointment")
    reason_for_visit: str = Field(..., max_lenght=255, description="Reason for the visit")
    appointment_type: Appointment_type = Field(default=AppointmentType.Consultation)
    status: AppointmentStatus = Field(default=AppointmentStatus.Scheduled)
    duration_minutes: Optional[int] = Field(None, gt=0, description="Duration in minutes")
    notes: Optional[str] = Field(None, description="Additional notes")
    
@validator("appointment_date")
    def validate_future_date(cls, value):
        if value < datetime.utcnow():
            raise ValueError("Appointment date must be in the future")
           return value 
           
class AppointmentCreate(AppointmentBase)
    """
        Used when creating a new appointment
    """
    pass 

class AppointmentUpdate(BaseModel):
    appointment_date: Optional[datetime]
    status: Optional[AppointmentStatus]
    check_in_time: Optional[datetime]
    duration_minutes: Optional[int] = Field(None, gt=0)
    notes: Optional[str]
    
    @validator("appointment_date")
    def validate_date(cls, value)
        if value and value < datetime.utcnow():
            raise ValueError("Appointment date must be in the future")
        return value

class AppointmentOut(AppointmentBase):
    id: str
    check_in_time: Optional[datetime]
    check_out_time: Optional[datetime]
    created_at: datetime
    updated_at: datetime 
    
class Config: 
    orm_mode = True 
	