# backend/app/schemas/doctor.py
from typing import List, Optional 

class DoctorBase(BaseModel):
	name: str 
	specializatin: str
	email: EmailStr 
	available_days: Optional[List[str]] = []
	
class DoctorCreate(DoctorBase):
	pass

class DoctorUpdate(BaseModel):
	name: Optional[str]
	specializatin: Optional[str]
	phone: Optional[str]
	available_days: Optional[List[str]]
	
class DoctorOut(DoctorBase):
	orm_mode = True 
	
