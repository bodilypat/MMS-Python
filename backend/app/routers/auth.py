#app/routers/auth.py 

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.scheamas import UserCreate, Userlogin, Token, UserResponse
from app.database import get_db
from app.services import AuthService, create_access_token, verify_password
from datetime import timedelta
from app.config import settings

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

#-----------------------------------
# User Registration Endpoint
#-----------------------------------
@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = AuthService.get_user_by_email(db, email=user.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    new_user = AuthService.create_user(db, user)
    return new_user

#-----------------------------------
# User Login Endpoint
#-----------------------------------
@router.post("/login", response_model=Token)
def login_user(user: Userlogin, db: Session = Depends(get_db)):
    db_user = AuthService.get_user_by_email(db, email=user.email)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": db_user.email}, expires_delta=access_token_expires)
    
    return {"access_token": access_token, "token_type": "bearer"}

#-----------------------------------
# User Logout Endpoint
#-----------------------------------
@router.post("/logout")
def logout_user():
    # In a real-world scenario, you might want to handle token blacklisting here.
    return {"message": "User logged out successfully"}

#-----------------------------------
# Token Refresh Endpoint
#-----------------------------------
@router.post("/refresh", response_model=Token)
def refresh_token(current_user: UserResponse = Depends(AuthService.get_current_user)):
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": current_user.email}, expires_delta=access_token_expires)
    
    return {"access_token": access_token, "token_type": "bearer"}   

#-----------------------------------
# Password Reset Endpoint
#-----------------------------------
@router.post("/reset-password")
def reset_password(email: str, db: Session = Depends(get_db)):
    user = AuthService.get_user_by_email(db, email=email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    # Here you would typically send a password reset email with a token
    # For simplicity, we'll just return a success message
    return {"message": "Password reset link has been sent to your email"}

#-----------------------------------
# Change Password Endpoint
#-----------------------------------
@router.post("/change-password")
def change_password(current_password: str, new_password: str, db: Session = Depends(get_db), current_user: UserResponse = Depends(AuthService.get_current_user)):
    user = AuthService.get_user_by_email(db, email=current_user.email)
    if not user or not verify_password(current_password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Current password is incorrect")
    
    AuthService.update_user_password(db, user, new_password)
    return {"message": "Password changed successfully"}

#-----------------------------------
# Get Current User Endpoint
#-----------------------------------
@router.get("/me", response_model=UserResponse)
def get_current_user(current_user: UserResponse = Depends(AuthService.get_current_user)):
    return current_user

#-----------------------------------
# Delete User Account Endpoint
#-----------------------------------
@router.delete("/delete-account")   
def delete_account(db: Session = Depends(get_db), current_user: UserResponse = Depends(AuthService.get_current_user)):
    user = AuthService.get_user_by_email(db, email=current_user.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    AuthService.delete_user(db, user)
    return {"message": "User account deleted successfully"}

#-----------------------------------
# Update User Profile Endpoint
#-----------------------------------
@router.put("/update-profile", response_model=UserResponse)
def update_profile(updated_user: UserCreate, db: Session = Depends(get_db), current_user: UserResponse = Depends(AuthService.get_current_user)):
    user = AuthService.get_user_by_email(db, email=current_user.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    updated_user_data = AuthService.update_user_profile(db, user, updated_user)
    return updated_user_data

