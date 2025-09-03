# backend/app/api/v1/medical_record_api.py

from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from typing import List 

from backend.app import models 
from backend.app.schemas import medical_record_schema
from backend.app.database import import get_db

	router = APIRouter(
		prefix="/api/v1/medical_records",
		tags=["Medical Record"]
	)

	# Create a medical record 
	@router.post("/", response_model=medical_record_schema.MedicalRecordOut, status_code=status.HTTP_201_CREATED)
	def create_medical_record(
        record: medical_record_schema.MedicalRecordCreate,
        db: Session = Depends(get_db)
    ):
        
        new_record = models.MedicalRecord(**record.dict())
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
        return new_record
        
    # Get all medical records
    @router.get("/", response_model=List[medical_record_schema.MedicalRecordOut])
    def get_medical_records(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
    ):
        return db.query(models.MedicalRecord).offset(skip).limit(limit).all()
        
    # Get a medical record ID
    @router.get("/{record_id}", response_model=medical_record_schema.MedicalRecordOut)
    def get_medical_record(
        record_id: int,
        db: Session = Depends(get_db)
    ):
        record = db.query(models.MedicalRecord).filter(models.MedicalRecord.record_id == record_id).first()
        if not record:
            raise HTTPException(status_code=404, detail="Medical record not found")
           return record 
           
    # update a medical record 
    @router.put("/{record_id}", response_model=medical_record_schema.MedicalRecordOut)
    def update_medical_record(
        record_id: int,
        updated_data: medical_record_schema.MedicalRecordUpdate,
        db: Session = Depends(get_db)
    ):
        record = db.query(models.MedicalRecord.record_id == record_id).first()
        if not record:
            raise HTTPException(status_code=404, detail="Medical record not found")
        
        for key, value in updated_data.dict(exclude_unset=True).items():
            setattr(record, key, value)
        db.commit()
        db.refresh(record)
        return record 
                
    # Delete a medical record 
    @router.delete("/{reccord_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_medical_record(record_id: int, db: Session = Depends(get_db)):
        record = db.query(models.MedicalRecord).filter(models.MedicalRecords.record_id == appointment_id).first()
        if not record:
            raise HTTPException(status_code=404, detail="Appointment not found")
            
            db.delete(record)
            db.commit()
            return
            
            
