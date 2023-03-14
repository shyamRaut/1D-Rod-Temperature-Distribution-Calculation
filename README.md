# 1D-Rod-Temperature-Distribution-Calculation
This code numerically approximates the temperature in a rod using the heat conduction equation:

heat equation

![heat equation](https://latex.codecogs.com/svg.latex?\frac{\partial%20U}{\partial%20t}%20=%20\alpha%20\frac{\partial^2%20U}{\partial%20x^2})


where:

U is the temperature of the rod at position x and time t (in Kelvin)
alpha is the thermal diffusivity of the rod (in m^2/s)
The rod has a length L (in meters) and is discretized into Nx points. The simulation runs for a total time of Time seconds, discretized into Nt time steps.

The initial condition is that the temperature throughout the rod is U0 Kelvin, and the boundary condition is that the temperature at the surface of the rod is U1 Kelvin.

Usage
To use this code, simply run it in a Python environment. The code will generate a plot of the temperature curve for all times.
