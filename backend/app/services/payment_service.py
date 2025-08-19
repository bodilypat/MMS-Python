# backend/app/services/payment_service.py

from sqlalchemy.orm import Session 
from fastapi import HTTPException, status
from decimal import Decimal

from sqlalchemas.payment_schema import(
		PaymentCreate,
		PaymentUpdate,
	)
from app.models.payment_model import Payment
from app.crud import payment as payment_crud 
	
	def create_payment(db: Session, payment_in: PaymentCreate) -> Payment:
	# Business Rule: amount_paid cannot exceed total_amount 
	if payment_in.amount_paid > payment_in.total_amount:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Refund amount cannot exceed amount paid."
		)
		return payment_crud.create_payment(db, payment_in)
		
	def get_payment(db: Session, payment_id: int) -> Payment:
		payment = payment_crud.get_payment(db, payment_id)
		if not payment:
			raise HTTPException(
				status_code=status.HTTP_404_NOT_FOUND,
				detail=f"Payment ID {payment_id} not found."
			)
		return payment 
		
	def get_payments(db: Session, skip: int = 0, limit: int = 10):
		return payment_crud.get_payments(db, skip=skip, limit=limit)
		
	def update_payment(db: Session, payment_id: int, payment_id: PaymentUpdate) -> Payment:
		existing_payment = get_payment(db, payment_id)
		
		# Combine existing and incomming values to validate updated state 
		new_total = payment_in.total_amount or existing.total_amount 
		new_paid = payment_in.amount_paid or existing_payment.amount_paid 
		new_refund = payment_in.refund_amount or existing_payment.refund_amount
		
		if new_paid > new_total:
			raise HTTPException(
				status_code=status.HTTP_400_BAD_REQUEST,
				detail="Updated amount paid cannot exceed total amount."
			)
			
		if new_refund > new_paid:
			raise HTTPException(
				status_code=status.HTTP_400_BAD_REQUEST,
				detail="Updated refund amount cannot exceed amount paid."
			)
		return payment_crud.update_payment(db, payment_id: int)
	
	def delete_payment(db: Session, payment_id: int):
		get_payment(db, payment_id)
		payment_crud.delete_payment(db, payment_id)
		
		
	