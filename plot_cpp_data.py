import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(t)


step_sizes = [10, 100, 1000, 10000, 100000]

timings_RK4 = list()
data_RK4 = list()
timings_AB4 = list()
data_AB4 = list()

for k in step_sizes:
    filepath = "./out/RK4-" + str(k) + ".dat"
    with open(filepath) as fhand:
        t_space = np.linspace(0, 1, k + 1)
        y_temp = list()
        for i, l in enumerate(fhand):
            if i == 0:
                timings_RK4.append(float(l.strip(' ns\n')))
            else:
                y_temp.append(float(l.strip()))
        data_RK4.append(np.linalg.norm(np.exp(t_space) - y_temp))
    filepath = "./out/AB4-" + str(k) + ".dat"
    with open(filepath) as fhand:
        t_space = np.linspace(0, 1, k + 1)
        y_temp = list()
        for i, l in enumerate(fhand):
            if i == 0:
                timings_AB4.append(float(l.strip(' ns\n')))
            else:
                y_temp.append(float(l.strip()))
        data_AB4.append(np.linalg.norm(np.exp(t_space) - y_temp))

fig, ax1 = plt.subplots()
ax1.loglog(step_sizes, data_AB4, "o-", color="goldenrod", label="AB4")
ax1.loglog(step_sizes, data_RK4, "o-", color="peru", label="RK4")
ax1.set_ylabel("Absolute Error")
ax1.legend(loc=6)
ax2 = ax1.twinx()
ax2.loglog(step_sizes, timings_AB4, "o-", color="midnightblue", label="AB4")
ax2.loglog(step_sizes, timings_RK4, "o-", color="cornflowerblue", label="RK4")
ax2.set_ylabel("Execution time [ns]")
ax2.legend(loc=7)
plt.savefig("./plots/performance_RK_vs_LMM.pdf", bbox_inches='tight', pad_inches=0.05)