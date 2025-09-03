#app/schemas/inventory_schema.py 

from pydantic import BaseModel 
from typing import Optional
from datetime import datetime 

class InventoryItemBase(BaseModel):
	name: str
	description: Optional[str] 
	quantity: int 
	unit: str 
	purchase_price: Optional[float]
	selling_price: Optional[float] 
	supplier: Optional[str]
	batch_no: Optional[str]
	expiry_date: Optional[datetime]
	
class InventoryItemCreate(InventoryItemBase):
	pass 

class InventoryItemOut(InventoryItemBase):
	id: int 
	created_at: datetime
	
	class Config:
		orm_mode = True 
		
class StockTransactionBase(BaseModel):
	item_id: int 
	change: int 
	source: str 
	reference_id: Optional[int]
	
class StockTransactionOut(StockTransactionBase):
    id: int
    timestamp: datetime 
    
    class Config:
        orm_mode = True 
        
        