import numpy as np


def RK4(t0, tn, n, y0, f):
    h = abs(tn - t0) / n
    t = np.linspace(t0, tn, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    for i in range(n):
        K1 = f(t[i], y[i])
        K2 = f(t[i]+h/2, y[i] + K1*h/2)
        K3 = f(t[i]+h/2, y[i] + K2*h/2)
        K4 = f(t[i]+h, y[i] + K3*h)
        y[i+1] = y[i] + h/6 * (K1 + 2*K2 + 2*K3 + K4)
    return y
