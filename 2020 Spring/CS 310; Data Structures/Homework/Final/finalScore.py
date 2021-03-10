#! /usr/bin/python3

import numpy as np

weights = np.array([.01, .02, .1, .2, .1, .04, .2, .03, .3, .1])
scores = np.array([18/20, 20/20, 95/100, 66/75, 95/100, 28/40, 72/100, 32/30, 90/100, 78/100])
print(np.sum(weights*scores))
