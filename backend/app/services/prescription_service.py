#app/services/prescription_service.py

from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.prescription import Prescription
from app.schemas.prescription import PrescriptionCreate, PrescriptionUpdate

#-----------------------------------------------
# Create a new prescription
#-----------------------------------------------
def create_prescription(db: Session, prescription: PrescriptionCreate) -> Prescription:
    db_prescription = Prescription(
        patient_id=prescription.patient_id,
        doctor_id=prescription.doctor_id,
        appointment_id=prescription.appointment_id,
        medication=prescription.medication,
        instructions=prescription.instructions,
        notes=prescription.notes,
        status=prescription.status,
        valid_until=prescription.valid_until,
    )
    db.add(db_prescription)
    db.commit()
    db.refresh(db_prescription)
    return db_prescription

#-----------------------------------------------
# Get a prescription by ID
#-----------------------------------------------
def get_prescription(db: Session, prescription_id: int) -> Optional[Prescription]:
    return db.query(Prescription).filter(Prescription.id == prescription_id).first()

#-----------------------------------------------
# Get all prescriptions
#-----------------------------------------------
def get_prescriptions(db: Session, skip: int = 0, limit: int = 100) -> List[Prescription]:
    return db.query(Prescription).offset(skip).limit(limit).all()

#-----------------------------------------------
# Update a prescription
#-----------------------------------------------
def update_prescription(db: Session, prescription_id: int, prescription_update: PrescriptionUpdate) -> Optional[Prescription]:
    db_prescription = db.query(Prescription).filter(Prescription.id == prescription_id).first()
    if not db_prescription:
        return None
    for var, value in vars(prescription_update).items():
        setattr(db_prescription, var, value) if value else None
    db.commit()
    db.refresh(db_prescription)
    return db_prescription

#-----------------------------------------------
# Delete a prescription
#-----------------------------------------------
def delete_prescription(db: Session, prescription_id: int) -> bool:
    db_prescription = db.query(Prescription).filter(Prescription.id == prescription_id).first()
    if not db_prescription:
        return False
    db.delete(db_prescription)
    db.commit()
    return True

#-----------------------------------------------
# Get prescriptions by patient ID
def get_prescriptions_by_patient(db: Session, patient_id: int) -> List[Prescription]:
    return db.query(Prescription).filter(Prescription.patient_id == patient_id).all()

#-----------------------------------------------
# Get prescriptions by doctor ID
#-----------------------------------------------
def get_prescriptions_by_doctor(db: Session, doctor_id: int) -> List[Prescription]:
    return db.query(Prescription).filter(Prescription.doctor_id == doctor_id).all()

#-----------------------------------------------
# Get prescriptions by appointment ID
#-----------------------------------------------
def get_prescriptions_by_appointment(db: Session, appointment_id: int) -> List[Prescription]:
    return db.query(Prescription).filter(Prescription.appointment_id == appointment_id).all()

#-----------------------------------------------
# Get prescriptions by status
#-----------------------------------------------
def get_prescriptions_by_status(db: Session, status: str) -> List[Prescription]:
    return db.query(Prescription).filter(Prescription.status == status).all()

#-----------------------------------------------
# Get valid prescriptions
#-----------------------------------------------
def get_valid_prescriptions(db: Session) -> List[Prescription]:
    from datetime import datetime
    current_date = datetime.utcnow()
    return db.query(Prescription).filter(Prescription.valid_until >= current_date).all()

#-----------------------------------------------
# Get expired prescriptions
#-----------------------------------------------
def get_expired_prescriptions(db: Session) -> List[Prescription]:
    from datetime import datetime
    current_date = datetime.utcnow()
    return db.query(Prescription).filter(Prescription.valid_until < current_date).all()

#-----------------------------------------------
# Count total prescriptions
#-----------------------------------------------
def count_total_prescriptions(db: Session) -> int:
    return db.query(Prescription).count()



