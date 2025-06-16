import numpy as np

def pos(posInit, speedInit, acc, t):
    posf = posInit + (speedInit * t) +((acc * t**2)/2)
    return posf
def speed(speedInit, acc, t):
    speedF = speedInit + (acc * t)
    return speedF


# exericicio 1
t = np.arange(0, 52.5, 2.5)

# print(pos(0, 10, 5, t))

# ex 2
t = np.arange(0, 50.5, 0.5)
print(speed(0, 5, t))