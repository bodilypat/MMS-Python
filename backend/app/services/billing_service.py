#app/services/billing_service.py 

from sqlalchemy.orm import Session 
from typing import Optional, List 

from app.models import billing_model
from app.schemas import billing_schema

def create_bill(db: Session, data: billing_schema.BillCreate) -> billing_model.Bill:
	total = sum(item.cost for item in data.items)
    
	db_bill = billing_models.Bill(
		patient_id=data.patient_id,
		appointment_id=data.appointment_id,
		amount=total,
		method=data.method,
		notes=data.notes,
        status=data.status or billing_schema.PaymentStatus.unpaid,
        created_by=data.created_by,
        updated_by=data.updated_by,
	)
	db.add(db_bill)
	db.flush() # Get db_bill.id before adding items
	
	for item in data.items:
		db_item= billing_model.BillItem(
			bill_id=db_bill.bill_id,
            description=item.description,  
            cost=item.cost,
            quantity=item.quantity,
		)
		
		db.commit()
		db.refresh(db_bill)
		return db_bill

def get_bill_by_id(db: Session, bill_id: int) -> Optional[billing_model.Bill]:
	return db.query(billing_model.Bill).filter(billing_model.Bill.bill_id == bill_id).first()
	
def get_bill_by_patient(db: Session, patient_id: int) -> List[billing_model.Bill]:
	return db.query(billing_model.Bill).filter(billing_model.Bill.patient_id == patient_id).all()
	
def update_payment_status(
        db: Session, bill_id: int, 
        staus: billing_schema.PaymentStatus
        ) -> Optional[billing_model.Bill]:
        bill = get_bill_by_id(db, bill_id)
        if not bill:
            return None 
        bill.status = status 
        db.commit()
        db.refresh(bill)
        return bill 
	