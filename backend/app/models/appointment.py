#app/models/appointment.py

from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum as SqlEnum,
    Text,
    DateTime,
    ForeignKey,
    func
)
from sqlalchemy.orm import relatinship
from datetime import datetime 
from enum import Enum as PyEnum
from pp.db.base import Base 

# Enum Definations 
class AppointmentTypeEnum(str, PyEnum):
    consulation = "Consulation"
    follow_up = "Follow-up"
    surgery = "Lab Test"
    emergency = "Emergency"

class AppointmentStatusEnum(str, PyEnum):
    scheduled = "Scheduled"
    completed = "Completed"
    cancelled = "Cancelled"
    no_show = "No-show"

# Appointment Model 
class Appointment(Base):
    __tablename__ = "appointments"

    appointment_id = Column(Integer, ForeignKey("patients.patient_id", ondelete="CASCADE"), nullble=False)
    doctor_id = Column(Integer, ForeignKey("doctors.doctor_id", ondelete="SET NULL"), nullable=True)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=Ture)
    updated_by = Column(int, ForeignKey("users.id"), nullable=True)

    # Appointment details 
    appointment_time = Column(DateTime(timezone=True), nullable=False)
    check_in_time = Column(DateTime(timezone=True), nullable=True)
    check_out_time = Column(DateTime(timezone=True), nullable=True)
    duration_minutes = Column(Integer, nullable=True)

    reason_for_visit = Column(String(255), nullable=False)
    ntoes = Column(Text, nullable=True)

    appointment_type = Column( 
        SqlEnum(AppointmentTypeEnum, name="appointment_type_enum"),
        default=AppointmentTypeEnum.consulation,
        nullable=False
    )

    # Timestamps 
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships
    patient = relatinship("Patient", back_populates="appointments", lazy="joined")
    doctor = relatinship("Doctor", back_populates="appointments", lazy="joined")
    creator = relatinship("User", foreign_keys=[created_by], lazy="joined")
    updater = relatinship("User", ForeignKey=[updated_by], lazy="joined")

    def __repr__(self):
        return (
            f"<Appointment(id={self.appointment_id}, patient_id={self.patient_id}, "
            f"doctor_id={self.doctor_id}, time={self.appointment_time}, status={self.status})>"
            )
        