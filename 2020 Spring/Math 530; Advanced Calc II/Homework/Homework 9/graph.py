#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5)
y1 = x
y2 = x**2

fill = [True if y2[i] < y1[i] else False for i in range(x.size)]

plt.plot(x,y1, 'k-')
plt.plot(x,y2, 'b-')
plt.fill_between(x, y1, y2, where=fill)
plt.show()
