import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
plt.rcParams['savefig.format'] = 'jpg'

r = np.linspace(-3.5, 3.5, 1001)

x = np.zeros(r.size)
x = np.where((-1 <= r) & (r <= 1), x+1, x)
x = np.where((-2 <= r) & (r <= 2), x+3, x)
x = np.where(0 <= r, x+1, x)
x = np.where(3 < r, x-1, x)


fig, ax = plt.subplots(1,1, figsize=(12, 8))
ax.plot(r, x, ':k')
off = 1/7
ax.axhline(y=5, xmin=.5, xmax=.5+off, lw=3, color='k', label="$f$")
ax.axhline(y=4, xmin=.5-off, xmax=.5, lw=3, color='k')
ax.axhline(y=4, xmin=.5+off, xmax=.5+2*off, lw=3, color='k')
ax.axhline(y=0, xmin=0, xmax=1.5*off, lw=3, color='k')
ax.axhline(y=3, xmin=1.5*off, xmax=2.5*off, lw=3, color='k')
ax.axhline(y=1, xmin=5.5*off, xmax=6.5*off, lw=3, color='k')
ax.axhline(y=0, xmin=6.5*off, lw=3, color='k')
ax.grid()

ax.set_xlim(r.min(), r.max())
ax.set_xlabel("$x$", size=20)
ax.set_ylabel("$y$", size=20)
ax.set_title(r"$f = \chi_{[-1,1]} + 3\chi_{[-2,2]} + \chi_{[0,\infty)}-"
             r"\chi_{(3,\infty)}$", size=25)

ax.legend(loc='upper left', fontsize=20)
fig.savefig("HW2P4")

