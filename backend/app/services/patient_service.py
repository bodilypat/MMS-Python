# app/services/patient_service.py

from typing import List, Optional
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientUpdate

#----------------------------------------
# Create a new patient record 
#----------------------------------------
def create_patient(db: Session, patient: PatientCreate, current_user_id: Optional[int] = None) -> bool:
    """
    Create a new patient record in the database.
    Args:
        db (Session): Database session.
        patient (PatientCreate): Patient data to create.
        current_user_id (Optional[int]): ID of the user creating the record.
    """
    try:
        # create patient record
        db_patient = Patient(**patient.dict())
        db.add(db_patient)
        db.commit()
        db.refresh(db_patient)

        # Audit log 
        if current_user_id:
            log_action(
                db=db,
                user_id=current_user_id,
                action=f"Created new patient record with ID {db_patient.id}",
                resource_type="Patient",
                resource_id=db_patient.id
            )
        return db_patient
    except Exception as e:
        db.rollback()
        raise e

#----------------------------------------
# Get a patient record by ID
#----------------------------------------
def get_patient(db: Session, patient_id: int) -> Optional[Patient]:
    """
    Retrieve a patient record by its ID.
    Args:
        db (Session): Database session.
        patient_id (int): ID of the patient to retrieve.
    """

    patient = db.query(Patient).filter(
        Patient.id == patient_id,
        Patient.is_deleted == False
        ).first()
    
    # Audit log for viewing patient record
    if patient and current_user_id:
        log_action(
            db=db,
            user_id=current_user_id,
            action=f"Viewed patient record with ID {patient_id}",
            resource_type="Patient",
            resource_id=patient_id
        )

    return patient


#----------------------------------------
# Get all patient records 
#----------------------------------------
def get_patients(db: Session, skip: int = 0, limit: int = 100) -> List[Patient]:
    """
    Retrieve all patient records.
    Args:
        db (Session): Database session.
        skip (int): Number of records to skip.
        limit (int): Maximum number of records to retrieve.
        current_user_id (Optional[int]): ID of the user retrieving the records.

    Returns:

    """
    patients = db.query(Patient).filter(
        Patient.is_deleted == False
    ).offset(skip).limit(limit).all()

    # Optional audit log for bulk retrieval
    if current_user_id:
        log_action(
            db=db,
            user_id=current_user_id,
            action=f"Retrieved patient records, skip={skip}, limit={limit}",
            resource_type="Patient",
            resource_id=None
        )   
    return patients

#----------------------------------------
# Update a patient record by ID
#----------------------------------------
def update_patient(
        db: Session, 
        patient_id: int, 
        patient_update: PatientUpdate, 
        current_user_id: Optional[int] = None
    ) -> Optional[Patient]:

    """
    Update a patient record by its ID.
    Args:
        db (Session): Database session.
        patient_id (int): ID of the patient to update.
        patient_update (PatientUpdate): Updated patient data.
        current_user_id (Optional[int]): ID of the user updating the record.
    Returns:
        Optional[Patient]: The updated patient record, or None if not found.
    """
    db_patient = db.query(Patient).filter(
        Patient.id == patient_id,
        Patient.is_deleted == False
    ).first()

    if not db_patient:
        return None

    # Track changes for audit log
    updated_fields = Dict[str, Any] = {}

    for field, value in patient_update.dict(exclude_unset=True).items():
        old_value = getattr(db_patient, field, None)
        if old_value != value:
            setattr(db_patient, field, value)
            updated_fields[field] = (old_value, value)
        try: 
            db.commit()
            db.refresh(db_patient)

            # Audit log for updates
            if current_user_id and updated_fields:
                changes = "; ".join(
                    [f"{field}: '{old}' -> '{new}'" for field, (old, new) in updated_fields.items()]
                )
                log_action(
                    db=db,
                    user_id=current_user_id,
                    action=f"Updated patient record ID {patient_id}. Changes: {changes}",
                    resource_type="Patient",
                    resource_id=patient_id
                )
            return db_patient
        except Exception as e:
            db.rollback()
            raise e
        
