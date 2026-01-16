from fastapi import FastAPI
from app.core.config import settings
from app.database import Base, engine
from app.routes import auth, employees

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employees API")

@app.get("/")
def root():
    return {"message": "FastAPI with SQLite deployed successfully!"}

app.include_router(auth.router, prefix="/api/auth")
app.include_router(employees.router, prefix="/api/employees")
