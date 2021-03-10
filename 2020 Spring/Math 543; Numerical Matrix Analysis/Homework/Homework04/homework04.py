#! /usr/bin/python3

import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['text.usetex'] = True
plt.rcParams['savefig.format'] = 'jpg'


def modified_GS(A):
	V = np.copy(A)
	r = np.zeros((A.shape[1], A.shape[1]))
	q = np.zeros(A.shape)
	for i in range(V.shape[1]):
		r[i,i] = np.linalg.norm(V[:,i], 2)
		q[:,i] = V[:,i]/r[i,i]
		for j in range(i+1, V.shape[1]):
			r[i, j] = np.dot(q[:,i], V[:,j])
			V[:, j] = V[:, j] - r[i,j]*q[:,i]
	return q, r

def classic_GS(A):
	r = np.zeros((A.shape[1], A.shape[1]))
	q = np.zeros(A.shape)
	for j in range(A.shape[1]):
		v = np.copy(A[:,j], order='K')
		for i in range(j):
			r[i,j] = np.dot(q[:,i],A[:,j])
			v = v - r[i,j]*q[:,i]
		r[j,j] = np.linalg.norm(v)
		q[:,j] = v/r[j,j]
	return q, r

def get_Machine_Ep():
	ep = 1
	while(1 + ep != 1):
		ep /= 2
	return ep

def matrix_Print(A):
	for i in A:
		print(i)

def is_Up_Tri(A, tol):
	if(A.shape[0] != A.shape[1]):
		return False
	for i in range(A.shape[0]):
		for j in range(i + 1, A.shape[0]):
			if(np.abs(A[j,i]) > tol):
				return False
	return True

def is_Low_Tri(A, tol):
	if(A.shape[0] != A.shape[1]):
		return False
	for i in range(A.shape[0]):
		for j in range(i + 1, A.shape[0]):
			if(np.abs(A[i,j]) > tol):
				return False
	return True

def is_Unitary(A, tol):
	for i in range(A.shape[1]):
		if(np.abs(1-np.linalg.norm(A[:,i], 2)) > tol):
			return False
		for j in range(i+1,A.shape[1]):
			if(np.abs(np.dot(A[:,i],A[:,j])) > tol):
			  	return False
	return True


# Experiment 1
x = np.linspace(-1, 1, 256)
A = np.transpose(np.array([x**0, x, x**2, x**3]))
q,r = np.linalg.qr(A, 'reduced')
scale = q[-1,:]
qScale = q@np.diag(1/scale)


fig1, ax1 = plt.subplots(1, figsize=(18,12))
ax1.set_title("Approximation of First Four Legendre Polynomials", size = 30)
ax1.plot(x, qScale[:,0], 'k', label = "$Q_0(x)$")
ax1.plot(x, qScale[:,1], 'b', label = "$Q_1(x)$")
ax1.plot(x, qScale[:,2], 'r', label = "$Q_2(x)$")
ax1.plot(x, qScale[:,3], 'purple', label = "$Q_3(x)$")
ax1.set_xlabel("$x$", size = 20)
ax1.set_ylabel("$Q_i(x)$", size = 20)
ax1.legend(loc=('best'), prop={'size':20})
fig1.savefig("Legendre Polynomials Approximations")
#plt.show()

# Experiment 2
n = 80
u, X = np.linalg.qr(np.random.rand(n,n))
v, X = np.linalg.qr(np.random.rand(n,n))
S = np.diag(2.**(np.arange(-1, -n-1, -1)))

A = u@S@v

qc, rc = classic_GS(A)
qm, rm = modified_GS(A)


rcd = np.array([rc[i,i] for i in range(rc.shape[0])])
rmd = np.array([rm[i,i] for i in range(rm.shape[0])])
ep = get_Machine_Ep()
sqep = np.sqrt(ep)
t = np.arange(1,n+1,1)


fig2, ax2 = plt.subplots(1, figsize=(18,12))
ax2.set_title("Gram-Schmidt Stability; Modified vs. Classic", size = 25)
ax2.plot(t, np.log10(rcd), 'ko', label="Classic Gram-Schmidt")
ax2.plot(t, np.log10(rmd), 'cx', label="Modified Gram-Schmidt")
ax2.plot(t, np.log10(sqep*np.ones(t.size)), 'r--', label=r"$\sqrt{\varepsilon_{machine}}$")
ax2.plot(t, np.log10(ep*np.ones(t.size)), 'b--', label=r"$\varepsilon_{machine}$")
ax2.plot(t, np.log10(2.**(-t)), 'purple', label=r"$2^{-j}$")
ax2.set_xlabel("$j$", size = 25)
ax2.set_ylabel("$\log_{10}(r_{jj})$", size = 25)
ax2.legend(loc='best', prop={'size':20})
fig2.savefig("GS Stability; Modified vs Classic")
#plt.show()


# 9.1(b)
P = np.transpose(np.array([np.ones(x.size), x, 1.5*x**2 - .5, x*(2.5*x**2 - 1.5)]))

fig3, ax3 = plt.subplots(1, figsize=(18,12))
ax3.set_title("Difference of Legendre Polys and Approximations", size = 30)
ax3.plot(x, P[:,0] - qScale[:,0], 'k', label = "$(P_0-Q_0)(x)$")
ax3.plot(x, P[:,1] - qScale[:,1], 'b', label = "$(P_1-Q_1)(x)$")
ax3.plot(x, P[:,2] - qScale[:,2], 'r', label = "$(P_2-Q_2)(x)$")
ax3.plot(x, P[:,3] - qScale[:,3], 'purple', label = "$(P_3-Q_3)(x)$")
ax3.set_xlabel("$x$", size = 20)
ax3.set_ylabel("$P_i(x) - Q_i(x)$", size = 20)
ax3.legend(loc=('best'), prop={'size':20})
fig3.savefig("Legendre Polynomials Approximations vs True")
print(np.linalg.norm(P - qScale, np.inf))
