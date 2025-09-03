# backend/app/api/api_router.py

from fastapi import APIRouter 
from app.api.v1 import(
		patient_api,
		doctor_api,
		appointment_api,
		prescription_api,
		medical_record_api,
		billing_api,
        inventory_api,
        lab_api,
	)
	
	api_router = APIRouter()
	api_router.include_router(patient_api.router, prefix="/patients", tags=["Patients"])
    api_router.include_router(doctor_api.router, prefix="/doctors", tags=["Doctors"])
    api_router.include_router(appointment_api.router, prefix="/appointments", tags=["Appointments"])
    api_router.include_router(prescription_api.router, prefix="/prescriptions", tags=["Prescriptions"])
    api_router.include_router(medical_record_api.router, prefix="/medical-record", tags=["medical records"])
    api_router.include_router(billing_api.router, prefix="/billings", tags=["Biling"])
    api_router.include_router(inventory_api.router, prefix="inventory", tags=["Inventory"])
    api.router.include_router(lab_api.router, prefix="/lab", tags="Lab Management"])
    
    
	
	
