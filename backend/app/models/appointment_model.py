# backend/app/models/appointment_model.py

from sqlalchemy import (
        Column, Integer, String, Enum, Text, DateTime, ForeTime, ForignKey, func
    )
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from backend.app.database import Base 

# Enum definitions
class AppointmentTypeEnum(str, PyEnum):
	Consulation = "Consulation"
	FollowUp = "Follow-up"
	Surgery = "Surgery"
	LabTest = "Lab Test"
	Emergengy = "Emergengy"
	
class AppointmentStatusEnum(str, PyEnum):
	Schedulled = "Scheduled"
	CheckedIn = "Checked-In"
	Cancelled = "Cancelled"
	NoShow = "No-Show"
	
# SQLAlchemy model
class Appointment(Base):
	__tablename__ = "appointments"
	
	appointment_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	
	patient_id = Column(Integer, ForeignKey("patients.patient_id", ondelete="CASCADE"), nullable=False)
	doctor_id = Column(Integer, ForeignKey("doctors.doctor_id", ondelete="SET NULL"), nullable=True)
	
	appointment_date = Column(DateTime, nullable=False)
    check_in_time = Column(DateTime, nullable=True)
    check_out_time = Column(DateTime, nullable=True)
    
    reason_for_visit = Column(String(255), nullable=False)
    
    appointment_type = Column(
        SqlEnum(AppointmentTypeEnum), default=AppointmentTypeEnum.Consulation, nullable=False 
    )
    status = Column(
        SqlEnum(AppointmentStatusEnum), default=AppointmentStatusEnum.Scheduled, nullable=False
    )
    duration_minutes = Column(Integer, nullable=True)
    
    notes = Column(Text, nullable=True)
    
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    updated_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    created_at = Column(DateTime(Timezone=True), server_default=func.now(), nullble=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    
    # Relationships (depend on model setup)
    patient = relationship("Patient", back_populates="appointments", lazy="joined")
    doctor = relationship("Doctor", back_populates="appointments", lazy="joined")
    creator = relationship("User", foreign_keys=[created_by], lazy="joined")
    updater = relationship("User", foreign_keys=[updated_by], lazy="joined")
    
    