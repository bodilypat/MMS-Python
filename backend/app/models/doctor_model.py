# backend/app/models/doctor_model.py

from sqlalchemy import ( Column, Integer, String, Enum, Text, Date, ForeignKey, TIMESTAMP, func )
from sqlalchemy.orm import relationship
from app.db.base import Base 
import enum

class GenderEnum(str, enum.Enum):
	male = "male"
	female = "female"
	other = "other"
	
class DoctorStatusEnum(str, enum.Enum):
	active = "active"
	inactive = "inactive"
	retired = "retired"
	on_leave = "on_leave"
	
class Doctor(Base):
	__tablename__ = "doctors" 
	
	doctor_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	first_name = Column(string(100), nullable=False)
	last_name = Column(String(100), nullable=False)
	specialization = Column(String(100), nullable=False)
	department = Column(String(100), nullable=True)
	email = Column(String(150), nullable=False, unique=True)
	phone_number = Column(String(20), nullable=False, unique=True)
	birthdate = Column(Date, nullable=True)
	gender = Column(Enum(GenderEnum), default=GenderEnum.other, nullable=False)
	address = Column(String(255), nullable=True)
	
	status = Column(Enum(DoctorStatusEnum), default=DoctorStatusEnum.active, nullable=False)
	hire_date = Column(Date, server_default=func.current_date(), nullable=False)
	retirement_date = Column(Date, nullable=True)
	notes = Column(Text, nullable=True)
    
	created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
	updated_by = Column(Integer, ForeignKey("users.id"), nullable=True)
	
	created_at = Column(TIMESTAMP, server_default=func.now(), nullable=True)
	updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
    
    def __repr__(self):
        return f"<Doctor(id={self.id}, name={self.first_name} {self.last_name}, status={self.status})>"
	
	