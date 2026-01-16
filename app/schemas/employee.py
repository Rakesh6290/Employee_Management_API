from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    department: Optional[str]
    role: Optional[str]

class EmployeeResponse(EmployeeCreate):
    id: int
    date_joined: date

    class Config:
        orm_mode = True


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    department: Optional[str] = None
    role: Optional[str] = None