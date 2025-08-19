# backend/app/api/v1/payment_api.py

from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from typing import List 

from app.schemas.payment_schema import PaymentCreate, PaymentUpdate, PaymentResponse
from app.models import payment as payment_model 
from app.service import payment_service 
from app.database import get_db

router = APIRouter(
		prefix="/payments",
		tags=["Payments"]
	)
	
	@router.post("/", response_model=payment_schema.PaymentOut, status_code=status.HTTP_201_CREATED)
	def create_payment(payment_schema.PaymentCreate, db: Session = Depends(get_db)):
		return payment_service.create(db=db, payment=payment)
		
	@router.get("/", response_model=List[payment_Schema.PaymentOut])
	def list_payments(skip: int = 0, limit: int =10, db: Session = Depends(get_db)):
		return payment_service.get_payments(db=db, skip=skip, limit=limit)
		
	@router.get("/{payment_id}", reponse_model=payment_schema.PaymentOut)
	def get_payment(payment_id: int, db: Session = Depends(get_db)):
		db_payment = payment_service.get_payment(db=db, payment_id=payment_id)
		if not db_payment:
			raise HTTPException(status_code=404, detail="Payment not found")
		return db_payment 
		
	@router.put("/{payment_id}", response_model=payment_schema.PaymentOut)
	def update_payment(payment_id: int, payment: payment_schema.PaymentUpdate, db: Session = Depends(get_db)):
		db_payment = payment_service.get_payment(db=db, payment_id=payment_id)
		if not db_payment:
			raise HTTPException(status_code=404, detail="Payment not found")
		return payment_service.update_payment(db=db, payment_id=payment_id, payment=payment)
		
	@router.delete("/{payment_id}", status_code=status.HTTP_201_NO_CONTENT)
	def delete_payment(payment_id: int, db: Session = Depends(get_db)):
		db_payment = payment_service.get_payment(db=db, payment_id=payment_id)
		if not db_payment:
			raise HTTPException(status_code= detail="Payment not found")
		payment_service.delete_payment(db=db, payment_id=payment_id)
		return 
		
	