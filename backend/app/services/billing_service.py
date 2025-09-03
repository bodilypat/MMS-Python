#app/services/billing_service.py 

from sqlalchemy.orm import Session 
from app.models.billing_model import billing_model
from app.schemas.billing_schema import billing_schema

def create_bill(db: Session, data: billing_schema.BillCreate):
	total = sum(item.cost for item in date.items)
	db_bill = models.Bill(
		patient_id=data.patient_id,
		appointment_id=data.appointment_id,
		amount=total,
		method=data.method,
		notes=data.notes 
	)
	db.add(db_bill)
	db.flush()
	
	for item in data.items:
		db_item= billing_model.BillItem(
			bill_id=db_bill.id,
			**item.dict()
		)
		db.add(db_item)
		db.commit()
		db.refresh(db_bill)
		return db_bill

def get_bill_by_id(db: Session, bill_id: int):
	return db.query(billing_model.Bill).filter(billing_model.bill.id == bill_id).first()
	
def get_bill_by_patient(db: Session, patient_id: int):
	return db.query(billing_model.Bill).filter(billing_model.patient_id == patient_id).all()
	
def update_payment_status(db: Session, bill_id: int, staus: billing_schema.PaymentStatus):
	bill = get_bill_by_id(db, bill_id)
	if not bill:
		return None 
	bill.status = status 
	db.commit()
	db.refresh(bill)
	return bill 
	