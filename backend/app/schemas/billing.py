#backend/app/schemas/billing.py

from pydantic import BaseModel
from typing import Optional, Literal
from datetime imprt datetime

class InvoiceBase(BaseModel):
	patient_id: str
	appointment_id: str
	amount: str
	status: Literal["unpaid","paid","cancelled"]
	
class InvoiceCreate(InvoiceBase):
	pass
	
class InvoiceUpdate(BaseModel):
	amount: Optional[float]
	status: Optional[str]
	
class InvoiceOut(InvoiceBase):
	id: str
	issued_date: datetime
	
	class Config:
		orm_mode= True 
		