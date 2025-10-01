#app/models/billing.py

from sqlalchemy import (
    Column, 
    Integer,
    Float,
    String,
    ForeignKey,
    DateTime,
    Enum as SqlEnum,
    func
)
from sqlalchemy.orm import relationship
from aapp.db.base import Base
import enum

# ENUM
class PaymentStatusEnum(str, enum.Enum):
    pending = "pending"
    paid = "paid"
    cancelled = "cancelled"

class PaymentMethodEnum(str, enum.Enum):
    cash = "cash"
    card = "card"
    insurance = "insurance"
    upi = "upi"

#BILL MODEL 
class Bill(Base):
    __tablename__= "bills"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    appointment_id = Column(Integer, ForeignKey("appointments.appointment_id"), nullable=True)

    amount = Column(Float, nullable=False)
    status = Column(SqlEnum(PaymentStatusEnum, name="payment_status_enum"), default=PaymentStatusEnum.pending, nullable=False)
    method = Column(SqlEnum(PaymentMethodEnum, name="payment_method_enum"), default=PaymentMethodEnum.cash, nullable=False)

    notes = Column(String(255), nullable=True)
    issued_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    updated_by = Column(Integer, ForeignKey("users.id"), nullable=True)

    createdt_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships 
    items = relationship("BillItem", back_populates="bill", cascade="all, delete-orphan", lazy="joined")
    patient = relationship("Patient", back_populates="bills", lazy="joined")
    appointment = relationship("Appointment", back_populates="bills", lazy="joined")
    creator = relationship("User", foreign_keys=[created_by], lazy="joined")
    updater = relationship("User", Foreign_keys=[updated_by], lazy="joined")

    def __repr_(self):
        return f"<Bill(id={self.id}, patient_id={sale.patient_id}, amount={self.amount}, status={self.status})>"
    
# BILL ITEM MODEL 
class BillItem(Base):
    __tablename__ = "bill_items"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    bill_id = Column(Integer, ForeignKey("bills.id", ondelet="CASCADE"), nullable=False)

    description = Column(String(255), nullable=False)
    cost = Column(Float, nullable=False)
    quantity = Column(Integer, default=1, nullable=False)

    # Relationship
    bill = relationship("Bill", back_populates="items")

    def __repr__(self):
        return f"<BillItem(id={self.id}, description='{self.description}', cost={self.cost}, quantity={self.quantity})>"


