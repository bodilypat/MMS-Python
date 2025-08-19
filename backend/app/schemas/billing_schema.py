# backend/app/schemas/billing_schema.py

from pydantic import BaseModel
from datetime import date 

class BillingBase(BaseModel):
	patient_id: int
	appointment_id: int 
	amount: float 
	status: str
	billing_date: date 
	
class BillingCreate(BillingBase):
	pass 
	
class BillingOut(BillingBase):
	id: int 
	
	class Config: 
		orm_mode = True 
		
		