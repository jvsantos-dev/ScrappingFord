import json
from pathlib import Path
from fastapi import APIRouter

router = APIRouter(prefix="/cars", tags=["cars"])

MOCK_DATA = Path(__file__).parent.parent / "api" / "mock_data.json" # path pra pegar a api/mock_data

@router.get("/")
def get_cars():
    if MOCK_DATA.exists():
        with open(MOCK_DATA, "r", encoding="utf-8") as f:
            return json.load(f)
    return []
