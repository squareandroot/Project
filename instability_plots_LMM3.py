import numpy as np
import matplotlib.pyplot as plt
from lmm_k3_unstable import LMM3


def f(t, y):
    return y


fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

x_plot_analytical = np.linspace(0, 1, 1000)

for i in range(3):
    axes[i].plot(x_plot_analytical, np.exp(
        x_plot_analytical), alpha=0.8, ls='--', color='orange')
    axes[i].set_ylim((0.8, 3.1))

y0 = LMM3(0, 1, 10, 1, f)
y1 = LMM3(0, 1, 20, 1, f)
y2 = LMM3(0, 1, 40, 1, f)

x0 = np.linspace(0, 1, 11)
x1 = np.linspace(0, 1, 21)
x2 = np.linspace(0, 1, 41)

axes[0].plot(x0, y0)
axes[1].plot(x1, y1)
axes[2].plot(x2, y2)

axes[0].set_title(r'$h = 0.1$')
axes[1].set_title(r'$h = 0.05$')
axes[2].set_title(r'$h = 0.025$')

plt.savefig('./plots/instability_LMM3.pdf',
            bbox_inches='tight', pad_inches=0.05)


def g(t, y):
    return 0


def LMM3_zero(t0, tn, n, y0, f):
    h = abs(tn - t0) / n
    t = np.linspace(t0, tn, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    y[1] = y0 + 1e-15
    K1 = f(t[0], y[0])
    for i in range(1, n):
        K2 = K1
        K1 = f(t[i], y[i])
        y[i+1] = h * (4 * K1 + 2 * K2) - 4 * y[i] + 5 * y[i-1]
    return y


N = 36
x = np.linspace(0, 1, N + 1)
y = LMM3_zero(0, 1, N, 1, g)
y_sol = np.ones(N + 1)

plt.figure()
plt.plot(x[-8:], y[-8:], label='Numerical solution')
plt.plot(x[-8:], y_sol[-8:], label='Analytical solution')

plt.legend(loc=6)

plt.savefig('./plots/zero_instability_LMM3.pdf',
            bbox_inches='tight', pad_inches=0.05)
