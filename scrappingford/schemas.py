from pydantic import BaseModel, ConfigDict, Field

class CarSchema(BaseModel):
    marca: str = Field(examples = ["Ford"])
    ano: int = Field(examples = [1])