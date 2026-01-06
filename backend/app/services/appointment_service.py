# app/services/appointment_service.py

from datetime import datetime
from typing import List, Optional

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.models.appointment import Appointment
from app.schemas.appointment import (
    AppointmentCreate,
    AppointmentUpdate,
    AppointmentStatusUpdate,
)
from app.core.constants import AppointmentStatus 

#-----------------------------------------------
# Create Appointment
#-----------------------------------------------
def create_appointment(
    db: Session,
    appointment_in: AppointmentCreate,
    patient_id: int,
) -> Appointment:
    
    """
    Create a new appointment for a patient.
    """
    db_appointment = Appointment(
        **appointment_in.dict(),
        patient_id=patient_id,
        status=AppointmentStatus.SCHEDULED,
        created_at=datetime.utcnow(),
    )
    
    try:
        db.add(db_appointment)
        db.commit()
        db.refresh(db_appointment)
        return db_appointment
    except SQLAlchemyError as e:
        db.rollback()
        raise e
#-----------------------------------------------
# Get Appointment by ID 
#-----------------------------------------------
def get_appointment_by_id (
    db: Session,
    appointment_id: int
) -> Optional[Appointment]:
    """
    Retrieve an appointment by its ID.
    """
    return (
        db.query(Appointment)
        .filter(Appointment.id == appointment_id)
        .first()
    )

#-----------------------------------------------
# List Appointments (Pagination Ready)
#-----------------------------------------------
def list_appointments(
    db: Session,
    skip: int = 0,
    limit: int = 50,
) -> List[Appointment]:
    """
    List appointments with pagination.
    """
    return (
        db.query(Appointment)
        .order_by(Appointment.date.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

#-----------------------------------------------
# Update Appointment (Patient Reschedule / Cancel)
#-----------------------------------------------
def reschedule_or_cancel_appointment(
    db: Session,
    appointment_id: int,
    appointment_in: AppointmentUpdate,
    patient_id: int,
) -> Optional[Appointment]:
    """
    Reschedule an existing appointment.
    """
    appointment = (
        db.query(Appointment)
        .filter(
            Appointment.id == appointment_id,
            Appointment.patient_id == patient_id,
        )
        .first()
    )

    if not appointment:
        return None
    
    for field, value in appointment_in.dict(exclude_unset=True).items():
        setattr(appointment, field, value)
    
    appointment.updated_at = datetime.utcnow()

    try:
        db.commit()
        db.refresh(appointment)
        return appointment
    
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    
#-----------------------------------------------
# Update Status (Doctor)
#-----------------------------------------------
def update_appointment_status(
    db: Session,
    appointment_id: int,
    status_update: AppointmentStatusUpdate,
) -> Optional[Appointment]:
    """
    Update the status of an appointment.
    """
    appointment = (
        db.query(Appointment)
        .filter(Appointment.id == appointment_id)
        .first()
    )

    if not appointment:
        return None
    
    appointment.status = status_update.status
    appointment.updated_at = datetime.utcnow()

    try:
        db.commit()
        db.refresh(appointment)
        return appointment
    
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    
#-----------------------------------------------
# Cancel Appointment (self cancel)
#-----------------------------------------------
def cancel_appointment(
    db: Session,
    appointment_id: int,
    patient_id: int,
) -> Optional[Appointment]:
    """
    Cancel an appointment by the patient.
    """
    appointment = (
        db.query(Appointment)
        .filter(
            Appointment.id == appointment_id,
            Appointment.patient_id == patient_id,
        )
        .first()
    )

    if not appointment:
        return None
    
    appointment.status = AppointmentStatus.CANCELLED
    appointment.updated_at = datetime.utcnow()

    try:
        db.commit()
        db.refresh(appointment)
        return appointment
    
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    
#-----------------------------------------------
# Delete Appointment (Admin Only)
#-----------------------------------------------
def delete_appointment(
    db: Session,
    appointment_id: int,
) -> bool:
    """
    Delete an appointment (admin only).
    """
    appointment = (
        db.query(Appointment)
        .filter(Appointment.id == appointment_id)
        .first()
    )

    if not appointment:
        return False
    
    try:
        db.delete(appointment)
        db.commit()
        return True
    
    except SQLAlchemyError as e:
        db.rollback()
        raise e
#-----------------------------------------------
# Doctor / Patient View
#-----------------------------------------------
def get_appointments_by_patient(
    db: Session,
    patient_id: int,
    skip: int = 0,
    limit: int = 50,
) -> List[Appointment]:
    """
    Retrieve appointments for a specific patient.
    """
    return (
        db.query(Appointment)
        .filter(Appointment.patient_id == patient_id)
        .order_by(Appointment.date.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

def get_appointments_by_doctor(
    db: Session,
    doctor_id: int,
    skip: int = 0,
    limit: int = 50,
) -> List[Appointment]:
    """
    Retrieve appointments for a specific doctor.
    """
    return (
        db.query(Appointment)
        .filter(Appointment.doctor_id == doctor_id)
        .order_by(Appointment.date.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

#-----------------------------------------------
# Time-based Queries
#-----------------------------------------------
def get_upcoming_appointments(
    db: Session,
    current_time: datetime,
    skip: int = 0,
    limit: int = 50,
) -> List[Appointment]:
    """
    Retrieve upcoming appointments.
    """
    return (
        db.query(Appointment)
        .filter(Appointment.date >= current_time)
        .order_by(Appointment.date.asc())
        .offset(skip)
        .limit(limit)
        .all()
    )

def get_past_appointments(
    db: Session,
    current_time: datetime,
    skip: int = 0,
    limit: int = 50,
) -> List[Appointment]:
    """
    Retrieve past appointments.
    """
    return (
        db.query(Appointment)
        .filter(Appointment.date < current_time)
        .order_by(Appointment.date.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
#-----------------------------------------------
# Status & Analytics
#-----------------------------------------------
def count_appointments_by_status(
    db: Session,
    status: AppointmentStatus,
) -> int:
    """
    Count appointments by their status.
    """
    return (
        db.query(Appointment)
        .filter(Appointment.status == status)
        .count()
    )
#-----------------------------------------------
# Appointment Reminders
#-----------------------------------------------
def get_appointments_for_reminders(
    db: Session,
    reminder_time: datetime,
    skip: int = 0,
    limit: int = 50,
) -> List[Appointment]:
    """
    Retrieve appointments that need reminders sent out.
    """
    return (
        db.query(Appointment)
        .filter(
            Appointment.date >= reminder_time,
            Appointment.date < reminder_time + timedelta(minutes=15),
            Appointment.status == AppointmentStatus.SCHEDULED,
        )
        .order_by(Appointment.date.asc())
        .offset(skip)
        .limit(limit)
        .all()
    )
#-----------------------------------------------
#