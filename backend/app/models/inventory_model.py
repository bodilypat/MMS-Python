#app/models/inventory_model.py

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey 
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base 

class InventoryItem(Base):
	__tablename__ = "inventory_items"
	
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, nullable=False)
	description = Column(String)
	quantity = Column(Integer, default=0)
	unit = Column(String, default="pcs") 
	selling_price = Column(Float, default=0.0)
	selling_price = Column(Float, default=0.0)
	supplier = Column(String, nullable=True)
	batch_no = Column(String, nullable=True)
	expiry_date = Column(DateTime, nullable=True)
	created_at = Column(DateTime, default=datetime.utcnow)
	
class StockTransaction(Base):
	__tablename__ = "stock_transactions"
	
	id = Column(Integer, primary_key=True, index=True)
	item_id = Column(Integer, ForeignKey("inventory_items.id"), nullable=False)
	change = Column(Integer, nullable=False)
	source = Column(String)
	reference_id = Column(Integer, nullable=True)
	timestamp = Column(DateTime, default=datetime.utcnow)
	
	item = relationship("InventoryItem") 
	