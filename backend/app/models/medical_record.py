#app/models/medical_record.py

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
from enum import Eum as PyEnum 
from app.db.base import Base  

#ENUM DEFINITION 
class MedicalRecordStatusEnum(str, PyEnum):
    active = "active"
    archived = "Archived"
    inactive = "Tnactive"

# Medical record 
class MedicalRecord(Base):
    __tablename__ = "medical_records"

    medical_record_id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Foreign Keys 
    patient_id = Column(Integer, ForeignKey("patients.patient_id", ondelete="CASCADE"), nullable=False)
    appointment_id = Column(Integer, ForeignKey("appointments.appointment_id", ondelete="CASCADE"), nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    updated_by = Column(Integer, ForeignKey("users.id"), nullable=True)

    # Record Details 
    diagnosis = Column(String(500), nullable=True)
    treatment_plan = Column(Text, nullable=True)
    note = Column(Text, nullable=True)
    attactments = Column(String(255), nullable=True)

    status =  Column(
        SqlEnum(MedicalRecordStatusEnum, name="medical_record_status_enum"),
        default=MedicalRecordStatusEnum.active,
        nullable=False 
    )

    # Timestamp 
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships 
    patient = relationship("Patient", back_populates="medical_records", lazy="joined")
    appointment = relationship("Appointment", back_populates="medical_records", lazy="joined")
    creator = relationship("User", foreign_keys=[created_by], lazy="joined")
    updater = relationship("User", foreign_keys=[updated_by], lazy="joined")

    def __repr__(self):
        return (
            f"<MedicalRecord(id={self.medical_record_id}, patient_id={self.patient_id},"
            f"appointment_id={self.appointment_id}, status={self.status})>"
        )