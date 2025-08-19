# backend/app/models/payment_model.py

from sqlalchemy import Column, Integer, String, Enum, as SqlEnum, Text, DateTime, ForeignKey, Numeric, func
from sqlalchemy.orm import relationship
from enum import Enum
from backend.app.database import Base 

# Enum Definitions
class PaymentStatusEnum(str, Enum):
	Paid = "Paid"
	PartiallyPaid = "Partially Paid"
	Pending = "Pending"
	Overdue = "Overdue"
	Refunded = "Refunded"
	
class PaymentMethodEnum(str, Enum):
	Cash = "Cash"
	CreditCard = "Credit Card"
	Insurance = "Insurance"
	Online = "Online"
	BankTransfer = "Bank Transfer"
	Other = "Other"
	
class InsuranceStatusEnum(str, Enum):
	Approved = "Approved"
	Pending = "Pending"
	Denied = "Denied"
	NotApplicable = "Not Applicable"
	
# Payment Model 
class Payment(Base):
	__tablename__ = "payments"
	
	payment_id = Column(Integer, ForeignKey("patients.patients_id", ondelete="CASCADE"), mullable=False)
	appointment_id = Column(Integer, ForeignKey("appointments.appointment_id", ondelete="CASCADE"), nullable=False)
	
	total_amount = Column(Numeric(10,2), nullable=False)
	amount_paid = column(Numeric(10,2), nullable=False, default=0.00)
	refund_amount = Column(Numeric(10,2), nullable=False, default=0.00)
	
	payment_status = Column(SqlEnum(PaymentStatusEnum), nullable=False, default=PaymentStatusEnum.Pending)
	payment_method = Column(SqlEnum(PaymentMethodEnum), nullable=False, default=PaymentMethodEnum.Cash)
	
	transaction_reference = Column(String(100), nullable=True)
	payment_date = Column(DateTime, nullable=False, server_default=func.now())
	
	insurance_claimed_amount = Column(Numeric(10,2), numable=False, default=0.0)
	insurance_status = Column(InsuranceStatusEnum), nullable=False, default=InsuranceStatusEnum.NotApplicable)
	insurance_provider = Column(100), nullable=True)
	
	notes = Column(Text, nullable=True)
	
	created_by = Column(Integer, ForeignKey("users.id"), nullable=True
	updated_by = Column(Integer, ForeignKey("users.id"), nullable=True)
	
	created_at = Coumnn(Datetime(timezone=True), server_default=func.now(), nullable=False)
	updated_by = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
	
	# Relationship
	patient = relationship("Patient", back_populates="payments", lazy="joined")
	appointment = relationship("Appointment", back_appointment="payments", lazy="joined")
	creator = relationship("User", foreign_keys=[created_by], lazy="joined")
	updater = relationship("User", foreign_keys=[updated_by], lazy="joined")
	