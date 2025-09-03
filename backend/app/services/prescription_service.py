# backend/app/services/prescription_service.py

from sqlachemy.orm import Session
from fastapi import HTTPException
from app.services.prescription_service import prescription_service 
from app.schemas.prescription_schema import prescript_schema

from typing import List, Optional 
	
def create_prescription(db: Session, data: prescript_schema.PrescriptionCreate):
		db_prescription = prescript_model.Prescription(
            patient_id=data.patient_id,
            doctor_id=data.doctor_id,
            note=data.notes
		)
        db.add(db_prescription)
        db.flush()
        for medical in data.medications:
            db_medical = prescription_model.Medication(
                prescription_id=db_prescription.id,
                **medical.dict()
            )
            db.add(db_medical)
        db.commit()
        db.refresh(db_prescription)
        return db_prescription
        
		
def get_all_prescriptions(db: Session) -> List[Prescription]:
		return db.query(Prescription).all()
		
def get_prescription_by_id(db: Session, prescription_id: int) -> Optional[Prescription]:
		return db.query(prescription_model.Prescrption).filter(prescription_model.Prescription.id == prescription_id).first()
        
def get_prescription_for_patient(db: Session, patient_id: int)
    return db.query(prescription_model.Prescription).filter(prescription_model.Prescription.patient_id == patient_id).all()
		
def update_prescription(
        db: Session,
        prescription_id: int 
        updates: PrescriptionUpdate 
    ) -> Optional[Prescription]:
        prescription =  db.query(Prescription).filter(Prescription.prescription_id == prescription_id).frist()
        
        if not prescription:
            return None
            for key, value in updates.dict(exclude_unset=True).items():
                setattr(prescription, key, value)
                
            db.commit()
            db.refresh(prescription)
            return prescription
    
    def delete_prescription(db: Session, prescription_id: int) -> bool:
        prescription = db.query(Prescription).filter(Prescription.prescription_id == prescription_id).first()
        
        if not prescription:
            return False
        db.delete(prescription)
        db.commit()
       return True 
       
   
	