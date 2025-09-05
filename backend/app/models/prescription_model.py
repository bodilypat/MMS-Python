# app/models/prescription_model.py

from sqlalchemy import(
	Column, Integer, String, Enum as SqlEnum, Text, Date, ForeignKey, TIMESTAMP, func
	)
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum

# Enums matching schema
class UnitEnum(str, enum.Enum):
	mg: 'mg'
	ml = 'ml'
	g = 'g' 
	units = 'units'
	tablet = 'tablet'
	capsule = 'capsule'
	drop = 'drop'
	patch = 'patch'
	
class RouteEnum(str, enum.Enum):
	oral = 'Oral'
	iv = 'IV'
	im = 'IM'
	topical = 'Topical'
	subcutaneous = 'Subtaneous'
	nasal = 'Nasal'
	other = 'Other'
	
class StatusEnum(str, enum.Enum):
	active: 'Active'
	completed = 'Completed'
	expired = 'Expired'
	cancelled = 'Cancelled'
	
class Prescription(Base):
    __tablename__ = 'prescriptions'
    
    prescription_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    record_id = Column(Integer, ForeignKey('medical_records.record_id', ondelete="CASCADE"), nullable=False)
    patient_id = Column(Integer, ForeignKey('patients.patient_id', ondelete="CASCADE"), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.doctor_id'), nullable=False)
    appointment_id = Column(Integer, ForeignKey('appointments.appointment_id', ondelete="SET NULL"), nullable=True)
    
    medication_name = Column(String(150), nullable=False)
    generic_name = Column(String(150), nullable=True)
    dosage = Column(String(50), nullable=False)
    unit = Column(Enum(UnitEnum), default=UnitEnum.mg, mullable=False)
    frequency = Column(String(100), nullable=False)
    route = Column(Enum(RouteEnum), default=RouteEnum.oral, nullable=False)
    duration_days = Column(Integer, nullable=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    
    instructions = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    refill_count = Column(Integer, default=0)
    status = Column(SqlEnum(StatusEnum), default=StatusEnum.active, nullable=False)
    
    created_by = Column(Integer, ForeignKey('users.id'), nullable=True)
    updated_by = Column(Integer, ForeignKey('users.id'), nullable=True)
    
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate.func.now(), nullable=False)
    
    # Relationships 
    patient = relationship("Patient", back_populates="prescriptions")
    doctor = relationship("Doctor", back_populates="prescriptions")
    appointment = relationship("Appointment", back_populates="prescriptions", lazy='joined')
    medical_record = relationship("MedicalRecord", back_populates="prescriptions")

