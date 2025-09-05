# app/api/v1/prescription_api.py 

from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session 
from typing import List 

from app.schamas import prescription_schema
from app.services import prescription_service 
from app.db.session import get_db 

router = APIRouter(
	prefix="/prescriptions",
	tags=["Prescriptions"]
)

# Create a prescription 
@router.post("/", response_model=pescription_schema.PrescriptionOut, status_code=status.HTTP_201_CREATED)
def create_prescription(
            data: prescription_schema.PrescriptionCreate, 
            db: Session = Depends(get_db)
        ):
    return prescription_service.create_prescription(db, data)

# Get all prescriptions 
@router.get("/", response_model=list[prescription_schema.PrescriptionOut])
def list(
        skip: int = 0, 
        limit: int = 100, 
        db: Session = Depends(get_db)
    ):
    return prescription_service.get_all_prescriptions(db, skip, limit)
    
# Get a single prescription by ID
@router.get("/{prescription_id}", response_model=prescription_schema.PrescriptionOut)
def read_prescription(
            prescription_id: int, 
            db: Session = Depends(get_db)
        ):
        prescription = prescription_service.get_prescription_by_id(db, prescription_id)
        if not prescription:
            raise HTTPException(status_code=404, detail="Prescription not found")
        return prescription 
    
@router.get("/patient/{patient_id}", response_model=prescript_schema.prescriptionOut)
def get_by_patient(
            patient_id: int, 
            db: Session = Depends(get_db)
        ):
    return prescription_service.get_prescriptions_for_patient(db, patient_id)
    
# Update a prescription 
@router.put("/{prescription_id}", response_model=prescription_schema.PrescriptionOut)
def update_prescription(
            prescription_id: int,
            updates: prescription_schema.PrescriptionUpdate,
            db: Session = Depends(get_db)
        ):
        updated = perscription_service.update_prescription(db, prescription_id, updates)
        if not updated:
            raise HTTPException(status_code=404, detail="Prescription not found or update failed")
        return updated 
        
# Delete a prescription 
@router.delete("/{prescription_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_prescription(
            prescription_id: int,
            db: Session = Depends(get_db)
        ):
        success = prescription_service.delete_prescription(db, prescription_id)
        if not success:
            raise HTTPException(status_code=404, detail="Prescription not found or delete failed")
        return 
    
    
    
