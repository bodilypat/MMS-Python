#app/core/permissions.py

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from app.dependancies import get_current_user
from app.schemas.user_schemas import UserOut

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Base permission class
class BasePermission:
    async def __init__(self, current_user: UserOut = Depends(get_current_user)):
        self.user = current_user            

    async def has_permission(self) -> bool:
        raise NotImplementedError("Subclasses must implement this method")
    
# Admin only permission
class IsAdmin(BasePermission):
    async def __call__(self, current_user: UserOut = Depends(get_current_user)):
        self.user = current_user
        return await self.has_permission()

    async def has_permission(self) -> bool:     
        if not self.user.is_admin:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action."
            )
        return True
    
# Authenticated users permission
class IsAuthenticated(BasePermission):
    async def __call__(self, current_user: Optional[UserOut] = Depends(get_current_user)):
        self.user = current_user
        return await self.has_permission()

    async def has_permission(self) -> bool:
        if not self.user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="You must be authenticated to perform this action."
            )
        return True
    
# Role Based Permission (Opitional)
class HasRole(BasePermission):
    def __init__(self, allowed_roles: list[str]):
        self.allowed_roles = allowed_roles

    async def __call__(self, current_user: UserOut = Depends(get_current_user)):    

        self.user = current_user
        return await self.has_permission()

    async def has_permission(self) -> bool:
        if not self.user or self.user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"You must have one of the allowed roles to perform this action."
            )
        return True
    
