#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1, 101)
ns = [1,2,3,4,5,6,7]
for n in ns:
	plt.plot(x, x/(1+10000*n*x))

plt.show()
