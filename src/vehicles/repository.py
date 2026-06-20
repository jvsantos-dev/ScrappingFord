from sqlalchemy import select 
from sqlalchemy.orm import Session 
from src.vehicles.models.vehicle import Vehicle 
from src.database.database import SessionLocal

class VehicleRepository:

    def __init__(self):
        self.session: Session = SessionLocal()

    def create(self, vehicle: Vehicle) -> bool:
        try:
            self.session.add(vehicle)
            self.session.commit()
            self.session.refresh(vehicle)
            return True 
        except Exception as e:
            print(e)
            self.session.rollback()
            return False
    
    def get_by_id(self, vehicle_id: int) -> Vehicle | None:
        return self.session.get(Vehicle, vehicle_id)
    
    def get_all(self) -> list[Vehicle]:
        statement = select(Vehicle)
        return list(self.session.scalars(statement))
    
    def update(self, vehicle: Vehicle) -> Vehicle:
        try:
            self.session.commit()
            self.session.refresh(vehicle)

            return vehicle 
        except Exception as e:
            print(e)
            self.session.rollback()
            raise
    
    def delete(self, vehicle: Vehicle) -> None:
        try:
            self.session.delete(vehicle)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise
    
    def close(self):
        self.session.close()

