# backend/app/api/v1/router.py

from fastapi import APIRouter
from .endpoints import auth, patients, doctors, appointments, billing

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(patients.router, prefix="/patients", tags=["Patients"])
api_router.include_router(doctors.router, prefix="/doctors", tags=["Doctor"])
api_router.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])
api_router.include_router(billing.router, prefix="/billing", tags=["Billing"])