#----------------------------------------
#     QUERY FUNCTIONS
# ---------------------------------------- 
def get_patients_by_name(
        db: Session, 
        name: str, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Patient]:

    """
    Retrieve patient records by name.
    Args:
        db (Session): Database session.
        name (str): Name of the patient to search for.
        skip (int): Number of records to skip.
        limit (int): Maximum number of records to retrieve.
        current_user_id (Optional[int]): ID of the user retrieving the records.

    returns:
        List[Patient]: List of patient records matching the name.
    """

    patients = db.query(Patient).filter(
        Patient.is_deleted == False,
        or_(
            Patient.first_name.ilike(f"%{name}%"),
            Patient.last_name.ilike(f"%{name}%")
        )
    ).offset(skip).limit(limit).all()

    # Audit log (bulk search)
    if current_user_id:
        log_action(
            db=db,
            user_id=current_user_id,
            action=f"Retrieved patient records by name: {name}, skip={skip}, limit={limit}",
            resource_type="Patient",
            resource_id=None
        )
    return patients


def get_patients_by_dob_range(
        db: Session, 
        start_date: datetime, 
        end_date: datetime, 
        skip: int = 0, 
        limit: int = 100,
        current_user_id: Optional[int] = None
    ) -> List[Patient]:

    """
    Retrieve patient records by date of birth range.
    Args:
        db (Session): Database session.
        start_date (datetime): Start date of birth range.
        end_date (datetime): End date of birth range.
        skip (int): Number of records to skip.
        limit (int): Maximum number of records to retrieve.
        current_user_id (Optional[int]): ID of the user retrieving the records.
    Returns:

    """
    patients = db.query(Patient).filter(
        Patient.is_deleted == False,
        and_(
            Patient.date_of_birth >= start_date,
            Patient.date_of_birth <= end_date
        )
    ).offset(skip).limit(limit).all()
    # Audit log (bulk search)
    if current_user_id:
        log_action(
            db=db,
            user_id=current_user_id,
            action=f"Retrieved patient records by DOB range: {start_date} to {end_date}, skip={skip}, limit={limit}",
            resource_type="Patient",
            extra_info = (
                f"Date of Birth Range: {start_date} to {end_date},"
                f" results={len(patients)}, skip={skip}, limit={limit}"                
            )
        )
    return patients

def get_patients_by_condition(
        db: Session, 
        condition: str, 
        skip: int = 0, 
        limit: int = 100,
        current_user_id: Optional[int] = None
    ) -> List[Patient]:

    """
    Retrieve patient records by medical condition.
    Args:
        db (Session): Database session.
        condition (str): Medical condition to search for.
        skip (int): Number of records to skip.
        limit (int): Maximum number of records to retrieve.
        current_user_id (Optional[int]): ID of the user retrieving the records.
    returns:
        List[Patient]: List of patient records matching the medical condition.
    """
    patients = db.query(Patient).filter(
        Patient.is_deleted == False,
        Patient.medical_conditions.ilike(f"%{condition}%")
    ).offset(skip).limit(limit).all()

    # Audit log (bulk search)
    if current_user_id:
        log_action(
            db=db,
            user_id=current_user_id,
            action=f"Retrieved patient records by condition: {condition}, skip={skip}, limit={limit}",
            resource_type="Patient",
            extra_info=(
                f"Medical Condition: {condition},"
                f" results={len(patients)}, skip={skip}, limit={limit}"
            )
        )
    return patients

def get_patient_by_assigned_doctor(db: Session, doctor_id: int, skip: int = 0, limit: int = 100) -> List[Patient]:
    """
    Retrieve patient records assigned to a specific doctor.
    Args:
        db (Session): Database session.
        doctor_id (int): ID of the assigned doctor.
        skip (int): Number of records to skip.
        limit (int): Maximum number of records to retrieve.
        current_user_id (Optional[int]): ID of the user retrieving the records.

    returns:
        List[Patient]: List of patient records assigned to the specified doctor.
    """
    patient = db.query(Patient).filter(
        Patient.assigned_doctor_id == doctor_id
    ).offset(skip).limit(limit).all()

    return patient

def get_patients_with_upcoming_appointments(db: Session, days_ahead: int = 7, skip: int = 0, limit: int = 100) -> List[Patient]:
    """
    Retrieve patient records with upcoming appointments within a specified number of days.
    Args:
        db (Session): Database session.
        days_ahead (int): Number of days ahead to check for appointments.
        skip (int): Number of records to skip.
        limit (int): Maximum number of records to retrieve.
        current_user_id (Optional[int]): ID of the user retrieving the records.
    returns:
        List[Patient]: List of patient records with upcoming appointments.
    
    """

    upcoming_date = datetime.now() + timedelta(days=days_ahead)
    return db.query(Patient).filter(
        Patient.next_appointment <= upcoming_date
    ).offset(skip).limit(limit).all()


