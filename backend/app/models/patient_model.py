# backend/app/models/patient_model.py

from sqlalchemy import ( Column, Integer, String, Date, Enum, Text, TIMESTAMP, func)
from sqlalchemy.orm import relatioship
from app.db.base import Base 
import enum

class GenderEnum(str, enum, Enum):
	male = "male"
	female = "female"
	other = "other" 
	
class StatusEnum(str, enum, Enum):
	active = "active"
	inactive = "inactive"
	deceased = "deceased" 
	
class Patient(Base):
	__tablename__ = "patients"
	
	patient_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	first_name = Column(String(100), nullable=False)
	last_name = Column(String(100), nullable=False)
	date_of_birth = Column(Date, nullable=False)
	gender = Column(Enum(GenderEnum), nullable=False)
	email = Column(String(100), unique=True)
	phone_number = Column(String(20), unique=True, Nullable=False)
	address = Column(String(255))
	primary_care_physician = Column(String(100))
	medical_history = Column(Text)
	allergies = Column(Text)
	
	created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
	updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
	
	status = Column(Enum(StatusEnum), default=StatusEnum.active, nullable=False)
	
	
