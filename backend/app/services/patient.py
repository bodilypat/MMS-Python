# backend/app/api/services/patient.py

from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPExceptions, status

def get_patient_by_email(db: Session, email: str):
	return db.query(models.Patient).filter(models.Patient.email == email).first()
	
def create_patient(db: Session, patient: schemas.PatientCreate):
	existing = get_patient_by_email(db, patient.email)
	if existing:
		raise HTTPExceptions(status_code=400, detail="Email already registered")
		
	new_patient = models.Patient(**patient.dict())
	db.add(new_patient)
	db.commit()
	db.refresh(new_patient)
	return new_patient