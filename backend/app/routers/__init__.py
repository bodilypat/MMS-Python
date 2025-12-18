#app/routers/__init__.py 

from app.routers import auth
from app.routers import users
from app.routers import patients 
from app.routers import doctors
from app.routers import appointments
from app.routers import medical_records
from app.routers import prescriptions
from app.routers import billing


__all__ = [
    "auth",
    "users",
    "patients",
    "doctors",
    "appointments",
    "medical_records",
    "prescriptions",
    "billing",
]


