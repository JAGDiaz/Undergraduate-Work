#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg as lin

plt.rcParams['savefig.format'] = 'jpg'

# 24.3
for j in range(10):
	A = np.random.normal(size=(10,10)) - 2*np.diag(np.ones(10))
	w, v = np.linalg.eig(A)
	alpha = np.max(np.real(w))

	t = np.linspace(0, 20, 1001)
	eAlpha = np.exp(t*alpha)

	tA = np.array([i*A for i in t])

	normExptA = np.array([np.linalg.norm(lin.expm(i),2) for i in tA])

	fig, ax = plt.subplots(figsize=(16,12))
	ax.plot(t, np.log(normExptA), 'k-', label=r"$\log\left|\left|e^{tA}\right|\right|_2$")
	ax.plot(t, np.log(eAlpha), 'r-', label =r"$e^{\alpha(A)t}$")
	ax.set_title(r"Random $10 \times 10$ matrix run #%02d" % (j+1), size = 25)
	ax.set_ylabel(r"$y$", size = 20)
	ax.set_xlabel(r"$t$", size = 20)
	small=np.log(normExptA).min()<np.log(eAlpha).min()and np.log(normExptA).min()or np.log(eAlpha).min()
	ax.set_xlim(t.min(),)
	ax.legend(loc='best', fontsize = 20)
	ax.set_ylim(small,)
	plt.savefig("log2NormVst%02d" % j)

