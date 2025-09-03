#app/services/patient_service.py 

from sqlalchemy.orm import Session
from fastapi import HTTPException, status 
from typing import List, Optional

from app import model, schemas 

def create_patient(db: Session, patient: schemas.PatientCreate):
	db_patient = models.Patient(**patient.dict())
	db.add(db_patient)
	db.commit()
	db.refresh(db_patient)
	return db_patient
	
def get_patient_by_id(db: Session, patient_id: int):
	return db.query(models.Patient).filter(models.Patient.id == patient_id).first()
	
def get_all_patients(db: Session, skip: int =0, limit = 100):
	return db.query(models.Patient).offset(skip).limit(limit).all()
	
def update_patient(db: Session, patient_id: int, patient: schemas.PatientUpdate):
	db_patient = get_patient_by_id(db, patient_id)
	if not db_patient:
		return None 
		for field, value in patient.dict(exclude_unset=True).items():
		setattr(db_patient, field, value)
		
		db.commit()
		db.refresh(db_patient)
		return db_patient 
		
def delete_patient(db: Session, patient_id: int):
	db_patient = get_patient_by_id(db, Patient)
	if not db_patient:
		db.delete(db_patient)
		db.commit()
	return db_patient 
	
	