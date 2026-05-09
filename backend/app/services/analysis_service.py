import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from ..api.schemas import EnergyDataCreate, EnergyDataResponse
from ..api.models import EnergyData, Building
from ..config import settings
from sqlalchemy.future import select

class DataCollectionService:
    def __init__(self, session: AsyncSession = None):
        self.session = session or settings.async_session()

    async def save_energy_data(self, data: EnergyDataCreate) -> EnergyDataResponse:
        energy = EnergyData(**data.dict())
        self.session.add(energy)
        await self.session.commit()
        await self.session.refresh(energy)
        return EnergyDataResponse.from_orm(energy)

    async def get_energy_data_by_building(self, building_id: int) -> list[EnergyDataResponse]:
        result = await self.session.execute(select(EnergyData).where(EnergyData.building_id == building_id))
        rows = result.scalars().all()
        return [EnergyDataResponse.from_orm(row) for row in rows]
