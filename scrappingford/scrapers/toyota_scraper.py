import re
from datetime import datetime
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

BASE_URL = "https://www.toyota.com"


# 🔹 1. Pegar modelos (Tacoma, Corolla, etc)
def get_models():
    url = f"{BASE_URL}/all-vehicles/"

    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    cars = []
    seen = set()
    current_year = datetime.now().year
    model_year_pattern = re.compile(r"^/([a-z0-9-]+)/([0-9]{4})(?:/|$)")

    for link in soup.find_all("a"):
        href = link.get("href")

        if not href:
            continue

        href = href.strip()
        if not href:
            continue

        if href.startswith("http"):
            parsed = urlparse(href)
            if "toyota.com" not in parsed.netloc:
                continue
            path = parsed.path.lower()
        else:
            path = href.lower()
            if not path.startswith("/"):
                continue

        match = model_year_pattern.match(path)
        if not match:
            continue

        model, year = match.groups()
        year = int(year)

        # Mantem apenas rotas de modelos com anos de linha plausiveis
        if (current_year - 1) <= year <= (current_year + 2) and model not in seen:
            seen.add(model)
            cars.append({"model": model, "year": year})

    return cars


def extract_hp_and_torque(text):
    hp = None
    torque = None

    hp_match = re.search(r'(\d+)\s*horsepower', text)
    torque_match = re.search(r'(\d+)\s*lb.-ft', text)

    if hp_match:
        hp = int(hp_match.group(1))

    if torque_match:
        torque = int(torque_match.group(1))

    return hp, torque


def get_car_data(cars):
    cars_data = []

    for car_info in cars:
        model = car_info["model"]
        year = car_info["year"]

        # 👉 monta URL de features automaticamente
        url = rf"https://www.toyota.com/{model}/features/mpg_other_price/"
        print(url)

        try:
            response = requests.get(url, headers=HEADERS, timeout=30)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            full_text = soup.get_text(separator=" ").lower()

            hp, torque = extract_hp_and_torque(full_text)

            # Fuel type
            fuel_type = None
            if "hybrid" in full_text:
                fuel_type = "hybrid"
            elif "gas" in full_text:
                fuel_type = "gasoline"

            # Transmission
            transmission = None
            if "manual" in full_text:
                transmission = "manual"
            elif "automatic" in full_text:
                transmission = "automatic"

            # Drivetrain
            drivetrain = None
            if "4wd" in full_text or "4x4" in full_text:
                drivetrain = "4x4"
            elif "awd" in full_text:
                drivetrain = "awd"

            car_data = {
                "name": model,
                "brand": "Toyota",
                "year": year,
                "type": "pickup",  # depois você melhora isso

                "hp": hp,
                "torque": torque,
                "fuel_type": fuel_type,

                "drivetrain": drivetrain,
                "transmission": transmission,

                "source": "toyota",
                "url": url,
                "last_update": datetime.now().isoformat()
            }

            cars_data.append(car_data)

        except Exception as e:
            print(f"Erro ao processar {model}: {e}")

    return cars_data

# https://www.toyota.com/{car}/features/mpg_other_price/
# 🔹 EXECUÇÃO COMPLETA
if __name__ == "__main__":
    print("🔍 Buscando modelos...")
    cars = get_models()
    print(get_car_data(cars))