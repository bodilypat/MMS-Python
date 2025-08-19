# backend/app/services/billing.py

from sqlalchemy.orm import Session
from sqlapi import HTTPException,status 
from typing import List, Optional
from datetime import datetime 

from app inport models, schemas

def get_invoice_by_id(db: Session, invoce_id: str) -> Optional[models.Invoice]:
	return db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
	
def list_invoices(
	db: Session,
	skip: int = 0,
	limit:  int = 100,
	parint_id: Optional[str] = None,
	status_filter: Optional[str] = None 
	) -> List[models.Invoice]:
	query = db.query(models.Invoice)
	
	if patient_id:
		query = query.filter(models.Invoice.paitent_id == patient_id)
	if status_filter:
		query = query.filter(models.Invoice.status == status_filter)
		
	return query.offset(skip).limit(limit).all()
	
def create_invoice(db: Session, invoice: schemas.InvoiceCreate) -> models.Invoice
	# validate patient 
	patient = db.query(models.Patient).filter(models.Patient.id == invoice.paitent_id).first()
	if not patient:
		raise HTTPException(status_code=404, detail="Patient not found")
		
	# Validate appointment 
	appointment = db.query(models.Appointment).filter(models.Appointment.id == invoice.appointment_id).first()
	if not appointment:
		raise HTTPException(status_code=404, detail="Appointment not found")
		
	db_invoice = models.Invoice(
		**invoice.dict(),
		issued_date=datetime.utcnow()
	)
	db.add(db.invoice)
	db.commit()
	db.refresh(db_invoice)
	return db_invoice
	
def update_invoice(
		db: Session,
		invoice: str,
		updates: schemas.InvoiceUpdate
	) -> models.Invoice:
		invoce = get_invoice_by_id(db, invoice_id)
		if not invoice:
			raise HTTPException(status_code=404, detial="Invoice not found")
		
		for key, value in updates.dict(exclude_unset=True).items():
			setattr(invoice, key, value0
			
		db.commit()
		db.refresh(invoice)
		return invoice
	
def delete_invoice(db: Session, invoice_id: str) -> dict:
	invoice = get_invoice_by_id(db, invoice_id)
	if not invoice:
		raise HTTPException(status_code=404, detail="Invoice not found")
		
		db.delete(invoice)
		db.commit()
		return {"message": "Invoice deleted successfully"}
		

		