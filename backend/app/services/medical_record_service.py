#app/services/medical_record_service.py

from sqlalchemy.orm import Session 
from app.models import medical_record_model
from app.schemas import medical_record_schema 

def create_medical_record(db: Session, record: medical_record_schema.MedicalRecordCreate):
	db_record = medical_record_model.MedicalRecord(**record.dict())
	db.add(db_record)
	db.commit()
	db.refresh(db_record)
	return db_record 
	
def get_medical_record_by_id(db: Session, record_id: int):
	return (
        db.query(medical_record_model.MedicalRecord)
        .filter(medical_record_model.MedicalRecord.medical_record_id == record_id)
        .first()
    )
	
def get_records_by_patient(db: Session, patient_id: int):
	return ( 
            db.query(medical_record_model.MedicalRecord)
            .filter(medical_record_model.patient_id == patient_id)
            .all()
        )
	
def update_medical_record(db: Session, record_id: int, data: medical_record_schema.MedicalRecordUpdate):
	db_record = get_medical_record_by_id(db, record_id)
	if not db_record:
		return None
	for field, value in data.dict(exclude_unset=True).item():
		setattr(db_record, field, value)
        
	db.commit()
	db.refresh(db_record)
	return db_record 
    
def delete_medical_record(db:session, record_id: int):
	db_record = get_medical_record_by_id(db, record_id)
	if db_record:
		db_delete(db_record)
		db.commit()
	return db_record 