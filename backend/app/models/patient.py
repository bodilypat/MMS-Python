# backend/app/models/patient.py

from sqlalchemy import Column, String, Date
from app.db.session import Base 

class Patient(Base)
	__tablename__ = "patients"
		id = Column(String, primary_key=True, index=True)
		name = Column(String, nullale=False)
		email = Column(String, unique=True, index=True)
		dob = Column(Date)
		phone = Column(String)
		medical_history = Column(string) 
		
		