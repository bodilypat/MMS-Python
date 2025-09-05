#app/services/lab_service.py

from sqlalchemy.orm import Session
from app.models import lab_model
from app.schemas import lab_schema 
from datetime import datetime 
from typing import List, Optional

# Lab Test Service
def create_lab_test(db: Session, test: lab_schema.LabTestCreate) -> lab_model.LabTest:
	db_test = lab_model.LabTest(**test.dict())
	db.add(db_test)
	db.commit()
	db.refresh(db_test) 
	return db_test

def list_bal_tests(db: Session)-> List[lab_model.labTest]:
	return db.query(lab_model.LabTest).all()

# Lab Order Services	
def create_lab_order(db: Session, order: lab_schema.LabTestCreate) -> lab_model.LabOrder:
	db_order = lab_model.LabOrder(**order.dict())
	db.add(db_order)
	db.commit()
	db.refresh(db_order)
	return db_order 
	
def get_lab_order_by_id(db: Session, order_id: int) -> Optional[lab_model.LabOrder]:
    return db.query(lab_model.LabOrder).filter(lab_model.LabOrder.id == order_id).first()
    
def update_lab_order(db: Session, order_id: int, data: lab_schema.LabOrderUpdate) -> Optional[lab_model.LabOrder]:
    order = db.query(lab_model.LabOrder).filter(lab_model.LabOrder.id == order_id).first()
    
    if not order:
        return None 
        
        update_data = data.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(order, field, value)
            
        if "status" in update_data and update_data["status"] == lab_schema.TestStatus.completed:
            order.completed_at = datetime.utcnow()
            
        db.commit()
        db.refresh(order)
        return order 
        
def get_order_by_patient(db: Session, patient_id: int) -> List[lab_model.LabOrder];
    return db.query(lab_model.LabOrder).filter_by(patient_id=patient_id).all()
    
	