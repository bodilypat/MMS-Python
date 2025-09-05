#app/models/billing_model.py 

from sqlalchemy import (Column, Integer, Float, String, ForeignKey, DateTime, Enum as SqlEnum, func)
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base 
import enum 

#Enum
class PaymentStatusEnum(str, enum.Enum):
    pending = "pending"
    paid = "paid"
    cancelled = "cancelled"
    
class PaymentMethodEnum(str, enum.Enum):
	cash = "cash"
	card = "card"
	insurance = "insurance"
	upi = "upi"
	
# Main Bill Model
class Bill(Base):
	__tablename__ = "bills"
	
	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	patient_id = Column(Integer, ForeignKey("patients.patient_id").nullable=False)
	appointment_id = Column(Integer, ForeignKey("appointments.appointment_id"), nullable=True)
    
	amount = Column(Float, nullable=False)
	status = Column(SqlEnum(PaymentStatusEnum), default=PaymentStatusEnum.pending, nullable=False)
	method = Column(SqlEnum(PaymentMethodEnum), default=PaymentMethodEnum.cash, nullable=False)
    
    notes = Column(String(255), nullable=True)
	issued_at = Column(DateTime(timezone=True), server_default=func.now(),nullable=False)
    
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    updated_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(Datetime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
	
# Bill Item Model 
class BillItem(Base):
    __tablename__ = "bill_items"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    bill_id = Column(Integer, ForeignKey("bills.id", ondelete="CASCADE"), mullable=False)
    
    descript = Column(String(255), nullable=False)
    cost = Column(Float, nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    
# Relationship
bill = relationship("Bill", back_populates="items")
