from fastapi import APIRouter, Depends
from ..services.data_collection_service import DataCollectionService
from ..services.analysis_service import AnalysisService
from ..services.consulting_service import ConsultingService
from ..api.schemas import EnergyDataCreate, EnergyDataResponse, ReportCreate, ReportResponse

router = APIRouter()

# Dependency injection for services

def get_data_collection_service():
    return DataCollectionService()

def get_analysis_service():
    return AnalysisService()

def get_consulting_service():
    return ConsultingService()

@router.post("/energy-data", response_model=EnergyDataResponse)
async def create_energy_data(data: EnergyDataCreate, service: DataCollectionService = Depends(get_data_collection_service)):
    return await service.save_energy_data(data)

@router.get("/energy-data/{building_id}", response_model=list[EnergyDataResponse])
async def get_energy_data(building_id: int, service: DataCollectionService = Depends(get_data_collection_service)):
    return await service.get_energy_data_by_building(building_id)

@router.post("/analysis", response_model=list[ReportResponse])
async def analyze_energy(building_id: int, service: AnalysisService = Depends(get_analysis_service)):
    return await service.run_analysis(building_id)

@router.post("/report", response_model=ReportResponse)
async def create_report(report: ReportCreate, service: ConsultingService = Depends(get_consulting_service)):
    return await service.generate_report(report)
