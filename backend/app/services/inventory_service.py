#app/services/inventory_service.py 

from sqlalchemy.orm import Session 
from app.services.inventory_model import inventory_model
from app.schemas.inventory_schema import inventory_schema

def create_item(db: Session, item: inventory_schema.InventoryItemCreate):
	db_item = models.InventoryItem(**item.dict())
	db.add(db_item)
	db.commit()
	db.refresh(db_item)
	return db_item 
	
def list_items(db: Session):
	return db.query(inventory_model.InventoryItem).all()

def update_stock(db: Session, data: inventory_schema.StockTransactionBase):
	item = db.query(inventory_model.InventoryItem).filter(inventory_model.InventoryItem.id == data.item_id).first()
	if not item:
		return None 
	item.quantity += data.change
	transaction = inventory_model.StockTransaction(**data.dict())
	db.add(transaction)
	db.commit()
	db.refresh(item)
	return item 
	
def get_transactions_for_item(db: Session, item_id: int):
	return db.query(inventory_model.StockTransaction).filter_by(item_id=item_id).all() 
	