#app/api/v1/lab_api.py

from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session 
from app.schemas.lab_schema import lab_schema 
from app.service.lab_service import lab_service 
from app.db.session import get_db 

router = APIRouterp(prefix="/lab", tags=["Lab Management"])

@router.post("/tests", response_model=lab_schema.LabTestOut)
def create_test(test: lab_schema.LabTestCreate, db: Session = Depends(get_db)):
	return Lab_service.create_lab_test(db, test)
	
@router.get("/tests", response_model=list[lab_schema.LabTestOut])
def get_tests(db: Session = Depends(get_db)):
	return lab_service.list_lab_tests(db)
	
@router.post("/orders", response_model=lab_schema.LabTestOut)
def order_test(order: lab_schema.LabTestCreate, db: Session = Depends(get_db)):
	return lab_service.creae_lab_order(db, order)
	
@router.get("/orders/{order_id}", response_model=schemas.LabOrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
	order = lab_service.get_lab_order_by_id(db, order_id)
	if not order:
		raise HTTPException(status_code=404, detail="Order not found")
	return order 
	
@router.put("/orders/{order_id}", response_model=lab_schema.LabOrderOut)
def update_order(order_id: it, data: lab_schema.LabOrderUpdate, db: Session = Depends(get_db)):
	updated = lab_service.update_lab_order(db, order_id, data)
	if not updated:
		raise HTTPException(status_code=404, detail="Order not found")
	return updated 
	
@router.get("/orders/patient/{patient_id}", response_model=list[lab_schema.LabOrderOut])
def get_patient_order(patient_id: int, db: Session = Depends(get_db)):
	return lab_service.get_orders_by_patient(db, patient_id)


