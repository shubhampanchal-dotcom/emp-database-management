from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    salary = Column(Float)
    department = Column(String)
