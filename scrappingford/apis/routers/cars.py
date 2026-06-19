from fastapi import APIRouter
import pandas as pd
import json
from pathlib import Path

###
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent # get current file and climb 4 folders up
data_path = BASE_DIR / "data"

car_data = {}

for file in data_path.glob("*.csv"):
    brand = file.name.split("-")[0].lower()

    df = pd.read_csv(file)
    car_data[brand] = json.loads(df.to_json(orient="records"))
###

### 
router = APIRouter(
    prefix="/{brand}"
)
###

### all cars
@router.get("/")
async def send_cars(brand: str):
    key = brand.lower()
    
    if key in car_data:
        return car_data[key]
    
    return {"message": f"couldnt find {brand} data"}
###

### cars filtered per year
@router.get("/{car_year:int}")
async def send_year(brand: str, car_year: int):
    brand_key = brand.lower()

    if brand_key not in car_data:
        return {"message": f"couldnt find {brand} data"}
    
    brand_cars = car_data[brand_key]

    filtered_cars = [
        car for car in brand_cars
        if str(car_year) in str(car.get("yearFrom", ""))
    ]

    if not filtered_cars:
        return {"message": f"couldnt find year {car_year} in {brand}"}
    
    return filtered_cars
###

### cars filtered per name
@router.get("/{car_name:str}")
async def send_car(brand: str, car_name: str):
    brand_key = brand.lower()

    if brand_key not in car_data:
        return {"message": f"couldnt find {brand} data"}
    
    brand_cars = car_data[brand_key]
    
    filtered_cars = [
        car for car in brand_cars 
        if car_name.lower() in str(car.get("model", "")).lower()
    ]

    if not filtered_cars:
        return {"message": f"couldnt find {car_name} in {brand}"}

    return filtered_cars
###