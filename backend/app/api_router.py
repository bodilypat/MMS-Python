# app/api_router.py

from fastapi import APIRouter 
from app.api.endpoints import(
		patient_router,
        department_router,
		doctor_router,
		appointment_router,
		prescription_router,
		medical_record_router,
		billing_router,
        inventory_router,
        lab_router,
	)
    
# Create the main API Router
api_router = APIRouter(prefix="/api")
    
# Include individual routers
api_router.include_router(patient_router.router, prefix="/patients", tags=["Patients"])
api_router.include_router(department_router.router, prefix="/departments", tags=["Departments"])
api_router.include_router(doctor_router.router, prefix="/doctors", tags=["Doctors"])
api_router.include_router(appointment_router.router, prefix="/appointments", tags=["Appointments"])
api_router.include_router(prescription_router.router, prefix="/prescriptions", tags=["Prescriptions"])
api_router.include_router(medical_record_router.router, prefix="/records", tags=["Medical records"])
api_router.include_router(billing_router.router, prefix="/billings", tags=["Billing"])
api_router.include_router(inventory_router.router, prefix="inventory", tags=["Inventory"])
api_router.include_router(lab_api.router, prefix="/labs", tags=["Labs"])
    
    
	
	
