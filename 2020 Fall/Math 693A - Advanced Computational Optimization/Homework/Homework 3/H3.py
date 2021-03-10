"""
Author: Joseph Diaz
Course: Math 693-A
Homework 3

This program optimizes the Rosenbrock function from a pair of
given starting points on the manifold using the dogleg method.
"""

import numpy as np
from numpy.linalg import norm, inv
from sympy import ordered, Matrix
from sympy import hessian as h
from sympy.abc import x, y
from sympy.utilities.lambdify import lambdify
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['savefig.format'] = 'jpg'


def normalize(v):
    return v / norm(v, ord=2)


def quad_model(f_ex, grad_ex, hess_ex):
    """
    This function returns a lambda function that is a
    quadratic approximation of f at a point x.
    :param f_ex:
    f evaluated at x.
    :param grad_ex:
    The gradient of f at x.
    :param hess_ex:
    The hessian of f at x.
    :return:
    """
    return lambda pea: f_ex + pea@grad_ex + .5*pea@hess_ex@pea


def trust_region(x_init, func, m_func, grad_func, hess_func,
                 p_func, max_trust=5., tolerance=1e-8, init_trust=None):
    """
    This function uses the dogleg method of the trust
    region to find the minimizer of a function of 2
    variables.
    :param x_init:
    A list of initial starting points for the optimization.
    :param func:
    The function we would like to optimize.
    :param m_func:
    The function we use to construct a quadratic
    model.
    :param grad_func:
    A function to compute the gradient of func.
    :param hess_func:
    A function to compute the hessian of func.
    :param p_func:
    The function we use to find a search direction
    that minimizes the quadratic model.
    :param max_trust:
    The maximum radius of the trust region.
    :param tolerance:
    Tolerance for stopping criteria.
    :param init_trust:
    :return:
    """
    x_solutions = [None]*x_init.shape[0]
    max_trust = 1 if max_trust < tolerance else max_trust
    for n, x_0 in enumerate(x_init):
        x_sols = np.zeros(shape=(1_000, x_init.shape[1]))
        ex = np.copy(x_0).astype(dtype=np.float64)
        k = 0
        eta = np.random.uniform(tolerance, .25)
        trust_radius = max_trust*.5 if init_trust is None else init_trust
        grad_x = grad_func(*ex)
        hess_x = hess_func(*ex)
        quad_x = m_func(func(*ex), grad_x, hess_x)

        while norm(grad_x, ord=2) > tolerance:
            x_sols[k] = ex
            p_approx = p_func(grad_x, hess_x, trust_radius)
            rho_k = (func(*ex) - func(*(ex + p_approx)))/\
                    (func(*ex) - quad_x(p_approx))
            if rho_k < .25:
                trust_radius *= .25
            elif np.abs(norm(p_approx) - trust_radius) < tolerance:
                trust_radius = min(2*trust_radius, max_trust)
            if rho_k > eta:
                ex += p_approx
                grad_x = grad_func(*ex)
                hess_x = hess_func(*ex)
                quad_x = m_func(func(*ex), grad_x, hess_x)
                k += 1
        x_solutions[n] = x_sols[:k]

    return x_solutions


def tau_min(p_u, p_fs, trust_radius):
    return lambda tau: norm(p_u + (tau - 1)*(p_fs-p_u)) - trust_radius


def bisection(a_low, a_high, func, tolerance=1e-8):
    while np.abs(a_high - a_low) > tolerance:
        m = .5 * (a_low + a_high)
        if np.sign(func(m)) != np.sign(func(a_high)):
            a_low = m
        else:
            a_high = m
    return .5 * (a_low + a_high)


def dogleg_step(grad_x, hess_x, trust_radius):
    p_u = -(grad_x.dot(grad_x))/(grad_x.dot(hess_x).dot(grad_x))*grad_x
    p_fs = -inv(hess_x).dot(grad_x)
    if norm(p_u, ord=2) >= trust_radius:
        return trust_radius*normalize(p_u)
    elif norm(p_fs, ord=2) <= trust_radius:
        return p_fs
    else:
        m = tau_min(p_u, p_fs, trust_radius)
        tau = bisection(1, 2, m)
        return p_u + (tau - 1)*(p_fs - p_u)


def make_grad_hess(funkshun, *args):
    g = funkshun(*args)

    vars = list(ordered(g.free_symbols))
    gradient = lambda func, frees: Matrix([func]).jacobian(frees)

    gradi = lambdify(vars, gradient(g, vars))
    hessi = lambdify(vars, h(g, vars))

    return lambda ex, why: gradi(ex, why).flatten(), hessi


f = lambda x1, x2: 100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2
grad_f, hess_f = make_grad_hess(f, x, y)

x_start = np.array([[-1.2, 1], [2.8, 4]])

solutions = trust_region(x_start, f, quad_model, grad_f, hess_f,
                         dogleg_step, max_trust=300., init_trust=1.)

for sol in solutions:
    print(f"Starting point: {sol[0]},\n"
          f"Minimum: {sol[-1]},\n"
          f"First 5:\n{sol[:5]}\n"
          f"Last 4:\n{sol[-4:]}\n"
          f"Total Iterations: {sol.shape[0]}\n")

# Remove the exit statement below to generate the plots relevant to the
# optimization above.
exit(0)

# Nothing but plots and testing beyond this point.
# ------------------------------------------------------------------------


