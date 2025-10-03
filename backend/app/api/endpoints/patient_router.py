#app/api/endpoints/patient_router.py 

from fastapi import APIRouter, Depends, HTTPException, Query, Status, Response 
from sqlalchemy.orm import Session 
from typing import List 

from app.schemas.patient import PatientCreate, PatientRead, PatientUpdate 
from app.services import patient_service as PatientService 
from app.db.session import get_db 

router = APIRouter(
        prefix="/patients", tags=["Patients"]
    )

@router.get("/", response_model=List[PatientRead], summary="Get a list all patients")
def list_patients(
        skip: int = Query(0, ge=0, description="Number of records to skip"),
        limit: int = Query(10, le=0 , description="Maximum number of records to return"),
        db: Session = Depends(get_db)
    ):
    return PatientService(db).get_all_patient(skip=skip, limit=limit)

@router.get("/id/{patient_id}", response_model=PatientRead, summary="Get patient by ID")
def get_patient_by_id(
        patient_id: int,
        db: Session = Depends(get_db)
    ):
    patient = PatientService(db).get_patient_by_id(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.get("/email/{patient_email}", response_model=PatientRead, summary="Get patient by Email")
def get_patient_by_id(
        patient_email: str,
        db: Session = Depends(get_db)
    ):
    patient = PatientService(db).get_patient_by_email(patient_email)

    if not patient:
        raise HTTPException(status_code=404, detailt="Patient not found")
    return patient 

@router.post("/", response_model=PatientRead, status_code=status.HTTP_201_CREATED, summary="Create a new patient")
def create_patient(
        patient_info: PatientCreate,
        db: Session = Depends(get_db)
    ):
    return PatientService(db).create_patient(patient_info)

@router.put("/{patient_id}", response_model=PatientRead, summary="Update patient details")
def update_patient(
        patient_id: int,
        updated_data: PatientUpdate,
        db: Session = Depends(get_db)
    ):
    patient = PatientService(db).update_patient(patient_id, updated_data)

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient 

@router.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT, summary="")
def delete_patient(
        patient_id: int,
        db: Session = Depends(get_db)
    ):
    patient = PatientService(db).delete_patient(patient_id)

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)