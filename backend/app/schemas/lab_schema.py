#app/schemas/lab_schema.py

from pydantic import BaseModel, Field 
from typing import Optional
from datetime import datetime
from enum import Enum 

class TestStatus(str, Enum):
    ordered = "ordered"
    sample_collected = "sample_collected"
    processing = "processing"
    completed =  "completed"
    
# Lab Test Schemas
class LabTestBase(BaseModel):
    name: str
    descriptioon: Optional[str] = None 
    price: Optional[int] = Field(default=None, ge=0, description="Price must be non-negative")
    normal_range: Optional[str] = None 
    unit: Optional[str] = None 
    	
class LabTestCreate(LabTestBase):
	pass 

class LabTestOut(LabTestBase):
	id: int 
	
	class Config:
		orm_mode: True 
	
# Lab Order Schemas 
	
class LabOrderBase(BaseModel):
	patient_id: int 
	doctor_id: int 
	appointment_id: Optional[int] = None
	test_id: int 
	
class LabOrderCreate(LabOrderBase):
	status: Optional[TestStatus] = TestStatus.ordered
	result: Optional[str] = None
	comments: Optional[str] = None 
    
class LabOrderUpdate(BaseModel):
    status: Optional[TestStatus] = TestStatus.ordered
    result: Optional[str] = None 
    comments: Optional[str] = None
	
class LabOrderOut(LabOrderBase):
	id: int 
	status: TestStatus[str]
    result: Optional[str] = None 
    comments: Optional[str] = None 
    ordered: datetime
    completed_at: Optional[datetime] = None 
    test: LabTestOut 
    
	class Config:
		orm_mode = True 
		