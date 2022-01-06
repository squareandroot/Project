import numpy as np
from runge_kutta_k4 import RK4


def LMM3(t0, tn, n, y0, f):
    h = abs(tn - t0) / n
    t = np.linspace(t0, tn, n+1)
    y = np.zeros(n+1)
    y[:2] = RK4(t0, t0 + h, 1, y0, f)
    K1 = f(t[0], y[0])
    for i in range(1, n):
        K2 = K1
        K1 = f(t[i], y[i])
        y[i+1] = h * (4 * K1 + 2 * K2) - 4 * y[i] + 5 * y[i-1]
    return y
