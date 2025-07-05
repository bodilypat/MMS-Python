from fastapi import APIRouter, Depends
from app.schemas import UserLogin, UserOut
from app.services.auth import login_user 

router = APIRouter()

@router.post("/login", response_model=UserOut)
def login(User_data: userLogin):
	return login_user(user_data)
	