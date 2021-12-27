import numpy as np
from runge_kutta_k4 import RK4


def Nystroem3(t0, tn, n, y0, f):
    h = abs(tn - t0) / n
    t = np.linspace(t0, tn, n+1)
    y = np.zeros(n+1)
    y[:3] = RK4(t0, t0 + 2*h, 2, y0, f)
    K1 = f(t[1], y[1])
    K2 = f(t[0], y[0])
    for i in range(2, n):
        K3 = K2
        K2 = K1
        K1 = f(t[i], y[i])
        y[i+1] = y[i-1] + h/3 * (7*K1 - 2*K2 + K3)
    return y
