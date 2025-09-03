# backend/app/api/v1/appointment_api.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List 

from backend.app import models 
from backend.app.schemas import appointment_schema
from backend.app.database import get_db

router = APIRouter(
		prefix = "/api/v1/appointments",
		tags = ["Appointments"]
	)
	
	# Create an appointment 
	@router.post("/", response_model=appointment_schema.AppointmentOut, status_code=status.HTTP_201_CREATED)
    def create_appointment(appointment: appointment_schema.AppointmentCreate, db: Session = Depends(get_db)):
        new_appointment = models.Appointment(**appointment.dict())
        db.add(new_appointment)
        db.commit()
        db.refresh(new_appointment)
        return new_appointment 
        
    # Get all appointments
    @router.get("/", response_model=List[appointment_schema.Appointment])
    def get_appointement(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return db.query(models.Appointment).offset(skip).limit(limit).all()
        
    # Get appointment by ID
    @router.get("/{appointment_id}", response_model=appointment_schema.AppointmentOut)
    def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
        appointment = db.query(models.Appointment).filter(models.Appointment.appointment_id == appointment_id).first()
        if not appointment:
            raise HTTPException(status_code=404, detail="appointment not found")
        return appointment 
        
    # Update appointment 
    @router.put("/{appointment_id}", response_model=appointment_schema.Appointment)
    def  update_appointment(appointment_id: int, updated_data: appointment_schema.AppointmentUpdate, db: Session = Depends(get_db)):
        appointment = db.query(models.Appointment).filter(models.Appointment.appointment_id == appointment_id).first()
        if not appointment:
            raise HTTPException(status_code=404, detail="Appointment not found")
            
        for key, value in updated_data.dict(exclude_unset=True).items():
            setattr(appointment, key, value)
            
        db.commit()
        db.refresh(appointment)
        return appointment
        
    # Delete appointment 
    @router.delete("/{appointment_id/{appointment_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
        appointment = db.query(models.Appointment).filter(models.Appointment.appointment_id == appointment_id).first()
        if not appointment:
            raise HTTPException(status_code=404, detail="Appointment not found")
            
            db.delete(appointment)
            db.commit()
            return
            
    