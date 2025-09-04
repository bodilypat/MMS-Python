#app/api/v1/medical_record_api.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.services import medical_record_service 
from app.schemas import medical_record_schema

from app.db.session import get_db 

router = APIRouter(prefix="/medical-records", tags=["Medical Records"])

# Create medical record
@router.post("/", response_model=medical_record_schema.MedicalRecordOut, status_code=status.HTTP_201_CREATED)
def create_record(record: medical_record_schema.MedicalRecordCreate, db: Session = Depends(get_db)):
    try:
        return medical_record_service.create_medical_record(db, record)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
        
# Get medical record by ID	
@router.get("/{record_id}", response_model=medical_record_schema.MedicalRecordOut)
def read_record(record_id: int, db: Session = Depends(get_db)):
	record = medical_record_service.get_medical_record_by_id(db, record_id)
	if not record:
		raise HTTPException(status_code=404, detail="Medical record not found")
	return record 
	
# Get patient id 
@router.get("/patient/{patient_id}", response_model=list[medical_record_schema.MedicalRecordOut])
def record_by_patient(patient_id: int, db: Session = Depends(get_db)):
	return medical_record_service.get_records_by_patient(db, patient_id)
	
# Update medical record 
@router.put("/{record_id}", response_model=medical_record_schema.MedicalRecordOut)
def update_record(record_id: int, data: medical_record_schema.MedicalRecordUpdate, db: Session = Depends(get_db)):
	updated = medical_record_service.update_medical_record(db, record_id, data)
	if not updated:
		raise HTTPException(status_code=404, detail="Medical record not found")
	return updated 
	
@router.delete("/{record_id}" status_code=status.HTTP_204_NO_CONTENT)
def delete_record(record_id: int, db: Session = Depends(get_db)):
	deleted = medical_record_service.delete_medical_record(db, record_id)
	if not deleted:
		raise HTTPException(status_code=404, detail="Medical record not found")
	return {"message": "Deleted successfully"}
	
	