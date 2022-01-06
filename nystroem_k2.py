import numpy as np
from runge_kutta_k4 import RK4


def Nystroem2(t0, tn, n, y0, f, procedure=None):
    h = abs(tn - t0) / n
    t = np.linspace(t0, tn, n+1)
    y = np.zeros(n+1)
    if not procedure:
        y[:2] = RK4(t0, t0 + h, 1, y0, f)
    elif procedure == 1:
        y[0] = y0
        y[1] = np.exp(-h)
    elif procedure == 2:
        y[0] = y0
        y[1] = 1 - h + 0.5 * h**2
    elif procedure == 3:
        y[0] = y0
        y[1] = 1 - h
    for i in range(1, n):
        y[i+1] = y[i-1] + 2 * h * f(t[i], y[i])
    return y
