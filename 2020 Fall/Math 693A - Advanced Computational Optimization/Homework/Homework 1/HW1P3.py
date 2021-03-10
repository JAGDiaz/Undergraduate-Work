"""
Author: Joseph Diaz
Course: Math 693-A

This program creates a contour plot for the function listed in
Problem 3 of the homework.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
plt.rcParams['savefig.format'] = 'jpg'


a = 15
n = int(1e2)

x = y = np.linspace(-a, a, n)

x, y = np.meshgrid(x, y)

f = lambda X, Y: 5 - 5*X - 2*Y + 2*X**2 + 5*X*Y + 6*Y**2

z = f(x, y)

fig, ax = plt.subplots(1, 1, figsize=(18, 14))
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='magma')
ax.set_xlabel("$x$", size=25)
ax.set_ylabel("$y$", size=25)
ax.set_zlabel("$f(x,y)$", size=25)
ax.view_init(40, 340)

fig.suptitle("$f(x,y) = 5-5x-2y+2x^2+5xy+6y^2$\n"
             fr"$(x,y) \in [-{a},{a}] \times [-{a},{a}]$", size=30)

plt.show()

fig.savefig("HW1P3surface")
