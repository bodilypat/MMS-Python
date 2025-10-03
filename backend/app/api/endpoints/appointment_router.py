#app/api/endpoints/appointment_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session 
from typing import List 

from app.schemas.appointment import AppointmentCreate, AppointmentUpdate, AppointmentRead 
from app.services import appointment_service as AppointmentService
from app.db.session import get_db 

router = APIRouter(
        prefix="/appointments", tags=["Appointments"]
)

@router.get("/", response_model=List[AppointmentRead], summary="List all of appointments")
def list_appointments(
        skip: int = Query(0, ge=0, description="Number of records to skip"),
        limit: int =Query(10, le=100, description="Maximum number of records to return"),
        db: Session = Depends(get_db)
    ):
    return AppointmentService(db).get_all_appointment(skip=skip, limit=limit)

@router.get("/{appointment_id}", response_model=AppointmentRead, summary="Get a single Appointment by ID")
def read_appointment(
        appointment_id: int,
        db: Session = Depends(get_db)
    ):
    return AppointmentService(db).get_appointment_by_id(appointment_id)

@router.post("/", response_model=AppointmentRead, status_code=status.HTTP_201_CREATED, summary="Appointment of found")
def create_appointment( 
        appointment_info: AppointmentCreate,
        db: Session = Depends(get_db)
    ):
    return AppointmentService(db).create_appointment(appointment_info)

@router.put("/{appointment_id}", response_model=AppointmentRead, summary="update an existing appointment")
def update_appointment(
        appointment_id: int,
        updated_appointment: AppointmentUpdate,
        db: Session = Depends(get_db)
    ):

    updated = AppointmentService(db).update_appointment(appointment_id,updated_appointment)
    if not updated:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return updated 

@router.delete("/{appointment_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Appointment")
def delete_appointment(
        appointment_id: int,
        db: Session = Depends(get_db)
    ):
    appointment = AppointmentService(db).delete_appointment(appointment_id)

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
