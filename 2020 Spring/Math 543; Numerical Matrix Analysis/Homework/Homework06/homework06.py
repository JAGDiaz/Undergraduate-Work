#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['savefig.format'] = 'jpg'

def get_ep_mach():
	ep = 1
	while(1 + ep != 1):
		ep /= 2
	return ep

A = np.array([[1,1],[1, 1.0001], [1, 1.0001]])
ANorm =  np.linalg.norm(A,2)
b = np.array([2, 0.0001, 4.0001])

Apinv = np.linalg.pinv(A)
x = Apinv@b
xNorm = np.linalg.norm(x, 2)

P = A@Apinv
y = P@b
yNorm = np.linalg.norm(y, 2)

kappa = ANorm*np.linalg.norm(Apinv,2)

theta = np.arccos(yNorm/np.linalg.norm(b, 2))

eta = (ANorm*xNorm)/yNorm

condNums = np.zeros((2,2))
condNums[0, 0] = 1./np.cos(theta)
condNums[0, 1] = (kappa/eta)*condNums[0, 0]
condNums[1, 0] = kappa*condNums[0, 0]
condNums[1, 1] = kappa + ((kappa**2)*np.tan(theta))/eta

ep = 1.23E-9
Aper = A + ep
AperNorm =  np.linalg.norm(Aper,2)
bper = b + ep

Aperinv = np.linalg.pinv(Aper)
xper = Aperinv@bper
xperNorm = np.linalg.norm(xper, 2)

Pper = Aper@Aperinv
yper = Pper@bper
yperNorm = np.linalg.norm(yper, 2)

kappaper = AperNorm*np.linalg.norm(Apinv,2)

thetaper = np.arccos(yperNorm/np.linalg.norm(bper, 2))

etaper = (AperNorm*xperNorm)/yperNorm

print(kappaper)
print(thetaper)
print(etaper)

condNumsper = np.zeros((2,2))
condNumsper[0, 0] = 1./np.cos(thetaper)
condNumsper[0, 1] = (kappaper/etaper)*condNumsper[0, 0]
condNumsper[1, 0] = kappaper*condNumsper[0, 0]
condNumsper[1, 1] = kappaper + ((kappaper**2)*np.tan(thetaper))/etaper

print(condNumsper)
#-----------------------------------------------------------------------------#

x = np.linspace(0,1,101)
ks = np.arange(500)
c = np.zeros(ks.size)

A = np.ones((x.size, ks.size))
for k in range(1,ks.size):
	A[:,k] = A[:,k-1]*x

for k in ks:
	Ainv = np.linalg.pinv(A[:,:k+1])
	c[k] = np.linalg.norm(A[:,:k+1], 2)*np.linalg.norm(Ainv, 2)

fig, ax = plt.subplots(figsize=(18,12))
ax.plot(np.log10(ks), np.log10(c), 'r-')
ax.set_ylabel(r"$\log_{10}\left(\kappa\left(A_k\right)\right)$", size=20)
ax.set_xlabel("$\log_{10}(k)$", size=20)
ax.tick_params(length=6, width=2, labelsize=20)
ax.set_title(r"Condition Number of Vandermonde Matrices $A_k \in \mathbb{R}^{101\times(k+1)}$", size = 20)
#ax.legend(loc=('best'))
fig.savefig("cVsk")

