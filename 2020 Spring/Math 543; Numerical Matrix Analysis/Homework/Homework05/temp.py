#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
plt.rcParams['savefig.format'] = 'jpg'

#a

ms = [8, 16, 32, 64, 128, 256, 512, 1024]
rho = np.array([])
rhoTemp = np.zeros(100)
for i in range(10):
	rho = np.append(rho, rhoTemp, axis=0)


print(rho.shape)
