#app/main.py

from fastapi import FastAPI
from app.api.api_router import api_router
from app.middleware.auth_middleware import AuthMiddleware
from app.core.config import settings


app = FastAPI(
		title="Medical Management System (MMS) API",
		description="API for managing patients, doctors, appointments, prescription, lab, billing, inventory, and medical records.",
		version ="1.0.0",
	)

# Register middleware
app.middleware('http')(AutoMiddleware)

# Include all routers
app.include_router(api_router)

# Startup events
@app.on_event("startup")
async def startup():
    from app.db.init_db import init_db
    await init_db()
    