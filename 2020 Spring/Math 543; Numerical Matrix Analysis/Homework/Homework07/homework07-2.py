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



def householderRedux(A):
	for k in range(A.shape[0]-2):
		x = np.array(A[k+1:, k], copy=True)
		e = np.zeros(x.size)
		e[0] = 1
		v = np.transpose(np.array([np.sign(x[0])*np.linalg.norm(x,2)*e + x], copy=True))
		v = v/np.linalg.norm(v,2)
		A[k+1:, k:] = A[k+1:, k:] - 2*v@(np.transpose(v)@A[k+1:, k:])
		A[: ,k+1: ] = A[: ,k+1: ] - 2*(A[: ,k+1: ]@v)@np.transpose(v)
	return A

def isHessenberg(A, tol):
	for j in range(0,A.shape[0]):
		for i in range(j+2, A.shape[1]):
			if(A[i,j] > tol):
				return False
	return True

def RayleighIter(A, vIn, maxiter):
	v = np.array(vIn/np.linalg.norm(vIn,2), copy=True)
	lam = v@A@np.transpose(v)
	k = 0
	while(k < maxiter):
		k = k + 1
		if(np.abs(np.linalg.det(A - lam*np.diag(np.ones(A.shape[0]))))<1e-15):
			return 0, v
		w = np.linalg.solve(A - lam*np.diag(np.ones(A.shape[0])), v)
		v = w/np.linalg.norm(w, 2)
		lam = v@A@np.transpose(v)

	return lam, v


for i in range(10):
	A = np.random.normal(size=(10,10))
	x = np.random.normal(size=(10))
	lam, x = RayleighIter(A,x,1e4)

	u,v = np.linalg.eig(A)
	for s in u:
		if(np.abs(s - lam)<1e-9):
			print(True)

#for i in range(10):
#	A = np.random.normal(size=(2**(i+1),2**(i+1)))
#	B = householderRedux(A)
#	print(isHessenberg(B, 1e-14))

	

