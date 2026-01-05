#app/api/v1/api_router.py

from fastapi import APIRouter

from app.api.v1.routes import (
    auth,
    users,
    roles,
    patients,
    doctors,
    appointments,
    medical_records,
    prescriptions,
    billing,
    reports
)
api_router = APIRouter()

#Auhentication & Authorization
api_router.include_router(
    auth.router, 
    prefix="/auth", 
    tags=["auth"]
)

#User Management
api_router.include_router(
    users.router, 
    prefix="/users", 
    tags=["users"]
)

# Core Medical Modules 
api_router.include_router(
    patients.router, 
    prefix="/patients", 
    tags=["patients"]
)

api_router.include_router(
    doctors.router, 
    prefix="/doctors", 
    tags=["doctors"]
)
api_router.include_router(
    appointments.router,
    prefix="/appointments",
    tags=["appointments"]
)
api_router.include_router(
    medical_records.router,
    prefix="/medical-records",
    tags=["medical-records"]
)
api_router.include_router(
    prescriptions.router,
    prefix="/prescriptions",
    tags=["prescriptions"]
)
api_router.include_router(
    billing.router,
    prefix="/billing",
    tags=["billing"]
)
api_router.include_router(
    reports.router,
    prefix="/reports",
    tags=["reports"]
)
# Role Management
api_router.include_router(
    roles.router, 
    prefix="/roles", 
    tags=["roles"]
)

