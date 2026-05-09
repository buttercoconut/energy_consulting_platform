from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class EnergyDataBase(BaseModel):
    building_id: int
    timestamp: datetime
    consumption_kwh: float

class EnergyDataCreate(EnergyDataBase):
    pass

class EnergyDataResponse(EnergyDataBase):
    id: int

    class Config:
        orm_mode = True

class ReportBase(BaseModel):
    building_id: int
    period_start: datetime
    period_end: datetime

class ReportCreate(ReportBase):
    pass

class ReportResponse(ReportBase):
    id: int
    recommendation: str
    savings_kwh: float
    savings_cost: float

    class Config:
        orm_mode = True
