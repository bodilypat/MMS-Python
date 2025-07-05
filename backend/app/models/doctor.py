#backend/app/models/doctor.py

from sqlalchemy import column, String, ARRAY
from app.db.session import Base
import uuid

class Doctor(Base):
	__tablename__ = "doctors"
	
	id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4())
	ame = Column(String, nullable=False)
	email = Column(String, unique=True, index=True, nullable=False)
	phone = Column(String, nullable=True)
	specialization = Column(String, nullable=False)
	available_days = Column(ARRAY(String))
	
