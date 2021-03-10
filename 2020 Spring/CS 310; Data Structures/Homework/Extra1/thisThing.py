#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(1,2,1001)
y = .25*x**2 - .5*np.log(x)

plt.plot(x,y)
plt.show()
