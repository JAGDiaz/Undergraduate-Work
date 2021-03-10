"""
Author: Joseph Diaz
Course: Math 693-A

This program optimizes the Rosenbrock function from a pair of
given starting points on the manifold using the Steepest Descent
and Newton Methods.
"""
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
plt.rcParams['text.usetex'] = True


def f(ex):
    return 100 * (ex[1] - ex[0] ** 2) ** 2 + (1 - ex[0]) ** 2


def normalize(v):
    return v/np.linalg.norm(v, ord=2)


def get_grad(funk, ex, dh):
    """
    This function computes the numerical gradient of a function of
    multiple variables using a difference quotient schema.
    :param funk:
    :param ex:
    :param dh:
    :return:
    """
    x_mat = np.repeat([ex], repeats=ex.size, axis=0)
    off = dh*np.eye(ex.size)
    x_minus = x_mat - off
    x_plus = x_mat + off
    backward_diff = np.fromiter(map(funk, x_minus), dtype=ex.dtype)
    forward_diff = np.fromiter(map(funk, x_plus), dtype=ex.dtype)
    return (forward_diff - backward_diff)/(2*dh)


def get_hessian(ex, grad_finder, dh, funk):
    """
    This function computes the Jacobian of the gradient of a function,
    at a given point; which is equivalent to the Hessian of the function
    at that point.
    :param grad_finder:
    Callable function that computes the Gradient at a given point.
    :param funk:
    Function whose Gradient and Hessian we want.
    :param ex:
    The point for which we want the Gradient and Hessian.
    :param dh:
    Step size on each variable.
    :return:
    Hessian Matrix for ex.
    """
    grad = grad_finder(funk, ex, dh)
    dxj = np.where(grad < dh, dh, grad*dh)
    x_plus = np.repeat([ex], repeats=ex.size, axis=0) + dxj * np.eye(ex.size)
    hessian = np.empty(shape=(ex.size, ex.size), dtype=ex.dtype)
    for j in range(ex.size):
        hessian[j] = (grad_finder(funk, x_plus[j], dh) - grad) / dxj[j]
    return hessian


def get_alpha(grad, funk, ex, pea, rho=.5, cee=1e-4):
    """
    This function finds alpha using the backtracking line search method.
    :param alpha:
    :param rho:
    :param cee:
    :param grad:
    :param funk:
    :param ex:
    Current point of optimization, n by 1 array.
    :param pea:
    Line search direction; n by 1 array.
    :return:
    """
    alpha = 1
    while funk(ex + alpha*pea) > funk(ex) + cee*alpha*np.dot(pea, grad):
        alpha *= rho
    return alpha


dx = 1e-8
n = int(3e4)
tolerance = 1e-8

x_steepest = [None, None]
x_newton = [None, None]
x_nought = [[1.2, 1.2], [-1.2, 1]]


# Steepest Descent Method for p
for j, x0 in enumerate(x_nought):
    xs = np.zeros(shape=(n, 2), dtype=np.float64)
    x = np.array(x0)

    begin = datetime.now()

    nabla_f = get_grad(f, x, dx)
    p = -normalize(nabla_f)
    a = get_alpha(nabla_f, f, x, p)

    i = 0
    while np.abs(f(x)) > tolerance and np.linalg.norm(nabla_f, ord=2) > tolerance and i < n:
        x += a*p
        xs[i] = x
        nabla_f = get_grad(f, x, dx)
        p = -normalize(nabla_f)
        a = get_alpha(nabla_f, f, x, p)
        i += 1

    print(f"Steepest Descent Method; starting at x0 = {x0}.")
    print(f"x_{i-1}: {xs[i-1]}, f at that point: {f(xs[i-1])}")
    x_steepest[j] = np.copy(xs[:i])
    del xs
    print(f"First 6 values of x: \n{x_steepest[j][:6]}")
    print(f"Last 6 values of x: \n{x_steepest[j][-6:]}\n")
    print(f"That took: {datetime.now() - begin}\n")


