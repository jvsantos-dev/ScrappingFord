from pydantic import ConfigDict, Field
from .constants import BaseSchema

class CategoryCreate(BaseSchema):
    name: str = Field(..., min_length=2, max_length=100)
    description: str = Field(..., min_length=2, max_length=225)

