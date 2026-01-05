#app/services/doctor_service.py

from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorUpdate

#-----------------------------------
# Create a new doctor
#-----------------------------------
def create_doctor(db: Session, doctor: DoctorCreate) -> Doctor:
    db_doctor = Doctor(**doctor.dict())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor
#-----------------------------------
# Get a doctor by ID
#-----------------------------------
def get_doctor(db: Session, doctor_id: int) -> Optional[Doctor]:
    return db.query(Doctor).filter(Doctor.id == doctor_id).first()

#-----------------------------------
# Get all doctors
#-----------------------------------
def get_doctors(db: Session, skip: int = 0, limit: int = 100) -> List[Doctor]:
    return db.query(Doctor).offset(skip).limit(limit).all()
#-----------------------------------
# Update a doctor
#-----------------------------------
def update_doctor(db: Session, doctor_id: int, doctor_update: DoctorUpdate) -> Optional[Doctor]:
    db_doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if db_doctor:
        for key, value in doctor_update.dict(exclude_unset=True).items():
            setattr(db_doctor, key, value)
        db.commit()
        db.refresh(db_doctor)
    return db_doctor

#-----------------------------------
# Delete a doctor
#-----------------------------------
def delete_doctor(db: Session, doctor_id: int) -> Optional[Doctor]:
    db_doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if db_doctor:
        db.delete(db_doctor)
        db.commit()
    return db_doctor

#-----------------------------------
# Find doctors by specialty
#-----------------------------------
def find_doctors_by_specialty(db: Session, specialty: str) -> List[Doctor]:
    return db.query(Doctor).filter(Doctor.specialty == specialty).all()

#-----------------------------------
# Find doctors by name
#-----------------------------------
def find_doctors_by_name(db: Session, name: str) -> List[Doctor]:
    return db.query(Doctor).filter(Doctor.name.ilike(f"%{name}%")).all()

#-----------------------------------
# Get doctors by availability
#-----------------------------------
def get_doctors_by_availability(db: Session, available: bool) -> List[Doctor]:
    return db.query(Doctor).filter(Doctor.is_available == available).all()

#-----------------------------------
# Count total number of doctors
#-----------------------------------
def count_doctors(db: Session) -> int:
    return db.query(Doctor).count()

