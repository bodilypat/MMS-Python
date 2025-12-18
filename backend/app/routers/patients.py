#app/routers/patients.py 

from fastapi import APIRouter, HTTPException, Depends   
from sqlalchemy.orm import Session
from typing import List
from app.schemas.patient import PatientCreate, PatientUpdate, PatientOut
from app.database import get_db
from app.services.patient_service import PatientService

router = APIRouter(
    prefix="/patients", 
    tags=["patients"]
)

#------------------------------------------
# Create a new patient
#----------------------------------
@router.post("/", response_model=PatientOut)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    service = PatientService(db)
    return service.create_patient(patient)

#------------------------------------------
# Get a patient by ID
#------------------------------------------
@router.get("/{patient_id}", response_model=PatientOut)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    service = PatientService(db)
    patient = service.get_patient_by_id(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

#------------------------------------------
# Update a patient by ID
#------------------------------------------
@router.put("/{patient_id}", response_model=PatientOut)
def update_patient(patient_id: int, patient: PatientUpdate, db: Session = Depends(get_db)):
    service = PatientService(db)
    updated_patient = service.update_patient(patient_id, patient)
    if not updated_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return updated_patient

#------------------------------------------
# Delete a patient by ID
#------------------------------------------
@router.delete("/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    service = PatientService(db)
    success = service.delete_patient(patient_id)
    if not success:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"detail": "Patient deleted successfully"}

#------------------------------------------
# List all patients
#------------------------------------------
@router.get("/", response_model=List[PatientOut])
def list_patients(db: Session = Depends(get_db)):
    service = PatientService(db)
    return service.list_patients()

#------------------------------------------
# Search patients by name
#------------------------------------------
@router.get("/search/", response_model=List[PatientOut])
def search_patients(name: str, db: Session = Depends(get_db)):
    service = PatientService(db)
    return service.search_patients_by_name(name)

#------------------------------------------
# Get patients by age range
#------------------------------------------
@router.get("/age/", response_model=List[PatientOut])
def get_patients_by_age(min_age: int, max_age: int, db: Session = Depends(get_db)):
    service = PatientService(db)
    return service.get_patients_by_age_range(min_age, max_age)

#------------------------------------------
# Get patients by medical condition
#------------------------------------------
@router.get("/condition/", response_model=List[PatientOut])
def get_patients_by_condition(condition: str, db: Session = Depends(get_db)):
    service = PatientService(db)
    return service.get_patients_by_medical_condition(condition)

#------------------------------------------
# Get patients with upcoming appointments
#------------------------------------------
@router.get("/upcoming-appointments/", response_model=List[PatientOut])
def get_patients_with_upcoming_appointments(db: Session = Depends(get_db)):
    service = PatientService(db)
    return service.get_patients_with_upcoming_appointments()

