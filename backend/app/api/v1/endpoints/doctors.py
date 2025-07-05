# backend/app/api/v1/endpoints/doctors.py

from fastapi import APIRouter
from app.services.doctor import list_doctors

router = APIRouter()

@router.get("/")
def get_doctor():
	return list_doctors()
	