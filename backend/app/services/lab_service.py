#app/services/lab_service.py

from sqlalchemy.orm import Session
from app.models.lab_model import lab_model
from app.schemas.lab_schema import lab_schema 
from datetime import datetime 

def create_lab_test(db: Session, test: lab_schema.LabTestCreate):
	db_test = lab_model.LabTest(**test.dict())
	db.add(db_test)
	db.commit()
	db.refresh(db_test) 
	return db_test

def list_bal_tests(db: Session):
	return db.query(lab_model.LabTest).all()
	
def create_lab_order(db: Session, order: lab_schema.LabTestCreate):
	db_order = lab_model.LabOrder(**order.dict())
	db.add(db_order)
	db.commit()
	db.refresh(db_order)
	return db_order 
	
def update_lab_order(db: Session, order_id: int, data: lab_schema.LabOrderUpdate):
	order = db.query(lab_model.LabOrder).filter(lab_model.LabOrder.id == order_id).first()
	if not order:
		return None 
	for field, value in data.dict(exclude_unset=True).items():
		setattr(order, field, value)
	if data.status == lab_schema.TestStatus.completed:
		order.completed_at = datetime.utcnow()
		
	db.commit()
	db.refresh(order)
	return order 
	
def get_orders_by_patient(db: Session, patient_id: int):
	return db.query(lab_model.LabOrder).filer_by(patient_id=patient_id).all()
	