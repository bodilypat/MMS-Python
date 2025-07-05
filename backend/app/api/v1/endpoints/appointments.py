# backend/app/api/v1/endpoints/appointments.py

from fastapi import APIRouter
from app.schemas import AppointmentCreate 
from app.services.appointment import create_appointment

router = APIRouter("/")
def book_appointment(data: AppointmentCreate):
	return create_appointment(data)
	