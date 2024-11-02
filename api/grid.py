import numpy as np

def build_grid(x0: float, y0: float, radius = 10, delta = 0.1) -> np.vstack:

    x_min, x_max = x0 - radius, x0 + radius
    y_min, y_max = y0 - radius, y0 + radius

    x_values = np.arange(x_min, x_max, delta)
    y_values = np.arange(y_min, y_max, delta)

    X, Y = np.meshgrid(x_values, y_values)

    grid_points = np.vstack([X.ravel(), Y.ravel()]).T
    
    return grid_points
