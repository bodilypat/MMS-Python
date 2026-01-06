# app/models/appointment.py

from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey,
    Text,
    Enum,
    Index,
)

from sqlalchemy.orm import relationship
from app.database import Base 
from app.core.costants import AppointmentStatus

class Appointment(Base):
    __tablename__ = "appointments"

#----------------------------------------------
# Primary key 
#----------------------------------------------
    id = Column(Integer, primary_key=True, index=True)

#----------------------------------------------
# Foreign keys and other fields
#----------------------------------------------
    patient_id = Column(
        Integer, 
        ForeignKey("patients.id", ondelete="CASCADE"), 
        nullable=False,
        index=True
    )
    doctor_id = Column(
        Integer,
        ForeignKey("doctors.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

#----------------------------------------------
# Appointment details
#----------------------------------------------
    appointment_date = Column(
        DateTime(timezone=True),
        nullable=False,
        index=True,
    )
    status = Column(
        Enum(AppointmentStatus, name="appointment_status"),
        nullable=False,
        default=AppointmentStatus.SCHEDULED,
        index=True,
    )
    
    reason = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)

#----------------------------------------------
# Audit fields
#----------------------------------------------
    created_at = Column(
        DateTime(timezone=True), 
        nullable=False,
        default=datetime.utcnow,
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

#----------------------------------------------
# Relationships
#----------------------------------------------
    patient = relationship(
        "Patient", 
        back_populates="appointments",
        lazy="joined",
    )

    doctor = relationship(
        "Doctor", 
        back_populates="appointments",
        lazy="joined",
    )

    prescriptions = relationship(
        "Prescription", 
        back_populates="appointment", 
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    medical_records = relationship(
        "MedicalRecord",
        back_populates="appointment",
        cascade="all, delete-orphan",
        lazy="selectin",
    )
 
#----------------------------------------------
# Table Indexes (Performance )
#----------------------------------------------
    __table_args__ = (
        Index(
            'ix_appointment_patient_date', 
            'patient_id', 
            'appointment_date'
        ),
        Index(
            'ix_appointment_doctor_date', 
            'doctor_id', 
            'appointment_date'
        ),
        Index(
            'ix_appointment_status_date', 
            'status', 
            'appointment_date'
        ),
    )

#----------------------------------------------
# String Representation
#----------------------------------------------
    def __repr__(self):
        return (
            f"<Appointment("
            f"id={self.id}, "
            f"patient_id={self.patient_id}, "
            f"doctor_id={self.doctor_id}, "
            f"appointment_date={self.appointment_date}, "
            f"status={self.status})>"
            f")>"
        )
    