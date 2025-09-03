#app/api/v1/appointment_api.py

from fastapi import APIRouter, Depends, HTTPException,
from sqlalchemy.orm import Session
from app.services.appointment_service import appointment_service 
from app.schemas.appointment_schema import appointment_schema 

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("/", response_model=appointment_schema.AppointmentOut)
def create(appointment: appointment_schema.AppointmentCreat, db: Session = Depends(get_db)):
	try:
		return appointment_service.create_appointment(db, appointment)
	except ValueError as e:
		raise HTTPException(status_code=400, detail=str(e))
		
@router.get("/{appointment_id}", response_model=appointment_schema.AppointmentOut)
def read(appointment_id: int, db: Session = Depends(get_db)):
	appointment = appointment_service.get_appointment_by_id(db, appointment_id)
	if not appointment:
		raise HTTPException(status_code=404, detail="Appointment not found")
	return appointment 
	
@router.get("/", response_model=list[appointment_schema.AppointmentOut])
def list(skip: int =0, limit: int = 100, db: Session = Depends(get_db)):
	return appointment_service.get_all_appointments(db, skip, limit)
	
@router.put("/{appointment_di}", response_model=appointment_schema.AppointmentOut)
def update(appointment_id: int, data: appointment_schema.AppointmentUpdate, db: Session = Depends(get_db)):
	updated = appointment_service.update_appointment(db, appointment_id, data)
	if not updated:
		raise HTTPException(status_code=404, detail="Appointment not found")
	return updated 
	
@router.delete("/{appointment_id}")
def delete(appointment_id: int, db: Session = Depends(get_db)):
	deleted = appointment_service.delete_appointment(db, appointment_id)
	if not deleted:
		raise HTTPException(status_code=404, detail="Appointment not found")
	return {"message": "Deleted successfully"}
	
	