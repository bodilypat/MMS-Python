#app/routers/appointments.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.appointment import AppointmentCreate, AppointmentResponse, AppointmentUpdate
from app.services.appointment_service import AppointmentService

router = APIRouter(
    prefix="/appointments", 
    tags=["appointments"]
)

#-----------------------------------------
# Create Appointment
#-----------------------------------------
@router.post("/", response_model=AppointmentResponse)
def create_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    service = AppointmentService(db)
    return service.create_appointment(appointment)

#-----------------------------------------
# Get All Appointments
#-----------------------------------------
@router.get("/", response_model=List[AppointmentResponse])
def get_appointments(db: Session = Depends(get_db)):
    service = AppointmentService(db)
    return service.get_appointments()

#-----------------------------------------
# Get Appointment by ID
#-----------------------------------------
@router.get("/{appointment_id}", response_model=AppointmentResponse)
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    service = AppointmentService(db)
    appointment = service.get_appointment_by_id(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

#-----------------------------------------
# Update Appointment
#-----------------------------------------
@router.put("/{appointment_id}", response_model=AppointmentResponse)
def update_appointment(appointment_id: int, appointment: AppointmentUpdate, db: Session = Depends(get_db)):
    service = AppointmentService(db)
    updated_appointment = service.update_appointment(appointment_id, appointment)
    if not updated_appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return updated_appointment

#-----------------------------------------
# Delete Appointment
#-----------------------------------------
@router.delete("/{appointment_id}")
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    service = AppointmentService(db)
    success = service.delete_appointment(appointment_id)
    if not success:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {"detail": "Appointment deleted successfully"}

#-----------------------------------------
# Get Appointments by Patient ID
#-----------------------------------------
@router.get("/patient/{patient_id}", response_model=List[AppointmentResponse])
def get_appointments_by_patient(patient_id: int, db: Session = Depends(get_db)):
    service = AppointmentService(db)
    return service.get_appointments_by_patient_id(patient_id)

#-----------------------------------------
# Get Appointments by Doctor ID
#-----------------------------------------
@router.get("/doctor/{doctor_id}", response_model=List[AppointmentResponse])
def get_appointments_by_doctor(doctor_id: int, db: Session = Depends(get_db)):
    service = AppointmentService(db)
    return service.get_appointments_by_doctor_id(doctor_id)

#-----------------------------------------
# Get Appointments by Date
#-----------------------------------------
@router.get("/date/{appointment_date}", response_model=List[AppointmentResponse])
def get_appointments_by_date(appointment_date: str, db: Session = Depends(get_db)):
    service = AppointmentService(db)
    return service.get_appointments_by_date(appointment_date)

#-----------------------------------------
# Get Appointments by Status
#-----------------------------------------
@router.get("/status/{status}", response_model=List[AppointmentResponse])
def get_appointments_by_status(status: str, db: Session = Depends(get_db)):
    service = AppointmentService(db)
    return service.get_appointments_by_status(status)



