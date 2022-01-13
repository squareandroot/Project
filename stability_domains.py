import numpy as np
import matplotlib.pyplot as plt
import nodepy.linear_multistep_method as lm

ab3 = lm.Adams_Bashforth(3)
am3 = lm.Adams_Moulton(3)
ny3 = lm.Nystrom(3)
theta_plot = np.exp(1j * np.linspace(0, 2*np.pi, 100))

mu_ab3 = (theta_plot**3 - theta_plot**2) / (23/12 * theta_plot**2 - 16/12 * theta_plot + 5/12)
mu_am3 = (theta_plot**3 - theta_plot**2) / (9/24 * theta_plot**3 + 19/24 * theta_plot**2 - 5/24 * theta_plot + 1/24)
mu_ny3 = (theta_plot**3 - theta_plot) / (7/3 * theta_plot**2 - 2/3 * theta_plot + 1/3)

methods = [mu_ab3, mu_am3, mu_ny3]

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 6))
for i in range(3):
    axes[i].set_aspect("equal")
for i, m in enumerate(methods):
    axes[i].fill(np.real(m), np.imag(m), color="orange", alpha=0.8)
    axes[i].spines['left'].set_position('zero')
    axes[i].spines['right'].set_color('none')
    axes[i].spines['bottom'].set_position('zero')
    axes[i].spines['top'].set_color('none')

plt.savefig('plots/stability_domains.pdf', bbox_inches='tight', pad_inches=0.05)
