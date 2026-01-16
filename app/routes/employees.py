from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from app.database import SessionLocal
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeResponse
from app.core.security import verify_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.schemas.employee import EmployeeUpdate


router = APIRouter()
security = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def auth(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if not verify_token(credentials.credentials):
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/", status_code=201)
def create_employee(emp: EmployeeCreate, db: Session = Depends(get_db), _: str = Depends(auth)):
    if db.query(Employee).filter(Employee.email == emp.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")

    employee = Employee(**emp.dict())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

@router.get("/")
def list_employees(
    page: int = 1,
    department: Optional[str] = None,
    role: Optional[str] = None,
    db: Session = Depends(get_db),
    _: str = Depends(auth)
):
    query = db.query(Employee)
    if department:
        query = query.filter(Employee.department == department)
    if role:
        query = query.filter(Employee.role == role)

    return query.offset((page - 1) * 10).limit(10).all()


@router.get("/{id}")
def get_employee(id: int, db: Session = Depends(get_db), _: str = Depends(auth)):
    emp = db.query(Employee).get(id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp


@router.patch("/{id}")
def partial_update_employee(
    id: int,
    emp: EmployeeUpdate,
    db: Session = Depends(get_db),
    _: str = Depends(auth)
):
    employee = db.query(Employee).get(id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    for key, value in emp.dict(exclude_unset=True).items():
        setattr(employee, key, value)

    db.commit()
    db.refresh(employee)
    return employee


@router.put("/{id}")
def update_employee(id: int, emp: EmployeeCreate, db: Session = Depends(get_db), _: str = Depends(auth)):
    employee = db.query(Employee).get(id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    for key, value in emp.dict().items():
        setattr(employee, key, value)

    db.commit()
    return employee


@router.delete("/{id}", status_code=204)
def delete_employee(id: int, db: Session = Depends(get_db), _: str = Depends(auth)):
    employee = db.query(Employee).get(id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(employee)
    db.commit()
