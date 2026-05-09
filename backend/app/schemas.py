# app/schemas.py
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class EnergyReadingBase(BaseModel):
    timestamp: datetime
    consumption_kwh: float
    cost_usd: float
    region: str

class EnergyReadingCreate(EnergyReadingBase):
    pass

class EnergyReading(EnergyReadingBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
