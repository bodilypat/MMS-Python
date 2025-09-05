#app/models/inventory_model.py

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey 
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base 

class InventoryItem(Base):
	__tablename__ = "inventory_items"
	
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, nullable=False)
	description = Column(String(255), nullable=True)
	quantity = Column(Integer, default=0, nullable=False)
	unit = Column(String, default="pcs", nullable=False)

    purchase_price = Column(Float, default=0.0)
	selling_price = Column(Float, default=0.0)
    
	supplier = Column(String, nullable=True)
	batch_no = Column(String(50), nullable=True)
	expiry_date = Column(DateTime, nullable=True)
    
	created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
	
    # Relationships
    transactions = relationship("StockTransaction", back_populates="item", cascade="all, delete-orphan")
    
class StockTransaction(Base):
	__tablename__ = "stock_transactions"
	
	id = Column(Integer, primary_key=True, index=True)
	item_id = Column(Integer, ForeignKey("inventory_items.id", ondelete="CASCADE"), nullable=False)
	change = Column(Integer, nullable=False)
	source = Column(String(100), nullable=False)
	reference_id = Column(Integer, nullable=True)
	timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
	
# Relationships
	item = relationship("InventoryItem", back_populates="transactions") 
	