# Newton's Method for p.
for j, x0 in enumerate(x_nought):
    xs = np.zeros(shape=(n, 2), dtype=np.float64)
    x = np.array(x0)

    begin = datetime.now()

    nabla_f = get_grad(f, x, dx)
    hess = get_hessian(x, get_grad, dx, f)
    p = -np.dot(np.linalg.inv(hess), nabla_f)
    a = get_alpha(nabla_f, f, x, p)

    i = 0
    while np.abs(f(x)) > tolerance and np.linalg.norm(nabla_f, ord=2) > tolerance and i < n:
        x += a*p
        xs[i] = x
        nabla_f = get_grad(f, x, dx)
        hess = get_hessian(x, get_grad, dx, f)
        p = -np.dot(np.linalg.inv(hess), nabla_f)
        a = get_alpha(nabla_f, f, x, p)
        i += 1

    print(f"Newton's Method; starting at x0 = {x0}")
    print(f"x_{i-1}: {xs[i-1]}, f at that point: {f(xs[i-1])}")
    x_newton[j] = np.copy(xs[:i])
    del xs
    print(f"First 6 values of x: \n{x_newton[j][:6]}")
    print(f"Last 6 values of x: \n{x_newton[j][-6:]}\n")
    print(f"That took: {datetime.now() - begin}\n")


x_s1, x_s2 = x_steepest
x_n1, x_n2 = x_newton
del x_steepest
del x_newton

sols1 = np.copy(x_s1)
sols2 = np.copy(x_s2)
soln1 = np.copy(x_n1)
soln2 = np.copy(x_n2)

x_s1 -= 1
x_s2 -= 1
x_n1 -= 1
x_n2 -= 1

x_s1 = np.linalg.norm(x_s1, ord=2, axis=1)
x_s2 = np.linalg.norm(x_s2, ord=2, axis=1)
x_n1 = np.linalg.norm(x_n1, ord=2, axis=1)
x_n2 = np.linalg.norm(x_n2, ord=2, axis=1)

print("Steepest Descent Method")
ps1 = np.polyfit(np.log(x_s1[:-1]), np.log(x_s1[1:]), 1)
print(f"Rate of convergence, x0 = (1.2, 1.2): {ps1[0]:5.6f}")
ps2 = np.polyfit(np.log(x_s2[:-1]), np.log(x_s2[1:]), 1)
print(f"Rate of convergence, x0 = (1.2, -1): {ps2[0]:5.6f}\n\n")

print("Newton's Method: ")
pn1 = np.polyfit(np.log10(x_n1[:-1]), np.log10(x_n1[1:]), 1)
print(f"Rate of convergence, x0 = (1.2, 1.2): {pn1[0]:5.6f}")
pn2 = np.polyfit(np.log10(x_n2[:-1]), np.log10(x_n2[1:]), 1)
print(f"Rate of convergence, x0 = (1.2, -1): {pn2[0]:5.6f}")


fig, ax = plt.subplots(2, 1, figsize=(12, 10))

ax[0].plot(np.log10(f(sols1.T)), '-k', label=r"$\vec{x}_0 = (1.2, 1.2)$")
ax[0].plot(np.log10(f(sols2.T)), '-r', label=r"$\vec{x}_0 = (-1.2, 1)$")
ax[0].set_ylabel(r"$\log_{10}\left(f(\vec{x}_k)\right)$", size=20)
ax[0].legend(loc='upper right', fontsize=20)
ax[0].set_title("Steepest Descent Algorithm", size=25)

ax[1].plot(np.log10(f(soln1.T)), '-k', label=r"$\vec{x}_0 = (1.2, 1.2)$")
ax[1].plot(np.log10(f(soln2.T)), '-r', label=r"$\vec{x}_0 = (1.2, -1)$")
ax[1].set_xlabel("$k$", size=20)
ax[1].set_ylabel(r"$\log_{10}\left(f(\vec{x}_k)\right)$", size=20)
ax[1].legend(loc='lower left', fontsize=20)
ax[1].set_title("Newton's Method Algorithm", size=25)

plt.show()

