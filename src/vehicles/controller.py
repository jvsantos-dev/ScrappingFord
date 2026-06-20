from fastapi import APIRouter
from src.vehicles.models.vehicle import Vehicle
from src.vehicles.repository import VehicleRepository 
from src.vehicles.schemas.vehicle import VehicleCreate
repository = VehicleRepository()
router = APIRouter()

@router.post("/vehicle")
def create_vehicle(vehicle: VehicleCreate):
    pass
    # entity = Vehicle(**vehicle.model_dump())

    # return service.create_vehicle(entity)


# @router.get("/vehicle/{vehicle_id}")
# async def get_vehicle_by_id(self, vehicle_id: int) -> Vehicle | None:
#     vehicle = await repository.get_by_id(vehicle_id)
#     if not vehicle:
#         raise 
#     return vehicle