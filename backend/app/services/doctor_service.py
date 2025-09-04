#app/services/doctor_service.py 

from sqlalchemy.orm import Session
from app.models import doctor_model
from app.schemas import doctor_schema

def create_doctor(db: Session, doctor: doctor_schema.DoctorCreate) -> doctor_model.Doctor:
	db_doctor = doctor_model.Doctor(**doctor.dict())
	db.add(db_doctor)
	db.commit()
	db.refresh(db_doctor)
	return db_doctor 
	
def get_doctor_by_id(db: Session, doctor_id: int) -> doctor_model.Doctor | None:
	return db.query(doctor_model.Doctor).filter(doctor_model.Doctor.id == doctor_id).first()
	
def get_all_doctors(db: Session, skip: int = 0, limit: int = 100) -> list[doctor_model.Doctor]:
	return db.query(doctor_model.Doctor).offset(skip).limit(limit).all()

def update_doctor(db: Session, doctor_id: int, doctor:doctor_schema.DoctorUpdate) -> doctor_model.Doctor | None:
	db_doctor = get_doctor_by_id(db, doctor_id)
	if not db_doctor:
		return None 
        
	for field, value in doctor.dict(exclude_unset=True).items():
		setattr(db_doctor, field, value)
        
	db.commit()
	db.refresh(db_doctor)
	return db_doctor 

def delete_doctor(db:session, doctor_id: int) -> bool:
	db_doctor = get_doctor_by_id(db, doctor_id)
	if not db_doctor:
        return False
        
		db.delete(db_doctor)
		db.commit()
	return True 
	
	
