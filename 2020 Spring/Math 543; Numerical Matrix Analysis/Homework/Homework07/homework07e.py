#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg as lin

plt.rcParams['savefig.format'] = 'jpg'

#26.2 

A = np.diag(-np.ones(32))
for i in range(A.shape[0] - 1):
	A[i, i+1] = 1
for i in range(A.shape[0] - 2):
	A[i, i+2] = 1


