#app/api/v1/appointment_api.py

from fastapi import APIRouter, Depends, HTTPException,
from sqlalchemy.orm import Session

from app.services import appointment_service 
from app.schemas import appointment_schema 
from app.db.session import get_db

router = APIRouter(prefix="/appointments", tags=["Appointments"])

# Create a new appointment
@router.post("/", response_model=appointment_schema.AppointmentOut, status_code=status.HTTP_201_CREATED)
def create_appointment(appointment: appointment_schema.AppointmentCreat, db: Session = Depends(get_db)):
	try:
		return appointment_service.create_appointment(db, appointment)
	except ValueError as e:
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# Get an appointment by Id		
@router.get("/{appointment_id}", response_model=appointment_schema.AppointmentOut)
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
	appointment = appointment_service.get_appointment_by_id(db, appointment_id)
	if not appointment:
		raise HTTPException(status_code=status.HTTP_404_FOUND, detail="Appointment not found")
	return appointment 
	
# list all appointment
@router.get("/", response_model=list[appointment_schema.AppointmentOut])
def list_appointment(skip: int =0, limit: int = 100, db: Session = Depends(get_db)):
	return appointment_service.get_all_appointments(db, skip, limit)
	
# Update appointment by ID
@router.put("/{appointment_id}", response_model=appointment_schema.AppointmentOut)
def update_appointment(appointment_id: int, data: appointment_schema.AppointmentUpdate, db: Session = Depends(get_db)):
	updated = appointment_service.update_appointment(db, appointment_id, data)
	if not updated:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")
	return updated 
	
# Delete appointment by ID
@router.delete("/{appointment_id}", status_code=status.HTTP_201_NO_CONTENT)
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
	deleted = appointment_service.delete_appointment(db, appointment_id)
	if not deleted:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")
	return None
    
	
	