#app/services/patient_service.py

from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientUpdate

#-------------------------------------
# Create a new patient record
#-------------------------------------
def create_patient(db: Session, patient: PatientCreate) -> Patient:
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient
    
#-------------------------------------
# Get a patient record by ID
#-------------------------------------
def get_patient(db: Session, patient_id: int) -> Optional[Patient]:
    return db.query(Patient).filter(Patient.id == patient_id).first()

#-------------------------------------
# Get all patient records
#-------------------------------------
def get_patients(db: Session, skip: int = 0, limit: int = 100) -> List[Patient]:
    return db.query(Patient).offset(skip).limit(limit).all()

#-------------------------------------
# Update a patient record
#-------------------------------------
def update_patient(db: Session, patient_id: int, patient_update: PatientUpdate) -> Optional[Patient]:
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if db_patient:
        for key, value in patient_update.dict(exclude_unset=True).items():
            setattr(db_patient, key, value)
        db.commit()
        db.refresh(db_patient)
    return db_patient
#-------------------------------------
# Delete a patient record
#-------------------------------------
def delete_patient(db: Session, patient_id: int) -> bool:
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if db_patient:
        db.delete(db_patient)
        db.commit()
        return True
    return False
#-------------------------------------
# Search patients by name
#-------------------------------------
def search_patients_by_name(db: Session, name: str) -> List[Patient]:
    return db.query(Patient).filter(Patient.name.ilike(f"%{name}%")).all()

#-------------------------------------
# Get patients by age range
#-------------------------------------  
def get_patients_by_age_range(db: Session, min_age: int, max_age: int) -> List[Patient]:
    return db.query(Patient).filter(Patient.age >= min_age, Patient.age <= max_age).all()

#-------------------------------------
# Get patients by medical condition
#-------------------------------------
def get_patients_by_medical_condition(db: Session, condition: str) -> List[Patient]:
    return db.query(Patient).filter(Patient.medical_conditions.ilike(f"%{condition}%")).all()

#-------------------------------------
# Get patients by assigned doctor
#-------------------------------------
def get_patients_by_assigned_doctor(db: Session, doctor_id: int) -> List[Patient]:
    return db.query(Patient).filter(Patient.assigned_doctor_id == doctor_id).all()

#---------------------------------------
# Get patients with upcoming appointments
#---------------------------------------
def get_patients_with_upcoming_appointments(db: Session, days_ahead: int) -> List[Patient]:
    from datetime import datetime, timedelta
    upcoming_date = datetime.now() + timedelta(days=days_ahead)
    return db.query(Patient).filter(Patient.next_appointment <= upcoming_date).all()
#-------------------------------------
# Count total number of patients
#-------------------------------------
def count_total_patients(db: Session) -> int:
    return db.query(Patient).count()

#-------------------------------------
# Get patients by insurance provider
#-------------------------------------
def get_patients_by_insurance_provider(db: Session, provider: str) -> List[Patient]:
    return db.query(Patient).filter(Patient.insurance_provider.ilike(f"%{provider}%")).all()

#-------------------------------------
# Get patients by city
def get_patients_by_city(db: Session, city: str) -> List[Patient]:
    return db.query(Patient).filter(Patient.city.ilike(f"%{city}%")).all()


