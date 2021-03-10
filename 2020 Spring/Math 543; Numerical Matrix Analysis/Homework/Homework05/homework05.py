#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse as ellip
plt.rcParams['text.usetex'] = True
plt.rcParams['savefig.format'] = 'jpg'

#a

ms = np.array([8, 16, 32, 64, 128, 256, 512])
rhoTemp = np.zeros(100)
minsig = np.ones(ms.size)
prob = np.zeros(ms.size)
rho = np.zeros(ms.size)
norm2 = np.zeros(ms.size)
j = 0
for m in ms:
	mNegSqrt = 1./np.sqrt(m)
	circle = ellip((0,0), width=2, height=2, fc='none', ec='blue')
	fig, ax = plt.subplots(figsize=(12,12))
	for i in range(99):
		A = np.random.normal(loc = 0., scale = mNegSqrt, size = (m,m))
		s = np.linalg.svd(A, compute_uv= False)
		prob[j] += 1 if s[-1] < 1./m else 0
		minsig[j] = minsig[j] if minsig[j] < s[-1] else s[-1]
		eVals = np.linalg.eigvals(A)
		norm2[j] = norm2[j] if norm2[j] > np.linalg.norm(A,2) else np.linalg.norm(A,2)
		rhoTemp[i] = np.max(np.absolute(eVals))
		realVals = np.real(eVals)
		imagVals = np.imag(eVals)
		ax.plot(realVals, imagVals, 'ko')
		ax.set_xlabel(r"Real Part", size = 20)
		ax.set_ylabel(r"Imaginary Part", size = 20)
		ax.set_title(r"Eigenvalues of 100 random $A_{%d\times%d}$" %(m,m), size = 20)
	ax.axhline(y=0, color='k')
	ax.axvline(x=0, color='k')
	ax.add_patch(circle)
	ax.grid()
	ax.tick_params(length = 6, width = 2, labelsize = 20)
	fig.savefig("Eigenvals%04dby%04d" % (m, m))
	rho[j] = np.max(rhoTemp)
	prob /= 100.
	j += 1

fig, ax = plt.subplots(figsize=(16,16))
rhoMax = np.max(rho)
colors=['red','blue','yellow','purple','orange','cyan','pink']
merg=tuple(zip(rho,colors,ms))
for r,c,m in merg:
	circle = ellip((0,0), width=2*r, height=2*r, fc='none', ec=c, 
				label=r"$m = %d,\ \rho\left(A\right) = %1.2f$" % (m,r))
	ax.set_xlabel(r"$x$", size=20)
	ax.set_ylabel(r"$y$", size=20)
	ax.add_patch(circle)
	ax.set_xlim(-rhoMax-.1, rhoMax + .1)
	ax.set_ylim(-rhoMax-.1, rhoMax + .1)
ax.set_title(r"Spectral Radius $\rho\left(A\right)$ for random $A_{m \times m}$", size=20)
ax.grid()
ax.tick_params(length = 6, width = 2, labelsize = 20)
ax.legend(loc=('center'), fontsize = 20)
fig.savefig("rhoVsM")

fig, ax = plt.subplots(figsize=(16,16))
ax.plot(np.log2(ms), norm2, 'k-', label=r"$\left|\left| A \right|\right|_2$")
ax.plot(np.log2(ms), rho, 'r-', label=r"$\rho\left(A\right)$")
ax.set_xlabel(r"$\log_2(m)$", size=20)
ax.set_ylabel(r"$y$", size=20)
ax.tick_params(length = 6, width = 2, labelsize = 20)
ax.grid()
ax.legend(loc=('best'), fontsize = 20)
ax.set_title(r"2-norm and sprectral radius of random $A_{m \times m}$", size=20)
fig.savefig("normAVsM")

fig, ax = plt.subplots(figsize=(16,16))
ax.plot(np.log2(ms), minsig, 'r-', label=r"$\sigma_{min}$")
ax.plot(np.log2(ms), 1./ms, 'k-', label=r"$\frac{1}{m}$")
ax.set_xlabel(r"$\log_2(m)$", size=20)
ax.set_ylabel(r"$y$", size=20)
ax.tick_params(length = 6, width = 2, labelsize = 20)
ax.grid()
ax.legend(loc=('best'), fontsize = 20)
ax.set_title(r"$\sigma_{min}$ and $\frac{1}{m}$ for random $A_{m \times m}$", size=20)
fig.savefig("MinSigmInv")

fig, ax = plt.subplots(figsize=(16,16))
ax.plot(np.log2(ms), np.log10(prob), 'r-')
ax.set_xlabel(r"$\log_2(m)$", size=20)
ax.set_ylabel(r"$\log_{10}(p)$", size=20)
ax.tick_params(length = 6, width = 2, labelsize = 20)
ax.grid()
ax.set_title(r"Proportion of $A_{m \times m}$ matrices with $\sigma_{min} < \frac{1}{m}$", size=20)
fig.savefig("minSigProp")
