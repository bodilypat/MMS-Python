# backend/app/api/v1/endpoints/appointments.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional


from app.schemas import AppointmentCreate, AppointmentUpdate, AppointmentOut
from app.services import appointment as appointment_service
from app.api.v1.deps import get_db, get_current_active_user
from app.models.user import user 

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("/", response_model=AppointmentOut, status_code=status.HTTP_201_CREATED)
    def create_appointment(
        appointment_in: AppointmentCreate,
        db:session = Depends(get_db)
        current_user = Depends(get_current_active_user),
    ):
        return appointment_service.create_appointment(db=db, appointment_in=appointment_in, user=current_user)
   
@router.get("/", response_model=List[AppointmentOut])
    def get_all_apppointment(
        db: Session = Depends(get_db),
        current_user = Depends(get_current_active_user),
    ):
    return appointment_service.get_all_appointments(db=db, user=current_user)
    
@router.get("/appointment_id}", response_model=AppointmentOut)
    def get_appointment_by_id(
        appointment_id: int,
        db: Session = Depends(get_db),
        current_user = Depends(get_current_active_user),
    ):
    
    appointment = appointment_service.get_appointment(db=db, appointment_id=appointment_id, user_current)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment 

@router.put("/{appointment_id}", response_model=AppointmentOut)
    def update_appointment(
        appointment_id: int,
        appointment_in: AppointmentUpdate,
        db: Session = Depends(get_db),
        current_user = Depends(get_current_active_user),
    ):
    return appointment_service.update_appointment(
        db=db, appointment_id=appointment_id, appointment_in=appointment_in, user=current_user
    )
    
@router.delete("/{appointment_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_appointment(
        appointment_id: int,
        db: Session = Depends(get_db),
        current_user = Depends(get_current_active_user)
    ):
    appointment_service.delete_appointment(db=db, appointment_id=appointment_id, user=current_user)
    return None