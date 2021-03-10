"""
Author: Joseph Diaz
Course: Math 693-A
Homework 4
Problem 2

This program uses the Conjugate Gradient method to solve a
linear system whose coefficient matrix is the Hilber matrix
for various dimensions n.
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm, cond

plt.rcParams['text.usetex'] = True
plt.rcParams['savefig.format'] = 'jpg'


def make_hilbert(n):
    assert n > 1 and isinstance(n, (int, np.int)), "Please use an integer greater than 1."
    hilbert_mat = np.array([[1/(i + j + 1) for i in range(n)] for j in range(n)])
    return hilbert_mat


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
    are = ei.dot(ex) - bee
    pea = -are
    are_norm = norm(are, ord=2)
    k = 0
    while are_norm > tolerance:
        r_norms[k] = are_norm
        alpha = are_norm**2/(pea.dot(ei).dot(pea))
        ex += alpha*pea
        are += alpha*ei.dot(pea)
        beta = are.dot(are)/(are_norm**2)
        pea = beta*pea - are
        are_norm = norm(are, ord=2)
        k += 1
    return ex, np.array(r_norms[:k])


ns = [5, 8, 12, 20]
x_sols = [None] * len(ns)
r_norms = [None] * len(ns)
iters = [None] * len(ns)
eigs = [None] * len(ns)
conds = [None] * len(ns)


for i, n in enumerate(ns):
    A = make_hilbert(n)
    eigs[i] = np.linalg.eig(A)[0]
    abs_eigs = np.abs(eigs[i])
    conds[i] = abs_eigs.max()/abs_eigs.min()
    b = np.ones(n)
    x = np.zeros(n)

    x_sols[i], r_norms[i] = conj_grad(A, x, b)
    iters[i] = len(r_norms[i])


fig, ax = plt.subplots(1, figsize=(12, 8))

ax.plot(ns, iters, '-k')
ax.grid()

ax.set_ylabel("Iterations", size=20)
ax.set_xlabel("$n$", size=20)
ax.set_title("Iterations for Standard CG on $H_n$", size=30)

fig.savefig("iterations_vs_n")


fig, ax = plt.subplots(1, figsize=(12, 8))

ax.set_ylabel(r"$\log_{10}\ ||r_k||_2$", size=20)
ax.set_xlabel("$k$", size=20)

for r_norm, n in zip(r_norms, ns):
    ax.plot(np.log10(r_norm), label=f"$||r_k||_2$ for $H_{{{n}}}$")
ax.grid()
ax.legend(loc='best', fontsize=15)

ax.set_title("Euclidean Norm of the Residuals vs. k", size=25)
fig.savefig("r_norm_vs_k_one")

fig, ax = plt.subplots(1, figsize=(12, 8))
ax.set_ylabel(r"$\log_{10}\ \left|\lambda_i\right|$", size=20)
ax.set_xlabel(r"$i$", size=20)
ax.set_xticks(np.arange(0, 21, 2))
ax.grid()

for eig, n in zip(eigs, ns):
    ax.plot(np.arange(n) + 1, np.log10(np.abs(eig)), '-', label=f"Eigenvalues of $H_{{{n}}}$")

ax.legend(loc='best', fontsize=15)
ax.set_title("Magnitude of Eigenvalues of $H_n$", size=25)

fig.savefig("eigs_plot")


fig, ax = plt.subplots(1, figsize=(12, 8))

ax.plot(ns, np.log10(conds), '-k')
ax.set_ylabel(r"$\log_{10}\ \kappa\left(H_n\right)$", size=20)
ax.set_xlabel("$n$", size=20)
ax.set_title("Condition Number of $H_n$", size=25)
ax.grid()

fig.savefig("condition_number_plot")


print("Approximate iterations for SD:")
for ex, cond in zip(x_sols, conds):
    norm_sol = norm(ex - np.ones(ex.size), ord=2)
    print(norm_sol)
    vep = 1e-6
    print(int((np.log(vep) - np.log(2*norm_sol))/(np.log(np.sqrt(cond)-1) - np.log(np.sqrt(cond)+1))))
