import numpy as np
def derivative(f,x, dx):
    return (f(x+dx) - f(x-dx))/(2*dx)

def right_derivative(f,x, dx):
    return (f(x+dx) - f(x))/dx

def f(x):
    return (x**3)*np.sin(x*(np.pi/180))


deltas = np.logspace(-16, 1 )

derivatives = derivative(f, 3, deltas)
right_derivatives = right_derivative(f, 3, deltas)

print(derivatives)
