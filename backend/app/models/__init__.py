#app/models/__init__.py

from app.models.user import User 
from app.models.patient import Patient
from app.models.appointment import Appointment
from app.models.doctor import Doctor
from app.models.medical_record import MedicalRecord
from app.models.prescription import Prescription
from app.models.billing import Billing

__all__ = [
    'User',
    'Patient',
    'Appointment',
    'Doctor',
    'MedicalRecord',
    'Prescription',
    'Billing'
]


