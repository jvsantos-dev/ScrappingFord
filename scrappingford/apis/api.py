from fastapi import FastAPI
from routers import cars

app = FastAPI()

app.include_router(cars.router)

@app.get("/")
async def root():
    return {"message": "Hello"}

# /{name of brand} -> returns all data from that brand
# /{name of brand}/{name of car} -> returns data from that car
# /{name of brand}/{year} -> returns only cars from that year

#  fastapi dev scrappingford/apis/api.py