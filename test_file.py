import numpy as np
import matplotlib.pyplot as plt
import nodepy.linear_multistep_method as lm
from adams_bashforth_k3 import AdamsBashforth3
from nystroem_k3 import Nystroem3


def f(t, y):
    return y


N = 5
x_plot = np.linspace(0, 5, N + 1)
x_plot_analytical = np.linspace(0, 5, 100000)

plt.plot(x_plot, AdamsBashforth3(0, 5, N, 1, f))
plt.plot(x_plot, Nystroem3(0, 5, N, 1, f))
plt.plot(x_plot_analytical, np.exp(x_plot_analytical))
plt.show()


theta_plot = np.linspace(0, 2*np.pi, 100)

# mu_plot = (np.exp(1j * theta_plot)**4 - np.exp(1j * theta_plot)**3) / (55/25 * np.exp(1j * theta_plot)**3 - 59/24 * np.exp(1j * theta_plot)**2 + 37/24 * np.exp(1j * theta_plot) - 9/24)
mu_plot = (np.exp(1j * theta_plot)**3 - np.exp(1j * theta_plot)**2) / (23/12 * np.exp(1j * theta_plot)**2 - 16/12 * np.exp(1j * theta_plot) + 5/12)
plt.plot(np.real(mu_plot), np.imag(mu_plot))
plt.show()
mu_plot = (np.exp(1j * theta_plot)**3 - np.exp(1j * theta_plot)) / (7/3 * np.exp(1j * theta_plot)**2 - 2/3 * np.exp(1j * theta_plot) + 1/3)
plt.plot(np.real(mu_plot), np.imag(mu_plot))
plt.show()



ab3 = lm.Adams_Bashforth(3)
print(ab3)
ny3 = lm.Nystrom(3)
print(ny3)
ab3.plot_stability_region()
ny3.plot_stability_region()
