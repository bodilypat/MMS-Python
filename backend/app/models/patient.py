#app/models/patient.py

from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, index=True)

    # Optional link to user account (patient portal)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True, unique=True)
    
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String, nullable=False)

    phone_number = Column(String, nullable=True)
    email = Column(String, nullable=True, unique=True)
    address = Column(String, nullable=True)

    blood_group = Column(String, nullable=True)
    allergies_info = Column(String, nullable=True)
    emergency_contacts_info = Column(String, nullable=True)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="patient", uselist=False)
    appointments = relationship("Appointment", back_populates="patient", cascade="all, delete-orphan")
    medical_records = relationship("MedicalRecord", back_populates="patient", cascade="all, delete-orphan")
    prescriptions = relationship("Prescription", back_populates="patient", cascade="all, delete-orphan")
    billing_records = relationship("BillingRecord", back_populates="patient", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Patient(id={self.id}, name={self.first_name} {self.last_name})>"
    
