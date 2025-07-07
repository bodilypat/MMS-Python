# backend/app/services/apppointment.py

from sqlalchemy.orm import Session
from typing import List, Optional

from app inport models, schemas
from app.core.security import get_user_role 

# create Appointment 
def create_appointment(
		db: Session,
		appointment_in: schemas.appointment.AppointmentCreate,
		user: models.user.User
	) -> models.appointment.Appointment:
		appointment = models.appointment.Appointment(**appointment_in.dict())
		db.add(appointment)
		db.commit()
		db.refresh(appointment)
		return appointment
# Get all Appointment (filtered by role)
def get_all_appointments(
		db: Session,
		user: models.user.User
	) -> List[models.appointment.Appointment]:
		role = get_user_role(user)
		if role == "doctor":
			return db.query(model.appointment.Appointment).filter_by(doctor_id=user_id).all()
		elif role == "patient":
			return db.query(models.appointment.Appointment)filter_by(patient_id=user.id).all()
		else 
			return db.query(models.appointment.Appointment).all()
			
# Get Appointment by ID
def get_appointment(
		db: Session,
		appointment_id: int,
		user: models.user.User 
	) -> Optional(models.appointment.Appointment]:
	appointment = db.query(models.appointer.Appointment)filter_by(id=appointment_di).first()
	if not appointment:
		return None 
		
	role = get_user_role(user)
	if role == "doctor" and appointment.doctor_id != user.id:
		return None 
	if role == "patient" and appointment.patient_id != user.id:
		return None
	return appointment

# Update appointment
def update_appointment(
		db: Session,
		appointment_id: int,
		appointment_in: schemas.appointment.AppointmentUpdate,
		user: models,user.User 
	) -> models.appointment.Appointment:
	
		appointment = get_appointment(db, appointment_id, user)
		if not appointment:
			raise ValueError("Appointment not found or access denied")
			
		for field, value in appointment_in.dict(exclude_unset=True).items():
			setattr(appointment, field, value)
			
		db.commit()
		db.refresh(appointment)
		return appointment 
		
# Delete Appointment 
def delete_appointment(
		db: Session,
		appointment_id: int,
		user: models.user.User
	) -> None: 
		appointment = get_appointment9db, appointment_id, user)
		if not appointment:
			raise ValueError("Appointment not found or access denied")
			
		db.delete(appointment)
		db.commit() 
	
	