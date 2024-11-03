from api.Location import Location
from api.grid import build_grid
from api.utils import _get_wind_data
import math 
from tqdm import tqdm

def calculate_smoke_dispersion(source: Location, point: Location, wind_speed: float, wind_direction: float):

    # emission rate
    Q = 100 

    # effective height
    H = 80


    x0, y0 = source.x, source.y
    x_, y_ = point.x, point.y 

    # x = (x ′−x0​)cosθ+(y ′−y0)sinθ    |    y = -(x ′−x0​)sinθ+(y ′−y0)cosθ 
    x = (x_ - x0) * math.cos(wind_direction) + (y_ - y0) * math.sin(wind_direction)
    y = - (x_ - x0) * math.sin(wind_direction) + (y_ - y0) * math.cos(wind_direction)

    # dispersion coeffs:
    sigma_y, sigma_z = calculate_dispersion_coefficients(x)

    # DO FORMULA HERE
    answer = 0

    return answer

def calculate_dispersion_coefficients(x: float) -> tuple[float, float]:
    sigma_y = 0.22 * (x ** 0.5)
    sigma_z = 0.2 * x

    return sigma_y, sigma_z 

def simulate_smoke_dispersion(source: Location, radius: float, delta: float) -> list[tuple[Location, float]]:
    grid = build_grid(source, radius=radius, delta=delta)

    for index, point in tqdm(enumerate(grid), total=len(grid)):
        wind_speed, wind_direction = _get_wind_data(point)
        dispersion = calculate_smoke_dispersion(source, point, wind_speed, wind_direction)
        grid[index] = (grid[index], dispersion)
    
    return grid, radius, delta
