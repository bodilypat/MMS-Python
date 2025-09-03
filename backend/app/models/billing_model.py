#app/models/billing_model.py 

from sqlalchemy.orm import Column, Integer, Float, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base 
import enum 

class PaymentStatus(str, enum, Enum):
	cash = "cash"
	card = "card"
	insurance = "insurance"
	upi = "upi"
	
class Bill(Base):
	__tablename__ = "bills"
	
	id = Column(Integer, primary_key=True, index=True)
	patient_id = Column(Integer, ForeignKey("patient.id").nullable=False)
	appointment_id = Column(Integer, ForeignKey("appointment.id"), nullable=True)
	amount = Column(Float, nullable=False)
	status = Column(Enum(PaymentStatus), default=PaymentStatus.pending)
	method = Column(Enum(PaymentMethod), default=PaymentMethod.cash)
	issued_at = Column(DateTime, default=datetime.utcnow)
	notes = Column(String(255), nullable=True)
	
	patient = relationship("Patient")
	appointment = relationship("Appointment")
	items = relationship("BillItem", back_populates="bill")
	
class billItem(Base):
	__tablename__ = "bill_items"
	
	id = Column(Integer, primary_key=True, index=True0
	bill_id = column(Inteter, ForeignKey("bills.id"), nullable=False)
	description = Column(String(255), nullable=False)
	cost = Column(Float, nullable=False)
	
	bill = relationship("Bill", back_populates="items")
	