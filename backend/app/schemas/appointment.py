#app/schemas/appointment.py 

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#--------------------------------------------
# Base Appointment Schema (shared attributes)
#--------------------------------------------
class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    Appointment_datetime: datetime
    status: Optional[str] = "scheduled" # scheduled, completed, cancelled , no-show
    reason: Optional[str] = None
    note: Optional[str] = None
    
#----------------------------------------------------
# Appointment Create Schema (attributes for creation)
#----------------------------------------------------
class AppointmentCreate(AppointmentBase):
    pass

#----------------------------------------------------
# Appointment Update Schema (attributes for update)
#----------------------------------------------------
class AppointmentUpdate(AppointmentBase):
    patient_id: Optional[int] = None
    doctor_id: Optional[int] = None
    Appointment_datetime: Optional[datetime] = None
    status: Optional[str] = None
    reason: Optional[str] = None
    note: Optional[str] = None

#----------------------------------------------------
# Schema for returning Appointment information
#----------------------------------------------------
class AppointmentReturn(AppointmentBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True