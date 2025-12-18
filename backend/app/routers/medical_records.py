#app/routers/medical_records.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.medical_record import MedicalRecordCreate, MedicalRecordResponse, MedicalRecordUpdate
from app.services.medical_record_service import MedicalRecordService

router = APIRouter(
    prefix="/medical-records",
    tags=["medical-records"]
)

#-------------------------------------------
# Create a new medical record
#-------------------------------------------
@router.post("/", response_model=MedicalRecordResponse)
def create_medical_record(
    record: MedicalRecordCreate,
    db: Session = Depends(get_db)
):
    service = MedicalRecordService(db)
    return service.create_medical_record(record)

#-------------------------------------------
# Get a medical record by ID
#-------------------------------------------
@router.get("/{record_id}", response_model=MedicalRecordResponse)
def get_medical_record(
    record_id: int,
    db: Session = Depends(get_db)
):
    service = MedicalRecordService(db)
    medical_record = service.get_medical_record_by_id(record_id)
    if not medical_record:
        raise HTTPException(status_code=404, detail="Medical record not found")
    return medical_record

#-------------------------------------------
# Update a medical record by ID
#-------------------------------------------
@router.put("/{record_id}", response_model=MedicalRecordResponse)
def update_medical_record(
    record_id: int,
    record_update: MedicalRecordUpdate,
    db: Session = Depends(get_db)
):
    service = MedicalRecordService(db)
    updated_record = service.update_medical_record(record_id, record_update)
    if not updated_record:
        raise HTTPException(status_code=404, detail="Medical record not found")
    return updated_record

#-------------------------------------------
# Delete a medical record by ID
#-------------------------------------------
@router.delete("/{record_id}", response_model=dict)
def delete_medical_record(
    record_id: int,
    db: Session = Depends(get_db)
):
    service = MedicalRecordService(db)
    success = service.delete_medical_record(record_id)
    if not success:
        raise HTTPException(status_code=404, detail="Medical record not found")
    return {"detail": "Medical record deleted successfully"}

#-------------------------------------------
# List all medical records
#-------------------------------------------
@router.get("/", response_model=List[MedicalRecordResponse])
def list_medical_records(
    db: Session = Depends(get_db)
):
    service = MedicalRecordService(db)
    return service.list_medical_records()

#-------------------------------------------
# Search medical records by patient name
#-------------------------------------------
@router.get("/search/", response_model=List[MedicalRecordResponse])
def search_medical_records(
    patient_name: str,
    db: Session = Depends(get_db)
):
    service = MedicalRecordService(db)
    return service.search_medical_records_by_patient_name(patient_name)

#-------------------------------------------
# Filter medical records by date range
#-------------------------------------------
@router.get("/filter/", response_model=List[MedicalRecordResponse])
def filter_medical_records_by_date(
    start_date: str,
    end_date: str,
    db: Session = Depends(get_db)
):
    service = MedicalRecordService(db)
    return service.filter_medical_records_by_date_range(start_date, end_date)

#-------------------------------------------
# Get medical records by doctor ID
@router.get("/doctor/{doctor_id}", response_model=List[MedicalRecordResponse])
def get_medical_records_by_doctor(
    doctor_id: int,
    db: Session = Depends(get_db)
):
    service = MedicalRecordService(db)
    return service.get_medical_records_by_doctor_id(doctor_id)

#-------------------------------------------
# Get medical records by patient ID
#-------------------------------------------
@router.get("/patient/{patient_id}", response_model=List[MedicalRecordResponse])
def get_medical_records_by_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    service = MedicalRecordService(db)
    return service.get_medical_records_by_patient_id(patient_id)

#-------------------------------------------
# Get recent medical records
#-------------------------------------------
@router.get("/recent/", response_model=List[MedicalRecordResponse])
def get_recent_medical_records(
    db: Session = Depends(get_db)
):
    service = MedicalRecordService(db)
    return service.get_recent_medical_records()

#-------------------------------------------
# Get medical records with critical conditions
#-------------------------------------------
@router.get("/critical/", response_model=List[MedicalRecordResponse])
def get_critical_medical_records(
    db: Session = Depends(get_db)
):
    service = MedicalRecordService(db)
    return service.get_critical_medical_records()

