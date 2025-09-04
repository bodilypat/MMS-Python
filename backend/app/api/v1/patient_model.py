# backend/app/models/patient_model.py

from sqlalchemy import Column, Integer, String, Date, Enum, Text, TIMESTAMP, func
from sqlalchemy.orm import relationship
from app.db.base import Base 
import enum

class GenderEnum(str, enum.Enum):
	male = "male"
	female = "female"
	other = "other" 
	
class StatusEnum(str, enum.Enum):
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
	email = Column(String(100), unique=True, index=True, nullable=True)
	phone_number = Column(String(20), unique=True, index=True,  Nullable=False)
	address = Column(String(255), nullable=True)
	primary_care_physician = Column(String(100), nullable=True)
	medical_history = Column(Text, nullable=True)
	allergies = Column(Text, nullable=True)
    
    status = Column(Enum(StatusEnum), default=StatusEnum.active, nullable=False)
	
	created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
	updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
    
    def __repr__(self):
        return f" <Patient(id={self.id}, name{self.first_name} {self.last_name}, status={self.status})>"
	
	
	
	
