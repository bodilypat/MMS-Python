#app/schemas/billing_schema.py

from pydanti import BaseModel 
from typing import List, Optional
from enum import Enum
from datetime import datetime

class PaymentStatus(str, Enum):
	pending = "pending"
	paid = "paid"
	cancelled = "cancelled"
	
class PaymentMethods(str, Enum):
	cash = "cash"
	card = "card"
	insurance = "insurance"
	upi = "upi"
	
class BillItemBase(BaseModel):
	description: str 
	cost: float
	
class BillItemCreate(BillItemBase):
	pass 
	
class BillItemOut(BillItemBase):
	id: int 
	
	class Config:
		orm_mode = True 
	
class BillBase(BaseModel):
	items: List[BillItemCreate]
	
class BillOut(BaseBase):
	id: int 
	status: PaymentStatus
	amount: float
	issued_at: datetime
	items: List[BillItemOut]
	
	class Config:
		orm_mode = True 
		