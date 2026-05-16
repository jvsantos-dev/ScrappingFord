from fastapi import FastAPI
from scrappingford.routers import cars

app = FastAPI(title="ScrappingFord API") 

app.include_router(cars.router)

@app.get("/")
def root():
    return {
        "message": "Bem-vindo à API ScrappingFord!",
        "rotas": "/cars"
    }
