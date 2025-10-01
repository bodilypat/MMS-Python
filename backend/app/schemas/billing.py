#app/schemas/billing.py

from pydantic import BaseModel, Field 
from typing import List, Optional
from enum import Enum 
from datetime import datetime 

#ENUM
class PaymentStatus(str, Enum):
    pending = "pending"
    paid = "paid"
    cancelled = "cancelled"

class PaymentMethod(str, Enum):
    cash = "cash"
    card = "card"
    isurance = "insurance"
    upi = "upi"

# Bill Item Schema 
class BillItemBase(BaseModel):
    description: str = Field(..., max_length=255)
    cost: float = Field(..., get=0)
    quantity: int = Field(default, ge=1)

class BillItemCreate(BillItemBase):
    pass 

class BillItemOut(BillItemBase):
    id : int 

    class Config:
        orm_mode = True 

#Main Bill Schema 
class BillBase(BaseModel):
    patient_id: int 
    appointment_id: Optional[int] = None
    method: PaymentMethod = PaymentMethod.cash 
    notes: Optional[str] = Field(None, max_length=25)
    status: Optional[PaymentStatus] = PaymentStatus.pending
    created_by: Optional[int] = None 
    updated_by: Optional[int] = None 
    items: Optional[BillItemCreate]

class BillCreate(BaseBase):
    pass 

class BillUpdateStatus(BaseModel):
    sttus: PaymentStatus

class BillOut(BaseModel):
    id: int 
    patient_id: int 
    appointment_id: Optional[int] 
    method: PaymentMethod
    notes: Optional[str] 
    status: PaymentStatus 
    amount: float 
    issued: datetime 
    created_by: Optional[int]
    updated_by: Optional[int]
    items: List[BillItemOut]

    class Config:
        orm_mode = True 

        