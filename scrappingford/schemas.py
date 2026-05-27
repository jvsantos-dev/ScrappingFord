from pydantic import BaseModel, ConfigDict, Field

class CarSchema(BaseModel):
    marca: str = Field(examples = ["Ford"])
    ano: int = Field(examples = [1])


# from scrappingford.database import DataBase

# sql = """SELECT 1"""
# db = DataBase()

# print(db.execute(sql))