# Test points with diagnostic info.
x_init = np.zeros(shape=(6, 2)).astype(dtype=np.float64)
x_init[0] = [-1.2, 1.]
x_init[1] = [2.8, 4.]
x_init[2] = [1.2, 1.2]
x_init[3] = [64., 89.]
x_init[4] = [-90., -100.]
x_init[5] = [200., -250.]

for i in range(50, 301, 50):
    equis = trust_region(x_init, f, quad_model,
                         grad_f, hess_f,
                         dogleg_step, max_trust=i,
                         init_trust=1.)
    print(f"Max trust radius: {i}")
    for sol in equis:
        print(f"Starting point: {sol[0]},\n"
              f"Minimum: {sol[-1]},\n"
              f"Total Iterations: {sol.shape[0]}\n"
              f"First 5:\n{sol[:5]}\n"
              f"Last 4:\n{sol[-4:]}")


# Rate of convergence computation.
minimum = [1., 1.]
for q in equis:
    w = q - minimum
    w = np.linalg.norm(w, ord=2, axis=1)
    coeff = np.polyfit(np.log(w[:-1]), np.log(w[1:]), 1)
    print(f"Rate of convergence; x0 = {q[0]}: {coeff[0]}")


# Objective function vs x_k graph generation.
for k, q in enumerate(equis[:2]):
    fig, ax = plt.subplots(figsize=(12, 8))

    ax.plot(np.log10(f(*q.T)), '-k',
            label=fr"$\vec{{x}}_0 = ({q[0,0]}, {q[0,1]})$")

    ax.grid()
    ax.set_xlabel(r"$k$", size=25)
    ax.set_ylabel(r"$\log_{10}\left(f(\vec{x}_k)\right)$", size=25)
    ax.tick_params(direction='in', width=2, length=8, labelsize=25)
    ax.set_title("Dogleg method, $\widehat{\Delta} = 300$", size=25)
    ax.legend(loc='upper right', fontsize=25);
    ax.set_xticks([i for i in range(0, q.shape[0], 5)])

    fig.savefig(f"HW3;Objective{k}")


# 3D matplotlib plot generation.
X = np.linspace(-2, 2, 5 * 101)
Y = np.linspace(-.1, 2, 5 * 101)
X, Y = np.meshgrid(X, Y)

Z = f(X, Y)
Z[Z > 400] = 400
fig, ax = plt.subplots(1, 1, figsize=(18, 14))

ax = plt.axes(projection='3d')
ax.plot(*q.T, f(*q.T), '-r', lw=4,
        label=f"Optimization Path\nDogleg Method\nSteps: {q.shape[0]}")
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', alpha=.5)

ax.text(*q[0], f(*q[0]) + 1,
        f"Starting point: $({q[0, 0]}, {q[0, 1]}, {f(*q[0]):3.2f})$",
        size=25, ha="right", va="bottom", color="red")
ax.text(*q[-1], f(*q[-1]),
        f"Minimum: $({q[-1, 0]:0.1f}, {q[-1, 1]:0.1f}, {f(*q[-1]):0.1f})$",
        size=25, ha="center", va="bottom", color="red")

ax.set_xlabel("$x$", size=30, labelpad=20)
ax.set_xticks([i - 2.0 for i in range(5)])
ax.set_ylabel("$y$", size=30, labelpad=20)
ax.set_yticks([.5*i for i in range(5)])
ax.set_zlabel("$f(x,y)$", size=30, labelpad=25)
ax.set_zticks([i*100 for i in range(5)])
ax.zaxis.set_rotate_label(False)

ax.tick_params(direction='in', width=2, length=8, labelsize=25)
ax.view_init(45, 230+60)
ax.legend(fontsize=20, loc='lower left')

ax.set_title("Rosenbrock's Function on "
             fr"$[{X.min()},{X.max()}]\times [{Y.min()},{Y.max()}]$", size=30);

fig.savefig(f"HW3;HardStart")


q = equis[1]

X = np.linspace(0, 3, 5 * 101)
Y = np.linspace(0, 6, 5 * 101)
X, Y = np.meshgrid(X, Y)

Z = f(X, Y)
Z[Z > 3_000] = 3_000
fig, ax = plt.subplots(1, 1, figsize=(18, 14))

ax = plt.axes(projection='3d')
ax.plot(*q.T, f(*q.T), '-r', lw=4,
        label=f"Optimization Path\nDogleg Method\nSteps: {q.shape[0]}")
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', alpha=.5)

ax.text(*q[0], f(*q[0]) + 1,
        f"Starting point: $({q[0, 0]}, {q[0, 1]}, {f(*q[0]):3.2f})$",
        size=25, ha="center", va="bottom", color="red")
ax.text(*q[-1], f(*q[-1]),
        f"Minimum: $({q[-1, 0]:0.1f}, {q[-1, 1]:0.1f}, {f(*q[-1]):0.1f})$",
        size=25, ha="right", va="top", color="red")

ax.set_xlabel("$x$", size=30, labelpad=20)
ax.set_ylabel("$y$", size=30, labelpad=20)
ax.set_zlabel("$f(x,y)$", size=30, labelpad=25)
ax.zaxis.set_rotate_label(False)
ax.set_zticks([i*1000 for i in range(4)])

ax.tick_params(direction='in', width=2, length=8, labelsize=25)
ax.view_init(45, 230)
ax.legend(fontsize=20, loc='lower left')

ax.set_title("Rosenbrock's Function on "
             fr"$[{X.min()},{X.max()}]\times [{Y.min()},{Y.max()}]$", size=30);

fig.savefig(f"HW3;EasyStart")

