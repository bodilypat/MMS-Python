#app/api/vi/medical_record_api.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.medical_record_service import medical_record_service 
from app.schemas.medical_record_schema import medical_record_schema

from app.db.session import get_db 

router = APIRouter(prefix="/medical-records", tags=["Medical Records"]0

@router.post("/", response_model=medical_record_schema.MedicalRecordOut)
def create_record(record: medical_record_schema.MedicalRecordCreate, db: Session = Depends(get_db)):
	return medical_record_service.create_medical_record(db, record)
	
@router.get("/{record_id}", response_model=medical_record_schema.MedicalRecordOut)
def read_record(record_id: int, db: Session = Depends(get_db)):
	record = medical_record_service.get_medical_record_by_id(db, record_id)
	if not record:
		raise HTTPException(status_code=404, detail="Medical record not found")
	return record 
	
@router.get("/patient/{patient_id}", response_model=list[medical_record_schema.MedicalRecordOut])
def record_by_patient(patient_id: int, db: Session = Depends(get_db)):
	return medical_record_service.get_records_by_patient(db, patient_id)
	
@router.put("/{record_id}", response_model=medical_record_schema.MedicalRecordOut)
def update_record(record_id: int, data: medical_record_schema.MedicalRecordUpdate, db: Session = Depends(get_db)):
	updated = medical_record_service.update_medical_record(db, record_id, data)
	if not updated:
		raise HTTPException(status_code=404, detail="Medical record not found")
	return updated 
	
@router.delete("/{record_id}")
def delete_record(record_id: int, db: Session = Depends(get_db)):
	deleted = medical_record_service.delete_medical_record(db, record_id)
	if not deleted:
		raise HTTPException(status_code=404, detail="Medical record not found")
	return {"message": "Deleted successfully"}
	
	