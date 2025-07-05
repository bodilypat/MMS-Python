# backend/app/schemas/appointment.py

from pydantic import BaseModel
from typing import Optional

class AppointmentBase(BaseModel)
	patient_id: str
	doctor_id: str
	datetime: str
	reason: Optional[str]
	
case AppointCreate(AppointmentBase)
	pass

class AppointOut(AppointBase) 
	id:str 
	status: str 
	