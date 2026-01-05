#app/services/appointment_service.py 

from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate, AppointmentUpdate

#-----------------------------------------
# Create a new appointment
#-----------------------------------------
def create_appointment(db: Session, appointment: AppointmentCreate) -> Appointment:
    db_appointment = Appointment(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

#-----------------------------------------
# Get an appointment by ID
#-----------------------------------------
def get_appointment(db: Session, appointment_id: int) -> Optional[Appointment]:
    return db.query(Appointment).filter(Appointment.id == appointment_id).first()

#-----------------------------------------
# Get all appointments
#-----------------------------------------
def get_appointments(db: Session, skip: int = 0, limit: int = 100) -> List[Appointment]:
    return db.query(Appointment).offset(skip).limit(limit).all()

#-----------------------------------------
# Update an existing appointment
#-----------------------------------------
def update_appointment(db: Session, appointment_id: int, appointment_update: AppointmentUpdate) -> Optional[Appointment]:
    db_appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if db_appointment:
        for key, value in appointment_update.dict(exclude_unset=True).items():
            setattr(db_appointment, key, value)
        db.commit()
        db.refresh(db_appointment)
    return db_appointment

#-----------------------------------------
# Delete an appointment
#-----------------------------------------
def delete_appointment(db: Session, appointment_id: int) -> bool:
    db_appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if db_appointment:
        db.delete(db_appointment)
        db.commit()
        return True
    return False

#-----------------------------------------
# Get appointments by patient ID
#-----------------------------------------
def get_appointments_by_patient(db: Session, patient_id: int) -> List[Appointment]:
    return db.query(Appointment).filter(Appointment.patient_id == patient_id).all()
#-----------------------------------------
# Get appointments by doctor ID
#-----------------------------------------
def get_appointments_by_doctor(db: Session, doctor_id: int) -> List[Appointment]:
    return db.query(Appointment).filter(Appointment.doctor_id == doctor_id).all()

#-----------------------------------------
# Get appointments by date
#-----------------------------------------
def get_appointments_by_date(db: Session, appointment_date: str) -> List[Appointment]:
    return db.query(Appointment).filter(Appointment.date == appointment_date).all()

#-----------------------------------------
# Get upcoming appointments
#-----------------------------------------
def get_upcoming_appointments(db: Session, current_date: str) -> List[Appointment]:
    return db.query(Appointment).filter(Appointment.date >= current_date).all()

#-----------------------------------------
# Get past appointments
#-----------------------------------------
def get_past_appointments(db: Session, current_date: str) -> List[Appointment]:
    return db.query(Appointment).filter(Appointment.date < current_date).all()

#-----------------------------------------
# Cancel an appointment
#-----------------------------------------
def cancel_appointment(db: Session, appointment_id: int) -> Optional[Appointment]:
    db_appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if db_appointment:
        db_appointment.status = 'canceled'
        db.commit()
        db.refresh(db_appointment)
    return db_appointment

#-----------------------------------------
# Reschedule an appointment
#-----------------------------------------
def reschedule_appointment(db: Session, appointment_id: int, new_date: str) -> Optional[Appointment]:
    db_appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if db_appointment:
        db_appointment.date = new_date
        db.commit()
        db.refresh(db_appointment)
    return db_appointment

#-----------------------------------------
# Get appointments by status
#-----------------------------------------
def get_appointments_by_status(db: Session, status: str) -> List[Appointment]:
    return db.query(Appointment).filter(Appointment.status == status).all()

#-----------------------------------------
# Get appointments within a date range
#-----------------------------------------
def get_appointments_in_date_range(db: Session, start_date: str, end_date: str) -> List[Appointment]:
    return db.query(Appointment).filter(Appointment.date.between(start_date, end_date)).all()

#-----------------------------------------
# Get the total number of appointments
#-----------------------------------------
def get_total_appointments(db: Session) -> int:
    return db.query(Appointment).count()
