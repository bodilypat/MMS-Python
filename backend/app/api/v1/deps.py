# backend/app/api/vi/deps.py

from app.db.session import SessionLocal
from sqlchemy.orm import Session 

def get_db():
	db = SessionLocal()
	
	try:
		yield db
	finally:
		db.close() 
		
		