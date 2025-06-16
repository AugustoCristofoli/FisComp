import numpy as np
import matplotlib.pyplot as plt
A = 2
B = 0.5
OMEGA = np.pi


def derivative(f,x, dx):
    return (f(x+dx) - f(x-dx))/(2*dx)

def second_derivative(f, x, dx):
    return (f(x-dx) - (2*f(x)) + f(x+dx))/(dx**2)

def f(t):
    return (A*np.sin((OMEGA*t)))+(B*(t**2))

def velocity(f,t, dx):
    return derivative(f, t, dx)

def analytic_velocity(t):
    return 2*OMEGA*np.cos(OMEGA*t)+t

def acceleration(f, t, dx):
    return second_derivative(f, t, dx)

def analytic_acceleration():
    return 1 - 2*(OMEGA**)2*np.sin(OMEGA*t)



t = np.arange(0, 10.1, 0.1)



velocities = velocity(f, t, 1e-9)
analytic_velocities = analytic_velocity(t)


plt.plot(t, velocities, '*--', color='blue', label='Velocidade Numérica')
plt.plot(t, analytic_velocities, color='red', label='Velocidade Analitica')
plt.ylabel('Tempo (s)')
plt.xlabel('Velocidade (m/s)')
plt.legend()
plt.grid()
plt.show()