#app/routers/prescriptions.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.prescription import PrescriptionCreate, PrescriptionUpdate, PrescriptionResponse
from app.database import get_db
from app.services.prescription_service import PrescriptionService

router = APIRouter(
    prefix="/prescriptions",
    tags=["prescriptions"]
)

#-----------------------------------------
# Create a new prescription
#-----------------------------------------
@router.post("/", response_model=PrescriptionResponse)
def create_prescription(prescription: PrescriptionCreate, db: Session = Depends(get_db)):
    service = PrescriptionService(db)
    return service.create_prescription(prescription)
#-----------------------------------------
# Get a prescription by ID
#-----------------------------------------
@router.get("/{prescription_id}", response_model=PrescriptionResponse)
def get_prescription(prescription_id: int, db: Session = Depends(get_db)):
    service = PrescriptionService(db)
    prescription = service.get_prescription_by_id(prescription_id)
    if not prescription:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return prescription

#-----------------------------------------
# Update a prescription by ID
#-----------------------------------------
@router.put("/{prescription_id}", response_model=PrescriptionResponse)
def update_prescription(prescription_id: int, prescription: PrescriptionUpdate, db: Session = Depends(get_db)):
    service = PrescriptionService(db)
    updated_prescription = service.update_prescription(prescription_id, prescription)
    if not updated_prescription:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return updated_prescription

#-----------------------------------------
# Delete a prescription by ID
#-----------------------------------------
@router.delete("/{prescription_id}")
def delete_prescription(prescription_id: int, db: Session = Depends(get_db)):
    service = PrescriptionService(db)
    success = service.delete_prescription(prescription_id)
    if not success:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return {"detail": "Prescription deleted successfully"}

#-----------------------------------------
# List all prescriptions
#-----------------------------------------
@router.get("/", response_model=List[PrescriptionResponse])
def list_prescriptions(db: Session = Depends(get_db)):
    service = PrescriptionService(db)
    return service.list_prescriptions()

#-----------------------------------------
# List prescriptions by patient ID
#-----------------------------------------
@router.get("/patient/{patient_id}", response_model=List[PrescriptionResponse])
def list_prescriptions_by_patient(patient_id: int, db: Session = Depends(get_db)):
    service = PrescriptionService(db)
    return service.list_prescriptions_by_patient(patient_id)

#-----------------------------------------
# List prescriptions by doctor ID
#-----------------------------------------
@router.get("/doctor/{doctor_id}", response_model=List[PrescriptionResponse])
def list_prescriptions_by_doctor(doctor_id: int, db: Session = Depends(get_db)):
    service = PrescriptionService(db)
    return service.list_prescriptions_by_doctor(doctor_id)

#-----------------------------------------
# List prescriptions by medication name
#-----------------------------------------
@router.get("/medication/{medication_name}", response_model=List[PrescriptionResponse])
def list_prescriptions_by_medication(medication_name: str, db: Session = Depends(get_db)):
    service = PrescriptionService(db)
    return service.list_prescriptions_by_medication(medication_name)

#-----------------------------------------
# List prescriptions by date range
#-----------------------------------------
@router.get("/date-range/", response_model=List[PrescriptionResponse])
def list_prescriptions_by_date_range(start_date: str, end_date: str, db: Session = Depends(get_db)):
    service = PrescriptionService(db)
    return service.list_prescriptions_by_date_range(start_date, end_date)

#-----------------------------------------
# List prescriptions by status
#-----------------------------------------
@router.get("/status/{status}", response_model=List[PrescriptionResponse])
def list_prescriptions_by_status(status: str, db: Session = Depends(get_db)):
    service = PrescriptionService(db)
    return service.list_prescriptions_by_status(status)


