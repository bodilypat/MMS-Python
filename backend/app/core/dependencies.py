#app/core/dependencies.py

from fastapi import Depends, HTTPException, status
from fastapi.orm import Session

from app.core.security import get_current_active_user
from app.database import get_db
from app.models.user import User

#-------------------------------------
# Authentication dependency
#-------------------------------------
def get_authenticated_user(
    current_user: User = Depends(get_current_active_user)
) -> User:
    
    """ 
    Ensures the request has a valid authenticated user.
    """
    if not current_user.is_authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is not authenticated",
        )
    return current_user

#-------------------------------------
# Role-based dependencies
#-------------------------------------
def require_admin(
    current_user: User = Depends(get_authenticated_user)
) -> User:
    
    """ 
    Ensures the authenticated user has admin privileges.
    """
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User does not have admin privileges",
        )
    return current_user

def require_doctor(
    current_user: User = Depends(get_authenticated_user)
) -> User:
    
    """ 
    Ensures the authenticated user has doctor privileges.
    """
    if not current_user.is_doctor:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User does not have doctor privileges",
        )
    return current_user

def require_patient(
    current_user: User = Depends(get_authenticated_user)
) -> User:
    
    """ 
    Ensures the authenticated user has patient privileges.
    """
    if not current_user.is_patient:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User does not have patient privileges",
        )
    return current_user

def require_nurse(
    current_user: User = Depends(get_authenticated_user)
) -> User:
    
    """ 
    Ensures the authenticated user has nurse privileges.
    """
    if not current_user.is_nurse:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User does not have nurse privileges",
        )
    return current_user

#-------------------------------------
# Ownership / access helpers 
#-------------------------------------
def allow_self_or_admin(
    user_id: int,
    current_user: User = Depends(get_authenticated_user)
) -> User:
    
    """ 
    Allows access if the current user is the owner of the resource or an admin.
    """
    if current_user.id != user_id and not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: not the owner or admin",
        )
    return current_user 



