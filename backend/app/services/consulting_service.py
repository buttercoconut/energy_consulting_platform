import asyncio
from datetime import datetime
from ..api.schemas import ReportResponse
from ..api.models import ConsultingReport, Building
from ..config import settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

class ConsultingService:
    def __init__(self, session: AsyncSession = None):
        self.session = session or settings.async_session()

    async def generate_report(self, report_data) -> ReportResponse:
        # Dummy logic: calculate savings as 10% of total consumption
        result = await self.session.execute(select(Building).where(Building.id == report_data.building_id))
        building = result.scalar_one_or_none()
        if not building:
            raise ValueError("Building not found")
        # In real scenario, fetch energy data and compute
        savings_kwh = 100.0
        savings_cost = savings_kwh * 0.15
        report = ConsultingReport(
            building_id=report_data.building_id,
            period_start=report_data.period_start,
            period_end=report_data.period_end,
            recommendation="Install solar panels and upgrade insulation.",
            savings_kwh=savings_kwh,
            savings_cost=savings_cost,
        )
        self.session.add(report)
        await self.session.commit()
        await self.session.refresh(report)
        return ReportResponse.from_orm(report)
