from .constants import BaseSchema
from pydantic import Field
from datetime import datetime 

class VehicleCreate(BaseSchema):
    model: str = Field(..., min_length=2, max_length=100)
    version: str = Field(..., min_length=2, max_length=100)
    year: int = Field(..., ge=1900)
    price: float = Field(..., gt=0)
    colors: list[str] = Field(default_factory=list, max_length=20)

class VehicleUpdate(BaseSchema):
    model: str | None = None 
    version: str | None = None 
    year: int | None = Field(None, ge=1900)
    price: float | None = Field(None, gt=0)
    colors: list[str] | None = None

class VehicleResponse(BaseSchema):
    id: int 
    model: str 
    version: str 
    year: int 
    price: float 
    colors: list[str]
    created_at: datetime 
    updated_at: datetime