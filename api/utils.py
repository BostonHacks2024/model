import requests 
from Location import Location

API_URL = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=wind_speed_10m,wind_direction_10m"

def get_wind_data(point: Location) -> tuple[float, float]:

    response = requests.get(API_URL.format(latitude=point.x, longitude=point.y))
    if response.status_code != 200:
        raise ImportError

    data = response.json()
    wind_speed = float(data["current"]["wind_speed_10m"])
    wind_direction = float(data["current"]["wind_direction_10m"])
    return wind_speed, wind_direction
    