from sqlalchemy import func 
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()

@table_registry.mapped_as_dataclass
class User():
    __tablename__ = "carros"
    id: Mapped[int] = mapped_column(primary_key='True')
    car_name: Mapped[str] 
    marca: Mapped[str]
    motor: Mapped[str]
    ano: Mapped[int]