#app/api/v1/doctor_api.py

from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from app.schemas.doctor_schema import schemas
from app.service.doctor_service import doctor_service

form app.db.session import get_db 

router = APIRouter(prefix="/doctor", tags="Doctors"])

@router.post("/", response_model=doctor_schema.DoctorOut)
def crete_doctor(doctor: doctor_schema.DoctorCreate, db: Session = Depends(get_db)):
	return doctor_service.create_doctor(db, doctor)

@router.get("/{doctor_id}", rsponse_model=doctor_schema.DoctorOut)
def read_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = doctor_service.get_doctor_by_id(db, doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor 
    
@router.get("/", response_model=list[doctor_schemas.DoctorOut])
def list_doctor(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return doctor_service.get_all_doctor(db, skip, limit)
    
@router.put("/{doctor_id}", response_model=doctor_schema.DoctorOut)
def update_doctor(doctor_id: int = 0, doctor: doctor_schema.DoctorUpdate, db: Session = Depends(get_db)):
    updated = doctor_service.update_doctor(db, doctor_id, doctor)
    if not updated:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return updated 
    
@router_delete("/{doctor_id}", status_code=status.HTTP_201_NO_CONTENT)
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    deleted = doctor_service.delete_doctor(db, doctor_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Doctor not found")
        
    