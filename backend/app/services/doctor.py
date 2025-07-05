# backend/app/services/doctor.py

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import List, Optional

from app import, models, schemas

def get_doctor_by_id(db: Session, doctor_id: str) -> Optional[models.Doctor]:
	return db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()
	
def get_doctor_by_email(db: Session, email: str) -> Optional[models.Doctor]:
	return db.query(models.Doctor).filter(models.Doctor.email == email).first()
	
def list_doctors(db: Session, skip: int = 0, limit: int =100) -> List[models.Doctor]:
	return db.query(models.Doctor).offset(skip).limitt(limit).all()
	
def create_doctor(db: Session, doctor: schemas.DoctorCreate) -> models.Doctor:
	existing = get_doctor_by_email(db, doctor.email)
	if existing:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Email already registered"
		)
		db.doctor = models.Doctor(**doctor.dict())
		db.add(db_doctor)
		db.commit()
		db.refresh(db_doctor)
		return db_doctor
def update_doctor9db: Session, doctor_id: str, updates: schemas.DoctorUpdate) -> models.Doctor:
	doctor = get_doctor_by_id(db, doctor_id)
	if not doctor:
		raise HTTPException(status_code=404, detail="Doctor not found")
		
	for key, value in updates.dict(exclude_unset=True).items():
		setattr(doctor, key, value)
		
	db.commit()
	db.refresh(doctor)
	return doctor
def delete_doctor(db: Session, doctor_id: str) -> dict:
	doctor = get_doctor_by_id(db, doctor_id)
	if not doctor:
		raise HTTPException(status_code=404, detail=:Doctor not found")
	db.delete(doctor)
	db.commit()
	return {"message": "Doctor deleted successfully")
	
	
