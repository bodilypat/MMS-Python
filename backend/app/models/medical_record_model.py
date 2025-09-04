#app/models/medical_record_model.py

from sqlalchemy import (
		Column,
		Integer,
		String,
		Text,
		Enum as SqlEnum,
		ForeignKey,
		TIMESTAMP,
		func
	)
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from app.db.base import Base 

# Status Enum definition 
class MedicalRecordStatusEnum(str, PyEnum):
	Active = "Active"
	Archived = "Archived"
	Inactive = "Inactive"
	
class MedicalRecord(Base):
	__tablename__ = "medical_records"
	
	medical_record_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	
	patient_id = Column(Integer, ForeignKey("patients.patient_id", ondelete="CASCADE"), nullable=False)
	appointment_id = Column(Integer, ForeignKey("appointments.appointment_id", ondelete="CASCADE"), nullable=False)
	
	diagnosis = Column(String(500), nullable=True)
	treatment_plan = Column(Text, nullable=True)
	note = Column(Text, nullable=True)
	
	status = Column(SqlEnum(MedicalRecordStatusEnum), default=MedicalRecordStatusEnum.Active, nullable=False)
	
	attactments = Column(String(255), nullable=True)
	
	created_at = Column(TIMESTAMP, server_default=func.new(), nullable=False)
	updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
	
	created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
	updated_by = Column(Integer, ForeignKey("users.id"), nullable=True)
	
	# Relationship 
	patient = relationship("Patient", back_populates= "medical_records", lazy="joined")
	apppointment = relationship("Appointment", back_populates="medical_records", lazy="joined")
	creator = relationship("User", foreign_keys=[created_by], lazy="joined")
	updator = relationship("User", foreign_keys=[updated_by], lazy="joined")