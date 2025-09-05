#app/api/v1/lab_api.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session 
from typing import List 

from app.schemas import lab_schema 
from app.service import lab_service 
from app.db.session import get_db 

router = APIRouter(prefix="/lab", tags=["Lab Management"])

# Create a new lab test
@router.post(
        "/tests", 
        response_model=lab_schema.LabTestOut, 
        status_code=status.HTTP_201_CREATED, 
        summary="Create a new lab test"
    )
def create_test(test: lab_schema.LabTestCreate, db: Session = Depends(get_db)):
	return lab_service.create_lab_test(db, test)
	
# List all available lab tests
@router.get(
        "/tests", 
        response_model=list[lab_schema.LabTestOut],
        summary="List all available lab tests"
    )
def get_tests(db: Session = Depends(get_db)):
	return lab_service.list_lab_tests(db)
	
# Create a lab test order for a patient
@router.post(
        "/orders", 
        response_model=lab_schema.LabOrderOut,
        status_code=status.HTTP_201_CREATED,
        summary="Create a lab test order for a patient"
    )
def order_test(order: lab_schema.LabOrderCreate, db: Session = Depends(get_db)):
	return lab_service.creae_lab_order(db, order)
	
# Get a specific lab test order by ID
@router.get(
        "/orders/{order_id}", 
        response_model=lab_schemas.LabOrderOut,
        summary="Get a lab test order by ID."
    )
def get_order(order_id: int, db: Session = Depends(get_db)):
	order = lab_service.get_lab_order_by_id(db, order_id)
	if not order:
		raise HTTPException(status_code=404, detail="Order not found")
	return order 
	
# Get a specific lab test order by ID
@router.put(
        "/orders/{order_id}", 
        response_model=lab_schema.LabOrderOut
    )
def update_order(order_id: it, data: lab_schema.LabOrderUpdate, db: Session = Depends(get_db)):
	updated = lab_service.update_lab_order(db, order_id, data)
	if not updated:
		raise HTTPException(status_code=404, detail="Order not found")
	return updated 
	
@router.get(
        "/orders/patient/{patient_id}", 
        response_model=list[lab_schema.LabOrderOut],
        summary="Get all lab orders for a specific patient"
    )
def get_patient_order(patient_id: int, db: Session = Depends(get_db)):
	return lab_service.get_orders_by_patient(db, patient_id)


