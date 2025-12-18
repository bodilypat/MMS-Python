#app/routers/doctors.py

from  fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas import DoctorCreate, DoctorResponse, DoctorUpdate
from app.database import get_db
from app.services.doctor_service import DoctorService

router = APIRouter(
    prefix="/doctors",
    tags=["doctors"]
)

#-----------------------------------
# Create a new doctor
#-----------------------------------
@router.post("/", response_model=DoctorResponse)
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    doctor_service = DoctorService(db)
    return doctor_service.create_doctor(doctor)

#-----------------------------------
# Get a list of all doctors
#-----------------------------------
@router.get("/", response_model=List[DoctorResponse])
def get_doctors(db: Session = Depends(get_db)):
    doctor_service = DoctorService(db)
    return doctor_service.get_all_doctors()

#-----------------------------------
# Get a doctor by ID
#-----------------------------------
@router.get("/{doctor_id}", response_model=DoctorResponse)
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor_service = DoctorService(db)
    doctor = doctor_service.get_doctor_by_id(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

#-----------------------------------
# Update a doctor's information
#-----------------------------------
@router.put("/{doctor_id}", response_model=DoctorResponse)
def update_doctor(doctor_id: int, doctor_update: DoctorUpdate, db: Session = Depends(get_db)):
    doctor_service = DoctorService(db)
    updated_doctor = doctor_service.update_doctor(doctor_id, doctor_update)
    if not updated_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return updated_doctor

#-----------------------------------
# Delete a doctor
#-----------------------------------
@router.delete("/{doctor_id}")
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor_service = DoctorService(db)
    success = doctor_service.delete_doctor(doctor_id)
    if not success:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return {"detail": "Doctor deleted successfully"}

#-----------------------------------
# Get doctors by specialty
#-----------------------------------
@router.get("/specialty/{specialty}", response_model=List[DoctorResponse])
def get_doctors_by_specialty(specialty: str, db: Session = Depends(get_db)):
    doctor_service = DoctorService(db)
    return doctor_service.get_doctors_by_specialty(specialty)

#-----------------------------------
# Get doctors by availability
#-----------------------------------
@router.get("/availability/{date}", response_model=List[DoctorResponse])
def get_doctors_by_availability(date: str, db: Session = Depends(get_db)):
    doctor_service = DoctorService(db)
    return doctor_service.get_doctors_by_availability(date)

#-----------------------------------
# Search doctors by name
#-----------------------------------
@router.get("/search/", response_model=List[DoctorResponse])
def search_doctors_by_name(name: str, db: Session = Depends(get_db)):
    doctor_service = DoctorService(db)
    return doctor_service.search_doctors_by_name(name)



