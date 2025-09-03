#app/api/v1/patient_api.py

from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session

from app.schemas import patient_schema
from app.services import patient_service
from app.db import get_db 

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.post("/", response_model=patient_schema.PatientOut)
def create_patient(patient:patient_schema.PatientCreate, db: Session = Depends(get_db)):
    return patient_service.create_patient(db, patient)
    
# Gall all patient 
@router.get("/", response_model=list[patient_schemas.PatientOut])
def get_all_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return patient_service.get_all_patients(db, skip, limit)
    
# Get patient by ID
@router.get("/{patient_id}", response_model=patient_schema.PatientOut)
def get_patient_by_id(patient_id: int, db: Session = Depends(get_db)):
    patient = patient_service.get_patient_by_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code = 404, detail="Patient not found")
    return Patient
    
# Update patient 
@router.put("/{patient_id}", response_model=patient_schema.PatientOut)
def update_patient(patient_id: int, patient: patient_schemas.PatientUpdate, db: Session = Depends(get_db)):
    updated = patient_service.update_patient(db, patient_id, patient)
    if not updated:
        raise HTTPException(status_code=404, detail="Patient not found")
    return updated
  
# Delete patient 
@router.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    deleted = patient_service.delete_patient(db, patient_id)
    if not deleted:
        raise HTTPException(status_code=404, detail ="Patient not found")
        