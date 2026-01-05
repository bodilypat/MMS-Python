#app/services/medical_record_service.py

from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.medical_record import MedicalRecord
from app.schemas.medical_record import MedicalRecordCreate, MedicalRecordUpdate

#------------------------------------------
# Create a new medical record
#------------------------------------------
def create_medical_record(db: Session, record: MedicalRecordCreate) -> MedicalRecord:
    db_record = MedicalRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

#------------------------------------------
# Get a medical record by ID
#------------------------------------------
def get_medical_record(db: Session, record_id: int) -> Optional[MedicalRecord]:
    return db.query(MedicalRecord).filter(MedicalRecord.id == record_id).first()

#------------------------------------------
# Get all medical records
#------------------------------------------
def get_medical_records(db: Session, skip: int = 0, limit: int = 100) -> List[MedicalRecord]:
    return db.query(MedicalRecord).offset(skip).limit(limit).all()

#------------------------------------------
# Update a medical record
#------------------------------------------
def update_medical_record(db: Session, record_id: int, record_update: MedicalRecordUpdate) -> Optional[MedicalRecord]:
    db_record = db.query(MedicalRecord).filter(MedicalRecord.id == record_id).first()
    if db_record:
        for key, value in record_update.dict(exclude_unset=True).items():
            setattr(db_record, key, value)
        db.commit()
        db.refresh(db_record)
    return db_record

#------------------------------------------
# Delete a medical record
#------------------------------------------
def delete_medical_record(db: Session, record_id: int) -> bool:
    db_record = db.query(MedicalRecord).filter(MedicalRecord.id == record_id).first()
    if db_record:
        db.delete(db_record)
        db.commit()
        return True
    return False

#------------------------------------------
# Search medical records by patient name
#------------------------------------------
def search_medical_records_by_patient_name(db: Session, patient_name: str) -> List[MedicalRecord]:
    return db.query(MedicalRecord).filter(MedicalRecord.patient_name.ilike(f"%{patient_name}%")).all()

#------------------------------------------
# Get medical records by date range
#------------------------------------------
def get_medical_records_by_date_range(db: Session, start_date: str, end_date: str) -> List[MedicalRecord]:
    return db.query(MedicalRecord).filter(MedicalRecord.record_date.between(start_date, end_date)).all()

#------------------------------------------
# Count total medical records
#------------------------------------------
def count_medical_records(db: Session) -> int:
    return db.query(MedicalRecord).count()

#------------------------------------------
# Get medical records by diagnosis
#------------------------------------------
def get_medical_records_by_diagnosis(db: Session, diagnosis: str) -> List[MedicalRecord]:
    return db.query(MedicalRecord).filter(MedicalRecord.diagnosis.ilike(f"%{diagnosis}%")).all()

#------------------------------------------
# Get recent medical records
#------------------------------------------
def get_recent_medical_records(db: Session, days: int) -> List[MedicalRecord]:
    from datetime import datetime, timedelta
    cutoff_date = datetime.now() - timedelta(days=days)
    return db.query(MedicalRecord).filter(MedicalRecord.record_date >= cutoff_date).all()

#------------------------------------------
# Get medical records by doctor ID
#------------------------------------------
def get_medical_records_by_doctor_id(db: Session, doctor_id: int) -> List[MedicalRecord]:
    return db.query(MedicalRecord).filter(MedicalRecord.doctor_id == doctor_id).all()



