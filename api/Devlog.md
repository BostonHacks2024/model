# Simulating Smoke Dispersion

To simulate smoke dispersion with wind direction, wind speed, and the coordinates of the smoke source, we can create a simplified mathematical model. One approach to model the spread of smoke is based on Gaussian plume dispersion. This model is commonly used for air pollution and smoke dispersion, taking into account wind and atmospheric conditions.

## 1. Gaussian Plume Model Formula

The Gaussian plume formula predicts smoke concentration at any point
\((x, y, z)\)
(x,y,z) downwind of the source. In this context:

𝑥
x: Distance in the wind direction from the source (downwind).
𝑦
y: Lateral distance perpendicular to the wind direction.
𝑧
z: Height above the ground.
Given the wind direction, wind speed, and initial smoke location, the formula for concentration
𝐶
(
𝑥
,
𝑦
,
𝑧
)
C(x,y,z) at any point can be:

Coordinates of the Smoke Source
(
𝑥
0
,
𝑦
0
)
(x
0
​
,y
0
​
)
Your Input: You already have these coordinates, which will serve as the origin point for your model. 2. Wind Speed
𝑢
u
Source: Obtain this from weather data APIs or datasets. Websites like OpenWeatherMap, NOAA, or Windy provide real-time and historical wind speed data.
Assumption: If live data is unavailable, use an average regional wind speed for an approximation. 3. Wind Direction
𝜃
θ
Source: This is typically given in degrees and can also be obtained from weather data providers (same as above).
Transformation: Convert wind direction to radians if needed, and use it to rotate the coordinate system so that smoke dispersion aligns with the wind. 4. Emission Rate
𝑄
Q
Assumption: Estimating
𝑄
Q directly may be challenging without specifics on the fire intensity. However, you can:
Assume a standard emission rate if you only need relative concentrations.
Use a rough estimate based on typical wildfire emissions (e.g., a default
𝑄
Q value in environmental studies).
Alternative Approach: Start with a hypothetical
𝑄
Q value, then adjust it as needed if more precise information becomes available. 5. Effective Height
𝐻
H
Assumption: This value depends on the fire’s intensity and the atmospheric conditions, but a reasonable range for low-level smoke plumes might be around 10-100 meters above ground.
Approximation: If unknown, you might start with a midpoint value (e.g., 50 meters) and test different heights to observe effects. 6. Dispersion Coefficients
𝜎
𝑦
σ
y
​
and
𝜎
𝑧
σ
z
​

Empirical Estimates: In the absence of detailed atmospheric data, you can use empirical formulas commonly used in environmental modeling:
For neutral atmospheric stability:
𝜎
𝑦
=
0.22
𝑥
0.5
σ
y
​
=0.22x
0.5
and
𝜎
𝑧
=
0.2
𝑥
σ
z
​
=0.2x
For unstable conditions:
𝜎
𝑦
=
0.16
𝑥
0.8
σ
y
​
=0.16x
0.8
and
𝜎
𝑧
=
0.14
𝑥
0.8
σ
z
​
=0.14x
0.8

For stable conditions:
𝜎
𝑦
=
0.06
𝑥
σ
y
​
=0.06x and
𝜎
𝑧
=
0.03
𝑥
σ
z
​
=0.03x
Choice of Stability Condition: Atmospheric stability typically depends on time of day and weather. If unsure, assume neutral stability (common during daytime with mixed weather conditions).

## Steps:

Given: $x_0, y_0$ - coordinates of wildfire source.

1. Calculate $x, y$:
   $$x = (x' - x_0) \cos\theta + (y' - y_0)\sin\theta$$
