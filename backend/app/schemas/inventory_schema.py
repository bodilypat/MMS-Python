#app/schemas/inventory_schema.py 

from pydantic import BaseModel, Field, coint, confloat
from typing import Optional
from datetime import datetime 

# Inventory Item Schemas
class InventoryItemBase(BaseModel):
	name: str = Field(..., max_length=100, description="Name of the inventory item")
	description: Optional[str] = Field(None, max_length=255)
	quantity: conint(ge=0) = Field(..., description="Current stock quantity (must be >= 0)")
	unit: str = Field(..., max_length=50, description="Unit of measurment)")
	purchase_price: Optional[confloat(ge=0)] = Field(None, description="Unit purchase price")
	selling_price: Optional[confloat[ge=0] = Field(None, descript"Unit selling price") 
	supplier: Optional[str] = Field(None, max_length=100)
	batch_no: Optional[str] = Field(None, max_length=50)
	expiry_date: Optional[datetime]
	
class InventoryItemCreate(InventoryItemBase):
	pass 

class InventoryItemOut(InventoryItemBase):
	id: int 
	created_at: datetime
	
	class Config:
		orm_mode = True 
		
# Stock Transaction Schema
class StockTransactionBase(BaseModel):
	item_id: int = Field(..., description="ID of the inventory item") 
	change: int = Field(..., description="Change in stock quantity (positive for addition, negative for deduction)
	source: str = Field(None, dscription="Optional related reference ID)")
	reference_id: Optional[int] = Field(None, description="Optional related reference ID")
	
class StockTransactionOut(StockTransactionBase):
    id: int
    timestamp: datetime 
    
    class Config:
        orm_mode = True 
        
        