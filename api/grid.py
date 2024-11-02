import numpy as np
from Location import Location 

def build_grid(source: Location, radius=5, delta=0.1) -> list:
    x0 = source.x
    y0 = source.y

    x_min, x_max = x0 - radius, x0 + radius
    y_min, y_max = y0 - radius, y0 + radius

    x_values = np.arange(x_min, x_max, delta)
    y_values = np.arange(y_min, y_max, delta)
    X, Y = np.meshgrid(x_values, y_values)

    grid_points = [Location(x, y) for x, y in zip(X.ravel(), Y.ravel())]
    
    return grid_points
