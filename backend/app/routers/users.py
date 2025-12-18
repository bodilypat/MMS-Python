#app/routers/user.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.user import UserCreate, UserResponse,
from app.database import get_db
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

#-------------------------------------------
# Create a new user
#-------------------------------------------
@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    db_user = user_service.get_user_by_email(user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_user(user)

#-------------------------------------------
# Get user by ID
#-------------------------------------------
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService(db)
    db_user = user_service.get_user_by_id(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

#-------------------------------------------
# Get all users
#-------------------------------------------
@router.get("/", response_model=List[UserResponse])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.get_users(skip=skip, limit=limit)

#-------------------------------------------
# Delete user by ID
#-------------------------------------------
@router.delete("/{user_id}", response_model=UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService(db)
    db_user = user_service.get_user_by_id(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_service.delete_user(user_id)

#-------------------------------------------
# Update user by ID
#-------------------------------------------
@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    db_user = user_service.get_user_by_id(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_service.update_user(user_id, user)

#-------------------------------------------
# Search users by name
#-------------------------------------------
@router.get("/search/", response_model=List[UserResponse])
def search_users(name: str, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.search_users_by_name(name)

#-------------------------------------------
# Get user by email
#-------------------------------------------
@router.get("/by_email/", response_model=UserResponse)
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    user_service = UserService(db)
    db_user = user_service.get_user_by_email(email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

#-------------------------------------------
# Get total user count
#-------------------------------------------
@router.get("/count/", response_model=int)
def get_user_count(db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.get_user_count()

#-------------------------------------------
# Get users by role
#-------------------------------------------
@router.get("/by_role/{role}/", response_model=List[UserResponse])
def get_users_by_role(role: str, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.get_users_by_role(role)

