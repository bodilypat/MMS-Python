#app/services/inventory_service.py 

from sqlalchemy.orm import Session 
from app.models import inventory_model
from app.schemas import inventory_schema
from typing import List, Optional

def create_item(db: Session, item: inventory_schema.InventoryItemCreate) -> inventory_model.InventoryItem:
	db_item = inventory_model.models.InventoryItem(**item.dict())
	db.add(db_item)
	db.commit()
	db.refresh(db_item)
	return db_item 
	
def get_all_items(db: Session, skip: int = 0, limit: int = 100) -> List[inventory_model.Inventory]:
	return db.query(inventory_model.InventoryItem).offset(skip).limit(limit).all()

def update_stock(db: Session, data: inventory_schema.StockTransactionBase)-> Optional[inventory_model.InventoryItem]:
	item = db.query(inventory_model.InventoryItem).filter(inventory_model.InventoryItem.id == data.item_id).first()
	if not item:
		return None 
    # Update quantity safely 
    new_quantity = item.quantity + data.change
    if new_quanity < 0:
        raise ValueError("Stock quantity cannot be negative")
	item.quantity = new_quantity
    
    # Create stock transaction record 
	transaction = inventory_model.StockTransaction(**data.dict())
	db.add(transaction)
    
	db.commit()
	db.refresh(item)
	return item 
	
def get_transactions_for_item(db: Session, item_id: int) -> List(inventory_model.StockTransaction]:
	return db.query(inventory_model.StockTransaction).filter_by(item_id=item_id).all() 
	