from src.vehicles.models.vehicle import Vehicle
from src.vehicles.repository import VehicleRepository 

repository = VehicleRepository()

def get_vehicle_by_id(self, vehicle_id: int) -> Vehicle | None:
    return repository.get_by_id(vehicle_id)

def create_vehicle(self, vehicle: Vehicle):
        prediction = self.model.predict(vehicle)
        vehicle.success_rate = prediction
        return self.repository.create(vehicle)

    
def get_all_vehicles(self) -> list[Vehicle]:
    return repository.get_all()
    
def update_vehicle(self, vehicle: Vehicle) -> Vehicle:
    return repository.update(vehicle)
    
def delete_vehicle(self, vehicle_id: int) -> bool:
    return repository.delete(vehicle_id)