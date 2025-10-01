#app/models/doctor.py

from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum,
    Text,
    Date,
    ForeignKey,
    TIMESTAMP,
    func
)
from sqlalchemy.orm import relationship
from app.db.base import Base 
import enum

class GenderEnum(str, eum.Enum):
    male = "male"
    female = "famale"
    other = "other"
    
class DoctorStatusEnum(Str, enum.Enum):
    active = "active",
    inactive = "inactive"
    retired = "retired"
    on_leave = "on_leave"

class Doctor(Base):
    __tablename__ = "doctors"

    doctor_id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Personal Info
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    birthdate = Column(Date, nullable=True)
    gender = Column(Enum(GenderEnum, name="gender_enum"), default=GenderEnum.other, nullable=False)
    address = Column(String(255), nullable=True)

    # Professional Info
    specialization = Column(String(100), nullable=False)
    department = Column(String(100), nullable=True)
    status = Column(Enum(DoctorStatusEnum, name="doctor_status_enum"), default=DoctorStatusEnum.active, nullable=False)
    hire_date = Column(Date, nullable=True)
    notes = Column(Text, nullable=True)

    # Contact 
    email = Column(String(150), unique=True, nullable=False)
    phone_number = Column(String(20), unique=True, nullable=False)

    # Metadata 
    created_by = Column(Integer, ForeignKey("users_id"), nullable=True)
    updated_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=True)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=funct.now(), nullable=False)

    # Relationships (optional)
    created_user = relationship("Users", foreign_keys=[created_by], backref="created_doctors")
    updated_user = relationship("Users", foreign_keys=[updated_by], backref="updated_doctors")

    def __repr__(self):
        return (
            f"<Doctor(doctor_id={self.doctor_id}, "
            f"name='{self.first_name} {self.last_name}', "
            f"status={self.status})>"
        )
