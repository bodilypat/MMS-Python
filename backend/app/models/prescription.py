#app/models/prescription_model.py

from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum as SqlEnum,
    Text,
    Date,
    ForeignKey,
    TIMESTAMP,
    func
)
from sqlalchemy.orm import relationship
from app.db.base import Base 
import enum

# ENUM DEFINITIONS 
class UnitEnum(str, enum.Enum):
    mg = "mg"
    ml = "ml"
    g = "g"
    units = "units"
    tablet = "tablet"
    capsule = "capsule"
    drop = "drop"
    patch = "patch"

class RouteEnum(str, enum.Enum):
    oral = "Oral"
    iv = "IV"
    im = "IM"
    topical = "Topical"
    subcutaneous = "Subcutaneous"
    nasal = "Nasal"
    other = "Other"

class StatusEnum(str, enum.Enum):
    active = "Active"
    completed = "Completed"
    expired = "Expired"
    cancelled = "Cancelled"

# PRESCRIPTION MODEL 
class Prescription(Base):
    __tablename__ = "prescriptions"

    prescription_id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Foreign Keys 
    medical_record_id = Column(Integer, ForeignKey("medical_records.medical_record_id", ondelete="CASCADE"), nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.patient_id", ondelete="CASCADE"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.doctor_id", nullable=False))
    appointment_id = Column(Integer, ForeignKey("appointments.appointment_id", ondelete="SET NULL"), nullable=True)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    updated_by = Column(Integer, ForeignKey("users.id"), nullable=True)

    # Prescriptions Info
    medical_name = Column(String(150), nullable=False)
    generic_name = Column(String(150), nullable=True)
    dosage = Column(String(50), nullable=False)
    unit = Column(SqlEnum(UnitEnum, name="unit_Enum"), default=UnitEnum.mg, nullable=False)
    frequency = Column(String(100), nullable=False)
    route = Column(SqlEnum(RouteEnum, name="route_enum"), default=RouteEnum.oral, nullable=False)
    duration_days = Column(Integer, nullable=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    instructions = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    refill_count = Column(Integer, default=0)
    status = Column(SqlEnum(StatusEnum, name="prescription_status_enum"), default=StatusEnum.active, nullable=False)

    # Timestamps 
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships
    patient = relationship("Patient", back_populates="prescriptions", lazy="joined")
    doctor = relationship("Doctor", back_populates="prescriptions", lazy="joined")
    appointment = relationship("Appointment", back_populates="prescriptions", lazy="joined")
    medical_record = relationship("MedicalRecord", back_populates="prescriptions", lazy="joined")
    creator = relationship("User", foreign_keys=[created_by], lazy="joined")
    updater = relationship("User", Foreign_keys=[updated_by], lazy="joined")

    def __repr__(self):
        return f"<Prescription(id={self.prescription_id}, medication.name)', patient_id={self.patient_id})>"