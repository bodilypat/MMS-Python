#app/main.py

from fastapi import FastAPI
from app.api.api_router import api_router

app = FastAPI(
		title="Medical Management System (MMS) API",
		description="API for managing patients, doctors, appointments, prescription, lab, billing, inventory, and medical records.",
		version ="1.0.0",
	)
	app.include_router(api_router, prefix="/api/v1")