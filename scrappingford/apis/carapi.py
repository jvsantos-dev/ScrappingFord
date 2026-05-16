import requests
import pandas as pd
import time

brands = [
    "Ford",
    "Toyota",
    "Honda",
    "Chevrolet",
    "Nissan",
    "Hyundai",
    "Kia",
    "Volkswagen",
    "Jeep",
    "Mazda"
]

models = []

BASE_URL = "https://carapi.app/api"

for brand in brands:

    print(f"\nBuscando modelos da marca: {brand}")

    url_models = f"{BASE_URL}/models/v2?make={brand}"

    try:
        response_models = requests.get(url_models)
        response_json_models = response_models.json()
    except Exception as e:
        print(f"Brand não funcionou: {e}")
    time.sleep(10)
    models_data = response_json_models['data']

    for model in models_data:

        model_name = model['name']

        print(f"Modelo: {model_name}")

        url_trims = (
            f"{BASE_URL}/trims/v2?"
            f"make={brand}&model={model_name}"
        )

        try:
            response_trims = requests.get(url_trims)
        except Exception as e:
            print(e)
        time.sleep(10)

        try:
            trims_data = response_trims.json()['data']
        except:
            print(f"Erro ao buscar trims de {model_name}")
            continue

        for trim in trims_data:

            trim_id = trim['id']


            url_detail = f"{BASE_URL}/trims/v2/{trim_id}"

            try:
                response_detail = requests.get(url_detail)
            except Exception as e:
                print(e)
            time.sleep(10)

            try:
                detail = response_detail.json()
            except:
                print(f"Erro no trim {trim_id}")
                continue

            colors = []

            if detail.get('exterior_colors'):

                for color in detail['exterior_colors']:

                    if 'name' in color:
                        colors.append(color['name'])

                    elif 'color' in color:
                        colors.append(color['color'])

            body_type = None

            if detail.get('bodies'):

                if len(detail['bodies']) > 0:

                    body_type = detail['bodies'][0].get('type')

            transmission = None

            if detail.get('transmissions'):

                if len(detail['transmissions']) > 0:

                    transmission = detail['transmissions'][0].get(
                        'description'
                    )

            tank_capacity = None

            if detail.get('mileages'):

                if len(detail['mileages']) > 0:

                    tank_capacity = detail['mileages'][0].get(
                        'fuel_tank_capacity'
                    )
            car_data = {

                "id": trim_id,

                "brand": brand,

                "model": model_name,

                "year": detail.get('year'),

                "trim": detail.get('trim'),

                "description": detail.get('description'),

                "type": body_type,

                "transmission": transmission,

                "tank_capacity": tank_capacity,

                "colors": colors
            }

            models.append(car_data)

            time.sleep(10)

df = pd.DataFrame(models)

print(df.head())

print(f"\nTotal de veículos coletados: {len(df)}")

df.to_csv("cars.csv", index=False, encoding="utf-8")

print("Arquivo salvo: ford_cars.csv")