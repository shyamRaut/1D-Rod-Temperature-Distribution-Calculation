import numpy as np
import matplotlib.pyplot as plt
import math

# Define the parameters
L = 1.0  # length of the rod in meter
Time = 10.0  # total time in sec
alpha = 1  # thermal diffusivity
Nx = 100  # number of points to discretize the rod
Nt = 1000  # number of time steps
N = 200  # number of terms to approximate the solution

# Define the initial conditions
U0 = 100.0+273  # initial temperature in kelvin
U1 = 0.0+273  # surface temperature in kelvin

# Define the discretization
x = np.linspace(0, L, Nx)
t = np.linspace(0, Time, Nt)
dx = L / (Nx - 1)
dt = Time / (Nt - 1)

# Define the temperature equation
U = np.zeros((Nx, Nt))
for j in range(Nt):
    for i in range(Nx):
        for k in range(1, N + 1):
            ln = k * math.pi / L
            U[i, j] = U[i, j] + (2 * (U0 - U1) / math.pi) * ((1 - (-1) ** k) / k) * (
                (math.sin(ln * x[i])) * math.exp(-alpha * ln ** 2 * t[j]))


# Plot the temperature curve for all time
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlabel('Distance in meter')
ax.set_ylabel('Temperature in kelvin')
ax.set_title('Temperature Curve T(x,t)')
for i in range(Nt):
    ax.plot(x, U[:, i], color='blue', alpha=0.1)
plt.show()
