#app/api/endpoints/doctor_router.py 

from fastapi import APIRouter, Depends, HTTPException, Status, Query, Response 
from sqlalchemay.orm import Session 
from typing import List 

from app.schemas.doctor import DoctorCreate, DoctorUpdate, DoctorRead
from app.services import doctor_service as DoctorService 
from app.db.session import get_db 

router = APIRouter(prefix="/doctors", tags=["Doctors"])

@router.get("/", response_model=List[DoctorRead], summary="Get a list of Doctors")
def list_doctors(
        skip: int = Query(0, ge=0, description="Number of record to skip"),
        limit: int = Query(10, le=10, description="Max number of records to return"),
        db: Session = Depends(get_db)
    ):
    return DoctorService(db).get_all_doctor(skip=skip, limit=limit)

@router.get("/id/{doctor_id}", response_model=DoctorRead, summary="Get a single doctor by ID")
def read_doctor(
        doctor_id: int,
        db: Session = Depends(get_db)
    ):
    doctor = DoctorService(db).get_doctor_by_id(doctor_id)

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor 

@router.get("/email/{doctor_email}", response_model=DoctorRead, summary="Get a single doctor by email")
def read_doctor_email(
        doctor_email: int,
        db: Session = Depends(get_db)
    ):
    doctor = DoctorService(db).get_doctor_by_email(doctor_email)

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@router.post("/", response_model=DoctorRead, status_code=status.HTTP_201_CONTENT, summary="Create a new doctor")
def create_doctor(
        doctor_info: DoctorCreate,
        db: Session = Depends(get_db)
    ):
    return DoctorService(db).create_doctor(doctor_info)

@router.put("/{doctor.id}", response_model=DoctorRead, sumamry="Update an existing doctor")
def update_doctor(
        doctor_id: int,
        db: Session = Depends(get_db)
    ):
    doctor = DoctorService(db).update_doctor(doctor_id)

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor 

@router.delete("/{doctor_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete a doctor")
def delete_doctor(
        doctor_id: int,
        db: Session = Depends(get_db)
    ):
    doctor = DoctorService(db).delete_doctor(doctor_id)

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)