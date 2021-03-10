#! /usr/bin/python3

import numpy as np
from matplotlib import pyplot as plt

def classic_GS(A):
	r = np.zeros((A.shape[1], A.shape[1]))
	q = np.zeros(A.shape)
	for j in range(A.shape[1]):
		v = np.copy(A[:,j], order='K')
		for i in range(j):
			r[i,j] = np.dot(q[:,i],v)
			v = v - r[i,j]*q[:,i]

		r[j,j] = np.linalg.norm(v)
		if(r[j,j] < 1e-12):
			r[j,j] = 1e-12
		q[:,j] = v/r[j,j]

	return q, r

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

A = np.zeros((120,10))
print("A is a %d by %d, with tolerance %1.3e" % (A.shape[0], A.shape[1], 1e-12))
q,r = classic_GS(A)
print("\nMy QR: Infinity norm of A - QR: %1.3e" % np.linalg.norm(A-q@r, np.inf))
print("My Q is unitary: ", is_Unitary(q,1e-12))
print("My R is upper triangular: ", is_Up_Tri(r, 1e-12))
print("--------------------------------------------------------------------")

pSizes = [(100,100,1e-12), (54,3,1e-13), (666,37,1e-14), (32,100,1e-15)]
for p in pSizes:
	print("A is a %d by %d, with tolerance %1.3e" % (p))

	Ar = np.random.randn(p[0],p[1])
	q,r = classic_GS(Ar)
	q1, r1 = np.linalg.qr(Ar, 'reduced')

	print("\nMy QR: Infinity norm of A - QR: %1.3e" % np.linalg.norm(Ar-q@r, np.inf))
	print("My Q is unitary: ", is_Unitary(q,p[2]))
	print("My R is upper triangular: ", is_Up_Tri(r, p[2]))

	print("\nPython's QR: Infinity norm of A - QR: %1.3e" % np.linalg.norm(Ar-q1@r1, np.inf))
	print("Python's Q is unitary: ", is_Unitary(q1,p[2]))
	print("Python's R is upper triangular: ", is_Up_Tri(r1,p[2]))
	print("--------------------------------------------------------------------")
