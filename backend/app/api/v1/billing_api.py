#app/api/v1/billing_api.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.billing_schema import billing_schema 
from app.services.billing_service import billing_service 
from app.db.session import get_db 

router = APIRouter(prefix="/billing", tags=["Billing"])

@router.post("/", response_model=billing_schema.BillOut)
def create_bill(data: billing_schema.BillCreate, db: Session = Depends(get_db)):
	return billing_service.create_bill(db, data)
	
@router.get("/{bill_id}", response_model=billing_schema.BillOut)
def get_bill(bill_id: int, db: Session = Depends(get_db)):
	bill = billing_service.get_bill_by_id(db, bill_id)
	if not bill: 
		raise HTTPException(status_code=404, detail="Bill not found")
	return bill
	
@router.get("/patient/{patient_id}", response_model=List(billing_schema.BillOut])
def get_bills_by_patient(patient_id: int, db: Session = Depends(get_db)):
	return billing_service.get_bills_by_patient(db, patient_id)
	
@router.put("/{bill_id}/status", response_model=billing_schema.BillOut)
def update_status(Bill_id: int, status: billing_schema.PaymentStatus, db: Session = Depends(get_db)):
	bill = billing_service.update_payment_status(db, bill_id, status)
	if not bill:
		raise HTTPException(status_code=404, detail="Bill not found")
	return bill
	
