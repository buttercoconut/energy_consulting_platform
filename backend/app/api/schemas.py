"""Pydantic models for API payloads."""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class EnergyDataBase(BaseModel):
    building_id: int
    timestamp: datetime
    energy_kwh: float
    voltage: Optional[float] = None
    current: Optional[float] = None

class EnergyDataCreate(EnergyDataBase):
    pass

class EnergyData(EnergyDataBase):
    id: int

    class Config:
        orm_mode = True

class EnergyDataList(BaseModel):
    items: List[EnergyData]
    total: int

class AnalysisResult(BaseModel):
    building_id: int
    period_start: datetime
    period_end: datetime
    avg_consumption: float
    peak_consumption: float
    anomaly_detected: bool
    recommendation: str

class AnalysisResultList(BaseModel):
    items: List[AnalysisResult]
    total: int
