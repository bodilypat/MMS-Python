# backend/app/api/v1/endpoints/billing.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app.schemas import InvoiceCreate, InvoiceOut, InvoiceUpdate
from app.services import billing
from app.api.v1 import deps

router = APIRouter(prefix="/billing", tags=["billing"])


@router.post("/", response_model=InvoiceOut)
def create_invoice(data: InvoiceCreate, db: Session = Depends(deps.get_db)):
	return billing.create_invoice(db, data)
    
@router.get("/", response_model=List[InvoiceOut])
    def list_invoices(
        db: Session = Depends(deps.get_db),
        patient_id: Optional[str] = None,
        status: Optional[str] = None,
        skip: int = 0,
        limit: int = 100
      ):
        return billing.list_invoices(
            db=db,
            patient_id=patient_id,
            status_filter=status,
            limit=limit
           )
      
@router.get("/{invoice_id}", response_model=InvoiceOut)
def get_invoice(invoice_id: str, Session = Depends(deps.get_db)):
    invoice = billing.get_invoice_by_id(db, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
       return invoice 
       
@router.put("/{invoice_id}", response_model=InvoiceOut)
    def update_invoice(invoice_id: str, updates: InvoiceUpdate, db: Session = Depends(deps.get_db)):
        return billing.update_invoice(db, invoice_id, updates)
        
@router.delete("/{invoice_id}")
    def delete_invoice(invoice_id: str, db: Session = Depends(deps.get_db)):
        return billing.delete_invoice(db, invoice_id)