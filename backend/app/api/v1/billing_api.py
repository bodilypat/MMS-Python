#app/api/v1/billing_api.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas import billing_schema 
from app.services import billing_service 
from app.db.session import get_db 

router = APIRouter(prefix="/billing", tags=["Billing"])

@router.post("/", response_model=billing_schema.BillOut, status_code=status.HTTP_201_CREATED)
def create_bill(data: billing_schema.BillCreate, db: Session = Depends(get_db)):
    """
        Create a new bill for a patient.
    """
	return billing_service.create_bill(db, data)
	
@router.get("/{bill_id}", response_model=billing_schema.BillOut)
def get_bill(bill_id: int, db: Session = Depends(get_db)):
    """
        Get a specific bill by ID.
    """
    
	bill = billing_service.get_bill_by_id(db, bill_id)
	if not bill: 
		raise HTTPException(status_code=404, detail="Bill not found")
	return bill
	
@router.get("/patient/{patient_id}", response_model=List(billing_schema.BillOut])
def get_bills_by_patient(patient_id: int, db: Session = Depends(get_db)):
    """
        Get all bill associated with a specific patient.
    """
	return billing_service.get_bills_by_patient(db, patient_id)
	
@router.put("/{bill_id}/status", response_model=billing_schema.BillOut)
def update_status(Bill_id: int, status: billing_schema.PaymentStatus, db: Session = Depends(get_db)):
    """
        Update the payment status of a bill.
    """
    
	bill = billing_service.update_payment_status(db, bill_id, status)
	if not bill:
		raise HTTPException(status_code=404, detail="Bill not found")
	return bill
	
