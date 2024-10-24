from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    if not crud.delete_employee(db=db, employee_id=employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"detail": "Employee deleted"}

@app.get("/employees/{employee_id}", response_model=schemas.Employee)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db=db, employee_id=employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee
