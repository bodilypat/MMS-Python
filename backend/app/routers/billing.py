#app/routers/billings.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.billing import BillingCreate, BillingUpdate, BillingResponse
from app.database import get_db
from app.services.billing_service import BillingService

router = APIRouter(
    prefix="/billings",
    tags=["billings"],
)

#--------------------------------------
# Create a new billing record
#--------------------------------------
@router.post("/", response_model=BillingResponse)
def create_billing(
    billing: BillingCreate,
    db: Session = Depends(get_db),
):
    billing_service = BillingService(db)
    return billing_service.create_billing(billing)

#--------------------------------------
# Get a billing record by ID
#--------------------------------------
@router.get("/{billing_id}", response_model=BillingResponse)
def get_billing(
    billing_id: int,
    db: Session = Depends(get_db),
):
    billing_service = BillingService(db)
    billing_record = billing_service.get_billing(billing_id)
    if not billing_record:
        raise HTTPException(status_code=404, detail="Billing record not found")
    return billing_record

#--------------------------------------
# Update a billing record by ID
#--------------------------------------
@router.put("/{billing_id}", response_model=BillingResponse)
def update_billing(
    billing_id: int,
    billing: BillingUpdate,
    db: Session = Depends(get_db),
):
    billing_service = BillingService(db)
    updated_billing = billing_service.update_billing(billing_id, billing)
    if not updated_billing:
        raise HTTPException(status_code=404, detail="Billing record not found")
    return updated_billing

#--------------------------------------
# Delete a billing record by ID
#--------------------------------------
@router.delete("/{billing_id}", response_model=dict)
def delete_billing(
    billing_id: int,
    db: Session = Depends(get_db),
):
    billing_service = BillingService(db)
    success = billing_service.delete_billing(billing_id)
    if not success:
        raise HTTPException(status_code=404, detail="Billing record not found")
    return {"detail": "Billing record deleted successfully"}

#--------------------------------------
# List all billing records
#--------------------------------------
@router.get("/", response_model=List[BillingResponse])
def list_billings(
    db: Session = Depends(get_db),
):
    billing_service = BillingService(db)
    return billing_service.list_billings()

#--------------------------------------
# Additional route: Get billings by patient ID
#--------------------------------------
@router.get("/patient/{patient_id}", response_model=List[BillingResponse])
def get_billings_by_patient(
    patient_id: int,
    db: Session = Depends(get_db),
):
    billing_service = BillingService(db)
    return billing_service.get_billings_by_patient(patient_id)
