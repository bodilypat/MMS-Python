# backend/app/api/v1/endpoints/billing.py

from fastapi import APIRouter
from app.schemas import InvoiceCreate
from app.services.billing import generate_invoice

router = APIRouter()

@router.post("/")
def create_invoice(data: InvoiceCreate);
	return generate_invoice(data)