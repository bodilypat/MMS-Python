#app/services/patient_service.py 

from sqlalchemy.orm import Session
from fastapi import HTTPException, status 
from typing import List, Optional

from app.models import patient_model as models
from app.schemas import patient_schema as schemas

def create_patient(db: Session, patient: schemas.PatientCreate) -> models.Patient:
	db_patient = models.Patient(**patient.dict())
	db.add(db_patient)
	db.commit()
	db.refresh(db_patient)
	return db_patient
	
def get_patient_by_id(db: Session, patient_id: int) -> Optional[models.Patient]:
	return db.query(models.Patient).filter(models.Patient.id == patient_id).first()
	
def get_all_patients(db: Session, skip: int = 0, limit = 100) ->List[models.Patient]:
	return db.query(models.Patient).offset(skip).limit(limit).all()
	
def update_patient(db: Session, patient_id: int, patient: schemas.PatientUpdate) ->Optional[models.Patient]:
	db_patient = get_patient_by_id(db, patient_id)
	if not db_patient:
		return None 
        
    patient_data = patient.dict(exclude_unset=True)
	for field, value in patient_data.items():
		setattr(db_patient, field, value)
		
		db.commit()
		db.refresh(db_patient)
		return db_patient 
		
def delete_patient(db: Session, patient_id: int) -> bool:
	db_patient = get_patient_by_id(db, patient_id)
	if not db_patient:
        return False
        
	db.delete(db_patient)
	db.commit()
	return True 
	
	