import numpy as np
import matplotlib.pyplot as plt
from nystroem_k2 import Nystroem2


def f(t, y):
    return -y


fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 12))
stepsizes = [4, 8, 16]

x = np.linspace(0, 1, 1000)
y1 = x/6 * np.exp(-x)
y2 = np.exp(-x) * (2*x - 3) / 12 + np.exp(x) / 4
y3 = np.exp(-x) * (2*x - 3) / 12 - np.exp(x) / 4
axes[0, 0].plot(x, y1, color='grey')
axes[1, 0].plot(x, y1, color='grey')
axes[2, 0].plot(x, y2, color='grey')
axes[2, 0].plot(x, y3, color='grey')

for i in range(3):
    for k in stepsizes:
        x = np.linspace(0, 1, k+1)
        y = (Nystroem2(0, 1, k, 1, f, i+1) - np.exp(-x)) * k**2
        axes[i, 0].plot(x, y, label=r'$h = 1/{}$'.format(k))
        axes[i, 0].legend()
