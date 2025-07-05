# backend/app/api/vi/endpoints/patients.py

from fastapi import APIRouter, Depends
from app.schemas import PatientCreate, PatientOut 
from app.services.patient import create_patient

router = APIRouter()
@router.post("/", response_model=PatientOut)
def add_patient(data: PatientCreate):
	return create_patient(data)
	
