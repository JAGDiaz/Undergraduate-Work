from sympy import ordered, Matrix
from sympy import hessian as h
from sympy.abc import x, y
from sympy.utilities.lambdify import lambdify
import numpy as np


def normalize(v):
    return v/np.linalg.norm(v, ord=2)


def make_grad_hess(funk, *args):
    g = funk(*args)

    vars = list(ordered(g.free_symbols))
    gradient = lambda func, frees: Matrix([func]).jacobian(frees)

    gradi = lambdify(vars, gradient(g, vars))
    hessi = lambdify(vars, h(g, vars))

    return gradi, hessi


def get_alpha(rho, cee, grad, funk, ex, pea):
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
    while funk(*(ex + alpha*pea)) > funk(*ex) + cee*alpha*np.dot(pea, grad):
        alpha *= rho
    return alpha


r = .5
c = 1e-4
#dx = 1e-4
n = int(3e4)
tolerance = 1e-8
a = 1

x_steepest = [None, None]
x_newton = [None, None]

f = lambda x1, x2: 100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2

gradient, hessian = make_grad_hess(f, x, y)


for j, x0 in enumerate([[1.2, 1.2], [-1.2, 1]]):
    x = np.zeros(shape=(n, 2), dtype=np.float64)
    x[0] = x0

    nabla_f = gradient(*x[0]).flatten()
    i = 1
    while np.abs(f(*x[i-1])) > tolerance and np.linalg.norm(nabla_f) > tolerance and i < n:
        p = -normalize(nabla_f)
        x[i] = x[i-1] + a*p
        a = get_alpha(r, c, nabla_f, f, x[i], p)
        nabla_f = gradient(*x[i]).flatten()
        i += 1

    print("Steepest Descent Method")
    print(f"x_{i-1}: {x[i-1]}, f at that point: {f(*x[i-1])}")
    x_steepest[j] = np.copy(x[:i])
    del x
    print(f"First 6 values of x: \n{x_steepest[j][:6]}")
    print(f"Last 6 values of x: \n{x_steepest[j][-6:]}\n\n")

for j, x0 in enumerate([[1.2, 1.2], [-1.2, 1]]):
    x = np.zeros(shape=(n, 2), dtype=np.float64)
    x[0] = x0

    nabla_f = gradient(*x[0]).flatten()
    hess = hessian(*x[0])
    p = -np.dot(np.linalg.inv(hess), nabla_f)

    i = 1
    while np.abs(f(*x[i-1])) > tolerance and np.linalg.norm(nabla_f) > tolerance and i < n:
        x[i] = x[i-1] + a*p
        hess = hessian(*x[i-1])
        p = -np.dot(np.linalg.inv(hess), nabla_f)
        nabla_f = gradient(*x[i]).flatten()
        a = get_alpha(r, c, nabla_f, f, x[i], p)
        i += 1

    print("Newton's Method")
    print(f"x_{i-1}: {x[i-1]}, f at that point: {f(*x[i-1])}")
    x_newton[j] = np.copy(x[:i])
    del x
    print(f"First 6 values of x: \n{x_newton[j][:6]}")
    print(f"Last 6 values of x: \n{x_newton[j][-6:]}\n\n")

x_s1, x_s2 = x_steepest
x_n1, x_n2 = x_newton

x_s1 -= 1
x_s2 -= 1
x_n1 -= 1
x_n2 -= 1

x_s1 = np.linalg.norm(x_s1, ord=2, axis=1)
x_s2 = np.linalg.norm(x_s2, ord=2, axis=1)
x_n1 = np.linalg.norm(x_n1, ord=2, axis=1)
x_n2 = np.linalg.norm(x_n2, ord=2, axis=1)


ps1 = np.polyfit(np.log(x_s1[:-1]), np.log(x_s1[1:]), 1)
print(f"ps1:{ps1}")
ps2 = np.polyfit(np.log(x_s2[:-1]), np.log(x_s2[1:]), 1)
print(f"ps2:{ps2}")
pn1 = np.polyfit(np.log(x_n1[:-1]), np.log(x_n1[1:]), 1)
print(f"ns1:{pn1}")
pn2 = np.polyfit(np.log(x_n2[:-1]), np.log(x_n2[1:]), 1)
print(f"ns2:{pn2}")


