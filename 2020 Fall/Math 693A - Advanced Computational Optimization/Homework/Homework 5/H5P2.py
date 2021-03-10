

import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['savefig.format'] = 'jpg'


def conj_grad(ei, ex, bee, tolerance=1e-6):
    """
    This method approximately solves a linear system to the
    given tolerance using the Conjugate Gradient method.
    :param ei:
    The matrix of the linear system.
    :param ex:
    The initial guess for our CG method.
    :param bee:
    The vector we are trying to find a solution for.
    :param tolerance:
    The 'precision' with which we want our solution
    to agree with the system.
    :return:
    Approximate solution to the system and an array
    of the residuals.
    """
    r_norms = [None]*1000
    exs = [None]*len(r_norms)
    are = ei.dot(ex) - bee
    pea = -are
    are_norm = norm(are, ord=2)
    k = 0
    while are_norm > tolerance:
        r_norms[k] = are_norm
        exs[k] = np.copy(ex)
        alpha = are_norm**2/(pea.dot(ei).dot(pea))
        ex += alpha*pea
        are += alpha*ei.dot(pea)
        beta = are.dot(are)/(are_norm**2)
        pea = beta*pea - are
        are_norm = norm(are, ord=2)
        k += 1
    return np.copy(ex), np.array(exs[:k]), np.array(r_norms[:k])


def classic_GS(A):
    r = np.zeros((A.shape[1], A.shape[1]))
    q = np.zeros(A.shape)
    for j in range(A.shape[1]):
        v = np.copy(A[:, j], order='K')
        for i in range(j):
            r[i, j] = np.dot(q[:, i], v)
            v -= r[i, j] * q[:, i]

        r[j, j] = norm(v, ord=2)
        if r[j, j] < 1e-12:
            r[j, j] = 1e-12
        q[:, j] = v / r[j, j]

    return q, r


np.random.seed(2*3*3*37)

n = 25
m = n//3

A1 = np.random.uniform(-10, 10, size=(n, n))
A2 = np.random.uniform(-10, 10, size=A1.shape)

V1, blah = classic_GS(A1)
V2, blah = classic_GS(A2)

d1 = np.random.uniform(-100, 100, size=(n,))
larges = np.random.uniform(100, 100_000, size=(m, ))
clustered = np.random.normal(loc=1, scale=1e-3, size=(n-m, ))
d2 = np.concatenate((larges, clustered))

D1 = np.diag(d1)
D2 = np.diag(d2)

A1 = V1.T@D1@V1
A2 = V2.T@D2@V2

b = np.ones(n)
x = np.zeros(n)

x1_star, x1, r1 = conj_grad(A1, x, b)
x2_star, x2,  r2 = conj_grad(A2, np.copy(x), b)

norm1 = norm(x1 - x1_star, ord=2, axis=1)
norm2 = norm(x2 - x2_star, ord=2, axis=1)


fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(2*np.log10(norm1), '--k', label="Uniformly distributed")
ax.plot(2*np.log10(norm2), '-k', label="Clustered")
ax.set_xlabel("$k$", size=20)
ax.set_ylabel(r"$\log_{10}\left(||x_k - x^*||^2\right)$", size=20)
ax.grid()

ax.legend(loc='lower left', fontsize=30)
ax.set_title("Eigenvalue Profiles of CG", size=30)

fig.savefig("EigValConjGradPlots")

plt.close(fig)
