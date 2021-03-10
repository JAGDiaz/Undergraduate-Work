#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['savefig.format'] = 'jpg'

x = np.linspace(1, 5, 1001)
F = 1 - x**(-4)


fig, ax = plt.subplots(figsize=(18,12))
ax.plot(x, F, 'r-')
ax.set_ylabel(r"$F(x)$", size=20)
ax.set_xlabel("$x$", size=20)
ax.tick_params(length=6, width=2, labelsize=20)
ax.set_title(r"CDF of $f(x)$", size = 20)
#ax.legend(loc=('best'))
fig.savefig("Stats14")
