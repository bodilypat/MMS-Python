#app/models/lab_model.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base 
from datetime import datetime
import Enum

class TestStatus(str, enum.Enum):
	ordered= "ordered"
	sample_collected = "sample_collected"
	processing = "processing"
	completed = "completed"
	
class LabTest(Base):
	__tablename__ = "lab_tests"
	
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, nullable=False) 
	description = Column(Text, nullable=True)
	normal_range = Column(String, nullable=True)
	unit = Column(String, nullable=True)
	
class LabOrder(Base):
	__tablename__ = "lab_orders"
	
	id = Column(Integer, primary_key=True, index=True)
	patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
	doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
	appointment_id = Column(Integer, ForeignKey("appointments.id"), nullable=True)
	test_id = Column(Integer, ForeignKey("lab_tests.id"), nullable=False)
	status = Column(Enum(TestStatus), default=TestStatus.ordered)
	result = Column(String, nullable=True)
	comments = Column(Text, nullable=True)
	ordered_at = Column(DateTime, default=datetime.utcnow)
	completed_at = Column(DateTime, nullable=True)
	
	patient = relationship("Patient")
	doctor = relationship("Doctor")
	test = relationship("LabTest")
	