#app/api/v1/inventory_api.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from app.schemas.inventory_schema import inventory_schema
from app.services.inventory_service import inventory_service 
from app.db.session import get_db 

router = APIRouter(prefix="/inventory", tags=["Inventory"])

@router.post("/", response_model=InventoryItemOut)
def add_item(item: inventory_schema.InventoryItemCreate, db: Session = Depends(get_db)):
	return inventory_services.create_item(db, item)
	
@router.get("/", response_model=list[inventory_schema.InventoryItemOut)
def stock_change(data: inventory_schema.StockTransactionBase, db: Session = Depends(get_db)):
	updated = inventory_service.update_stock(Db, data)
	if not updated:
		raise HTTPException(status_code=404, detail="Item not found")
	return updated 
	
@router.get("/stock", response_model=list[inventory_schema.StockTransactionOut])
def stock_change(data: inventory_schema.StockTransactionBase, db: Session = Depends(get_db)):
	updated = inventory_service.update_stock(db, data)
	if not updated:
		raise HTTPException(status_code=404, detail="Item not found")
	return updated 
	
@router.get("/{item_id}/transactions", response_model=list[inventory_schemas.StockTransactionOut])
def item_transactions(item_id: int, db: Session = Depends(get_db)):
	return inventory_service.get_transactions_for_item(db, item_id)
	
	