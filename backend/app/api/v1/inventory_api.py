#app/api/v1/inventory_api.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session 
from typing import List 

from app.schemas import inventory_schema
from app.services import inventory_service 
from app.db.session import get_db 

router = APIRouter(prefix="/inventory", tags=["Inventory"])

# Create a new inventory item
@router.post("/", response_model=inventory_schema.InventoryItemOut, status_code=status.HTTP_201_CREATED)
def add_item(item: inventory_schema.InventoryItemCreate, db: Session = Depends(get_db)):
	return inventory_services.create_item(db, item)
	
# Get all inventory items 
@router.get("/", response_model=list[inventory_schema.InventoryItemOut)
def list_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
	return inventory_service.get_all_items(db, skip=skip, limit=limit) 
	
# Perform stock change 
@router.post("/stock", response_model=inventory_schema.StockTransactionOut)
def stock_change(data: inventory_schema.StockTransactionBase, db: Session = Depends(get_db)):
	updated = inventory_service.update_stock(db, data)
	if not updated:
		raise HTTPException(status_code=404, detail="Item not found or stock update failed")
	return updated 
	
# Get stock transactions for an item
@router.get("/{item_id}/transactions", response_model=list[inventory_schemas.StockTransactionOut])
def item_transactions(item_id: int, db: Session = Depends(get_db)):
	return inventory_service.get_transactions_for_item(db, item_id)
	
	