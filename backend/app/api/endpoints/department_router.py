#app/api/v1/endpoints/department_router.py

from fastapi import APIRouter, Depends, HTTPException, Status, Query, Response
from sqlalchemy.orm import Session
from typing import List 

from app.schemas.department import DepartmentCreate, DepartmentRead, DepartmentUpdate 
from app.services import department_service as DepartmentService 
from db.session import get_db

router = APIRouter()

@router.get("/", response_model=DepartmentRead, summary="Get a list of Department")
def list_departments(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, le=100),
        db: Session = Depends(get_db)
    ):
    return DepartmentService(db).get_all_departments(skip, limit)

@router.get("/{department_id}", response_model=DepartmentRead, summary="Get a sigle department")
def read_department(
        department_id: int,
        db: Session = Depends(get_db)
    ):
    department = DepartmentService(db).get_department_by_id(department_id)

    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    return department 

@router.post("/", response_model=DepartmentRead, status_code=status.HTTP_201_CREATED, summary="Create a new department")
def create_department(
        department_data: DepartmentCreate,
        db: Session = Depends(get_db)
    ):
    return DepartmentService(db).create_department(department_data)

@router.put("/{department_id}", response_model=DepartmentRead, summary="Update an existing department")
def update_department(
        department_id: int,
        updated_department: DepartmentUpdate,
        db: Session = Depends(get_db)
    ):
    updated = DepartmentService(db).update_department(department_id, updated_department)

    if not department:
        return None 
    return updated

@router.delete("/{department_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Department")
def delete_department(
        department_id: int,
        db: Session = Depends(get_db)
    ):

    success = DepartmentService(db).delete_department(department_id)
    if not success:
        return False 
    return Response(status_code=status.HTTP_NO_CONTENT)

