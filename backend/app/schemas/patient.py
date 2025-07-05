# backend/app/schemas/patient.py

from pydantic import BaseModel 
from typing import Optional, List

class PatientBase(BaseModel)
	name: str
	dob: str
	gender: str
	phone: str 

class PatientCreate(PatientBase):
	medical_history: Optional[List[str]] = []
	
class PatientOut(PatientBase):
	medical_history: Optional[List[str]] = [] 
	
	