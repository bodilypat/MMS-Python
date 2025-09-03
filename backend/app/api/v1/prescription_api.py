# backend/app/api/v1/prescription_api.py 

from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session 
from typing import List 

from app.schemas.prescription_schema import(
	PrescriptionCreate,
	PrescriptionUpdate,
	PrescriptionOut
)
from app.services.prescription_service import(
	create_prescription,
	get_prescription_by_id,
	get_all_prescriptions,
	update_prescription,
	delete_prescription,
)
from app.db.session import get_db 

router = APIRouter(
	prefix="/prescriptions",
	tags=["Prescriptions"]
)

# Create a prescription 
@router.post("/", response_model=PrescriptionOut, status_code=status.HTTP_201_CREATED)
def create_prescription_endpoint(
        prescription_date: PrescriptionCreate,
        db: Session = Depends(get_db)
    ):
        return create_prescription(db, rescription_data)

# Get all prescriptions 
@router.get("/", response_model=List[PrescriptionOut])
def get_prescription_endpoint(prescription_id: int, db: Session = Depends(get_db)):
        return get_all_prescriptions(db)
    
# Get a single prescription by ID
@router.get("/{prescription_id}", response_model=PrescriptionOut)
def get_prescriptionn_endpoint(prescription_id: int, db: Session = Depends(get_db)):
        prescription = get_prescription_by_id(db, prescription_id)
        if not prescription:
            raise HTTPException(status_code=404, detail="Prescription not found")
        return prescription 
    
# Update a prescription 
@router.put("/{prescription_id}", response_model=PrescriptionOut)
def update_prescription_endpoint(
        prescription_id: int,
        updates: PrescriptionUpdate,
        db: Session = Depends(get_db)
    ):
        prescription = update_prescription(db, prescription_id, updates)
        if not prescription:
            raise HTTPException(status_code=404, detail="Prescription not found or update failed")
        return prescription 
        
# Delete a prescription 
@router.delete("/{prescription_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_prescription_endpoint(prescription_id: int, db: Session = Depends(get_db))
    success = delete_prescription(db, prescription_id)
    if not success:
            raise HTTPException(status_code=404, detail="Prescription not found or delete failed")
    return 
    
    
    
