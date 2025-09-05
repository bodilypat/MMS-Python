# app/services/prescription_service.py

from sqlachemy.orm import Session
from typing import List, Optional

from app.models import prescription_model
from app.schemas import prescript_schema 
	
def create_prescription(db: Session, data: prescript_schema.PrescriptionCreate):
		db_prescription = prescript_model.Prescription(
            patient_id=data.patient_id,
            doctor_id=data.doctor_id,
            note=data.notes
		)
        db.add(db_prescription)
        db.flush() # Get ID before commit
        
        for medication in data.medications:
            db_medication = prescription_model.Medication(
                prescription_id=db_prescription.prescription_id,
                **medication.dict()
            )
            db.add(db_medication)
            
        db.commit()
        db.refresh(db_prescription)
        return db_prescription
        
		
def get_all_prescriptions(db: Session, skip: int = 0, limit: int = 100) -> List[prescription_model.Prescription]:
		return db.query(prescription_model.Prescription).offset(skip).limit(limit).all()
		
def get_prescription_by_id(db: Session, prescription_id: int) -> Optional[prescription_model.Prescription]:
		return db.query(prescription_model.Prescrption).filter(
                            prescription_model.Prescription.prescription_id == prescription_id
                        ).first()
        
def get_prescription_for_patient(db: Session, patient_id: int) -> List[prescription_model.Prescription]:
    return db.query(prescription_model.Prescription).filter(
                    prescription_model.Prescription.patient_id == patient_id
                   ).all()
		
def update_prescription(
        db: Session,
        prescription_id: int 
        updates: prescription_schema.PrescriptionUpdate 
    ) -> Optional[prescription_model.Prescription]:
                prescription =  db.query(prescription.Prescription).filter(
                                    prescription_model.Prescription.prescription_id == prescription_id
                                ).frist()
        
        if not prescription:
            return None
            
        for key, value in updates.dict(exclude_unset=True).items():
                setattr(prescription, key, value)
                
            db.commit()
            db.refresh(prescription)
            return prescription
    
    def delete_prescription(db: Session, prescription_id: int) -> bool:
        prescription = db.query(prescription_model.Prescription).filter(
                prescription_model.Prescription.prescription_id == prescription_id
            ).first()
        
        if not prescription:
            return False
            
        db.delete(prescription)
        db.commit()
        return True 
       
   
	