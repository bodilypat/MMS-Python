# backend/app/schemas/payment_schema.py

from pydantic import BaseModel, Field, condecimal
from typing import Optional, Literal
from datetime import datetime

# Enum - Like Literals for Consistency

PaymentStatus = Literal["Paid", "Partially Paid", "Pending", "Overdue", "Refunded"]
PaymentMethod = Literal["Cash", "Credit Card", "Debit Card", "Insurance", "Online", "Bank Transfer", "Other"]
InsuranceStatus = Literal["Approved", "Pending", "Denied", "Not Applicable"]

# Base Schema

class PaymentBase(BaseModel):
	patient_id: int 
	appointment_id: int 
    
	total_amount: condecimal(max_digits=10, decimal_places=2) = Field(..., ge=0)
	amount_paid: condecimal(max_digits=10, decimal_places=2) = Field(0.00, ge=0)
	
	payment_status: PaymentStatus = "Pending"
	payment_method: PaymentMethod = "Card"
	
	transaction_reference: Optional[str] = None
	payment_date: Optional[datetime] = None 
	
	insurance_claimed_amount: Optional[condecimal(max_digits=10, decimal_places=2)] = Field(0.00, ge=0)
	insurance_status: InsuranceStatus = "Not Applicable"
	insurance_provider: Optional[str] = None
	
	notes: Optional[str] = None
	refund_amount: Optional[condecimal(max_digits=10, decimal_places=2)] = Field(0.00, ge=0)
	
	created_by: Optional[int]
	updated_by: Optional[int]
	
# Create Schema

class PaymentCreate(PaymentBase):
    pass

# Updat Schema    
class PaymentUpdate(BaseModel):
    patient_id: Optional[int]
    appointment_id: Optional[int]
    
    total_amount: Optional[condecimal(max_digits=10, decimal_places)] = Field(None, ge=0)
    amount_paid: Optional[condecimal(max_digits=10, decimal_place=2)] = Field(None, ge=0)
    
    payment_status: Optional[Literal['Paid', 'Partially Paid', 'Pending', 'Overdue', 'Refunded']] = None
    payment_method: Optional[Literal['Cash', 'Credit', 'Debit Card', 'Insurance', 'Online', 'Bank Transfer', 'Other']] = None 
    
    transaction_reference: Optional[str] = None
    payment_date: Optional[datetime] = None
    
    insurance_claimed_amount: Optional[condecimal(max_digits=10, decimal_places=2)] = Field(None, ge=0)
    insurance_status: Optional[Literal['Approved', 'Pending', 'Denied', 'Not Applicable']] = None
    insurance_provider: Optional[str] = None
    
    notes: Optional[str] = None
    refund_amount: Optional[condecimal(max_digits=10, decimal_places=2)] = Field(None, ge=0)
    
    created_by: Optional[int] = None 
    updated_by: Optional[int] = None
    
# Response schema
class PaymentResponse(PaymentBase):
    payment_id: int
    balance_due: condecimal(max_digits=10, decimal_places=2)
    created_at: datetime 
    updated_at: datetime 
    
    class Config:
        orm_mode: True 
        
        
    
    