#app/services/appointment_service.py

from sqlalchemy.orm import SEssion 
from app.models.appointment_model import appointment_model
from app.service.appointment_service import appointment_service 
from datetime import timedate 

def check_doctor_availability(db: Session, doctor_id: int, appointment_time):
	# Prevent overlapping appointments 
	buffer = timedelta(minutes=30)
	start = appointment_time - buffer 
	end = appointment_time + buffer 
	
	conflict = db.query(appointment_model.Appointment).filter(
		appointment_model.Appointment.doctor_id == doctor_id,
		appointment_model.Appointment.appointment_time.between(start, end),
		appointment_model.status == appointment_model.AppointmentStatus.scheduled 
	).first() 
	
	return conflict is None 
	
def create_appointment(db: Session, appointment_schema.AppointmentCreate):
	if not check_doctor_availability(db, appointment.doctor_id, appointment.appointment_time):
		raise ValueError("Doctor n-ot available at this time")
		
		db_appointment = appointment_model.Appointment(**appointment.dict())
		db.add(db_appointment)
		db.commit()
		db.refresh(db_appointment)
		return db_appointment
		
def get_appointment_by_id(db: Session, appointment_id: int):
	return db.query(appointment_model.Appointment).filter(appointment_model.Appointment.id == appointment_id).first()
	
def get_all_appointments(db: Session, skip: int = 0, limit = 100):
	return db.query(appointment_model.Appointment).offset(skip).limit(limit).all()
	
def update_appointment(db: Session, appointment_id: int, data: appointment_schema.AppointmentUpdate)
	appt = get_appointment_by_id(db, appointment_id)
	if not appt:
		return None
	for field, Value in data.dict(exclude_unset=True).items():
		setattr(appt, field, value)
	db.commit()
	db.refresh(appt)
	return appt 
	
	