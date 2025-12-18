#app/services/billing_service.py 

from sqlalchemy.orm import Session
from typing import List, Optional
from app.models import BillingRecord
from app.schemas import BillingRecordCreate, BillingRecordUpdate

#---------------------------------------------
# create a new billing record
#---------------------------------------------
def create_billing_record(db: Session, record: BillingRecordCreate) -> BillingRecord:
    db_record = BillingRecord(
        patient_id=record.patient_id,
        appointment_id=record.appointment_id,
        amount=record.amount,
        billing_date=record.billing_date,
        due_date=record.due_date,
        status=record.status,
        description=record.description,
        payment_method=record.payment_method,
        notes=record.notes
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

#---------------------------------------------
# get a billing record by id
#---------------------------------------------
def get_billing_record(db: Session, record_id: int) -> Optional[BillingRecord]:
    return db.query(BillingRecord).filter(BillingRecord.id == record_id).first()

#---------------------------------------------
# get all billing records
#---------------------------------------------
def get_billing_records(db: Session, skip: int = 0, limit: int = 100) -> List[BillingRecord]:
    return db.query(BillingRecord).offset(skip).limit(limit).all()

#---------------------------------------------
# update a billing record
#---------------------------------------------
def update_billing_record(db: Session, record_id: int, record_update: BillingRecordUpdate) -> Optional[BillingRecord]:
    db_record = db.query(BillingRecord).filter(BillingRecord.id == record_id).first()
    if db_record:
        for key, value in record_update.dict(exclude_unset=True).items():
            setattr(db_record, key, value)
        db.commit()
        db.refresh(db_record)
    return db_record

#---------------------------------------------
# delete a billing record
#---------------------------------------------
def delete_billing_record(db: Session, record_id: int) -> bool:
    db_record = db.query(BillingRecord).filter(BillingRecord.id == record_id).first()
    if db_record:
        db.delete(db_record)
        db.commit()
        return True
    return False

#---------------------------------------------
# get billing records by patient id
#---------------------------------------------
def get_billing_records_by_patient(db: Session, patient_id: int) -> List[BillingRecord]:
    return db.query(BillingRecord).filter(BillingRecord.patient_id == patient_id).all()

#---------------------------------------------
# get billing records by status
#---------------------------------------------
def get_billing_records_by_status(db: Session, status: str) -> List[BillingRecord]:
    return db.query(BillingRecord).filter(BillingRecord.status == status).all()

#---------------------------------------------
# get total billing amount for a patient
#---------------------------------------------
def get_total_billing_amount_for_patient(db: Session, patient_id: int) -> float:
    total = db.query(func.sum(BillingRecord.amount)).filter(BillingRecord.patient_id == patient_id).scalar()
    return total if total else 0.0

#---------------------------------------------
# mark a billing record as paid
#---------------------------------------------
def mark_billing_record_as_paid(db: Session, record_id: int) -> Optional[BillingRecord]:
    db_record = db.query(BillingRecord).filter(BillingRecord.id == record_id).first()
    if db_record:
        db_record.status = 'Paid'
        db.commit()
        db.refresh(db_record)
    return db_record

#---------------------------------------------
# get overdue billing records
#---------------------------------------------
def get_overdue_billing_records(db: Session, current_date: date) -> List[BillingRecord]:
    return db.query(BillingRecord).filter(
        BillingRecord.status != 'Paid',
        BillingRecord.due_date < current_date
    ).all()

#---------------------------------------------
# generate billing summary report
def generate_billing_summary_report(db: Session, start_date: date, end_date: date) -> List[BillingRecord]:
    return db.query(BillingRecord).filter(
        BillingRecord.billing_date >= start_date,
        BillingRecord.billing_date <= end_date
    ).all()
#---------------------------------------------

