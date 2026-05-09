from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..config import settings
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # relationships omitted for brevity

class Building(Base):
    __tablename__ = "buildings"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    name = Column(String, nullable=False)
    customer = relationship("Customer", backref="buildings")

class EnergyData(Base):
    __tablename__ = "energy_data"
    id = Column(Integer, primary_key=True)
    building_id = Column(Integer, ForeignKey("buildings.id"))
    timestamp = Column(DateTime, nullable=False)
    consumption_kwh = Column(Float, nullable=False)
    building = relationship("Building", backref="energy_data")

class ConsultingReport(Base):
    __tablename__ = "consulting_reports"
    id = Column(Integer, primary_key=True)
    building_id = Column(Integer, ForeignKey("buildings.id"))
    period_start = Column(DateTime, nullable=False)
    period_end = Column(DateTime, nullable=False)
    recommendation = Column(String, nullable=False)
    savings_kwh = Column(Float, nullable=False)
    savings_cost = Column(Float, nullable=False)
    building = relationship("Building", backref="reports")
