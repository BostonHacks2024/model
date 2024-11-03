import requests 
from Location import Location
import random

API_URL = "https://open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=wind_speed_10m,wind_direction_10m"

def get_wind_data(point: Location) -> tuple[float, float]:

    response = requests.get(API_URL.format(latitude=point.x, longitude=point.y))
    if response.status_code != 200:
        raise ImportError

    data = response.json()
    wind_speed = float(data["current"]["wind_speed_10m"])
    wind_direction = float(data["current"]["wind_direction_10m"])
    return wind_speed, wind_direction
    
def _get_wind_data(point: Location) -> tuple[float, float]:
    base_wind_speed = 5.0
    wind_speed_variation = 5.0 

    wind_speed = base_wind_speed + random.uniform(-wind_speed_variation, wind_speed_variation)

    base_wind_direction = random.choice([0, 90, 180, 270])
    wind_direction_variation = 30
    wind_direction = (base_wind_direction + random.uniform(-wind_direction_variation, wind_direction_variation)) % 360

    wind_speed = max(0, wind_speed)

    return wind_speed, wind_direction
