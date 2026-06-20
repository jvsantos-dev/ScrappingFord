from pydantic import ConfigDict, Field
from .constants import BaseSchema

class BrandCreate(BaseSchema):
    name: str = Field(..., min_length=2, max_length=100)
    country: str = Field(..., min_length=2, max_length=100)
    foundation_year: int = Field(..., ge=1800)

class BrandUpdate(BaseSchema):
    name: str | None = None 
    country: str | None = None 
    foundation_year: int | None = None

class BrandResponse(BaseSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int 
    name: str 
    country: str 
    foundation_year: int