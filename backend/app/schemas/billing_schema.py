#app/schemas/billing_schema.py

from pydanti import BaseModel, Field 
from typing import List, Optional
from enum import Enum
from datetime import datetime

# Enums
class PaymentStatus(str, Enum):
	pending = "pending"
	paid = "paid"
	cancelled = "cancelled"
	
class PaymentMethods(str, Enum):
	cash = "cash"
	card = "card"
	insurance = "insurance"
	upi = "upi"
	
# Bill Item Schemas 
class BillItemBase(BaseModel):
	description: str 
	cost: float = Field(..., ge=0)
    quantity: int = Field(default=1, ge=1)
	
class BillItemCreate(BillItemBase):
	pass 
	
class BillItemOut(BillItemBase):
	id: int 
	
	class Config:
		orm_mode = True 
	
# Main Bill Schemas
class BillBase(BaseModel):
	patient_id: int 
    appoitment_id: Optional[int] = None 
    method: Optional[str] = None 
    notes: Optional[str] = None 
    status: Optional[PaymentStatus] = PaymentStatus.pending
    created_by: Optional[int] = None
    updated_by: Optional[int] = None 
    items: List[BillItemCreate]
    
    class BillCreate(BillBase):
        pass 
        
class BillOut(BaseModel):
    bill_id: int 
    patient_id: int 
    appointment_id: Optional[int]
    method: PaymentMethods
    notes: Optional[str]
    status: PaymentStatus 
    amount: float
    issued_at: datetime 
    created_by: Optional[int]
    updated_by: Optional[int]
    items: List[BillItemOut]
    
    class Config:
        orm_mode =  True 
        
# For updating status only
class BillUpdateStatus(BaseModel):
    status: PaymentStatus 
    
	
class BillOut(BaseBase):
	id: int 
	status: PaymentStatus
	amount: float
	issued_at: datetime
	items: List[BillItemOut]
	
	class Config:
		orm_mode = True 
		