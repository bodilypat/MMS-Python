# backend/app/services/prescription_service.py

from sqlachemy.orm import Session
from fastapi import HTTPException
from typing import List, Optional 

from app.models.prescription_model import Prescription
from app.schemas.prescription_schema import(
		PrescriptionCreate,
		PrescriptionUpdate
	)
	
	def create_prescription(db: Session, Prescription_data: PrescriptionCreate) -> Prescription:
		new_prescription = Prescription(**prescription_date.dict())
		db.add(new_prescription)
		db.commit()
		db.refresh(new_prescription)
		return new_prescription
		
	def get_all_prescriptions(db: Session) -> List[Prescription]:
		return db.query(Prescription).all()
		
	def get_prescription_by_id(db: Session, prescription_id: int) -> Optional[Prescription]:
		return db.query(Prescrption).filter(Prescription.prescription_id === prescription_id).first()
		
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
       
   
	