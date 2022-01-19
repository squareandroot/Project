import numpy as np
import matplotlib.pyplot as plt
from nystroem_k2 import Nystroem2
from nystroem_k3 import Nystroem3
from adams_bashforth_k3 import AdamsBashforth3
from scipy.integrate import RK45


def f1(t, y):
    return np.sin(y) + 3*y + t ^ 2 + 4


def f2(t, y):
    return 10 * (y - t**2/(t**2 + 1)) + 2*t/(t**2 + 1)**2


def f3(t, y):
    return (t - y)/2


def solf2(t):
    return t**2 / (t**2 + 1)


N = 100000
t = np.linspace(0, 2, N + 1)

sol_RK4 = RK45(f2, 0, [0, 0], 3).step()

plt.plot(sol_RK4)
plt.plot(t, solf2(t))
