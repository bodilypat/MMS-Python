#app/main.py

from fastapi import FastAPI
from app.routers import (
    auth,
    users,
    patients,
    appointnents,
    doctors,
    medical_records,
    prescriptions,  
    billing,
)

app = FastAPI("medical Management System")
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(patients.router)
app.include_router(appointnents.router)
app.include_router(doctors.router)
app.include_router(medical_records.router)
app.include_router(prescriptions.router)
app.include_router(billing.router)

