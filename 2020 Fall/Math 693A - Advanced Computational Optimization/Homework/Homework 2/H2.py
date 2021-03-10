"""
Author: Joseph Diaz
Course: Math 693-A
Homework 2

This program optimizes the Rosenbrock function from a pair of
given starting points on the manifold using the Steepest Descent
and Newton Methods. This is an augmentation on Homework 1 that
incorporates exact step length selection.
"""
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams['text.usetex'] = True
plt.rcParams['savefig.format'] = 'jpg'


def f(ex):
    return 100 * (ex[1] - ex[0] ** 2) ** 2 + (1 - ex[0]) ** 2


def normalize(v):
    return v / np.linalg.norm(v, ord=2)


def get_grad(func, ex, dh=1e-8):
    """
    This function computes the numerical gradient of a function of
    multiple variables using a difference quotient schema.
    :param func:
    :param ex:
    :param dh:
    :return:
    """
    x_mat = np.repeat([ex], repeats=ex.size, axis=0)
    off = dh * np.eye(ex.size)
    x_minus = x_mat - off
    x_plus = x_mat + off
    backward_diff = np.fromiter(map(func, x_minus), dtype=ex.dtype)
    forward_diff = np.fromiter(map(func, x_plus), dtype=ex.dtype)
    return (forward_diff - backward_diff) / (2 * dh)


def get_hessian(func, ex, grad_finder, dh=1e-8):
    """
    This function computes the Jacobian of the gradient of a function,
    at a given point; which is equivalent to the Hessian of the function
    at that point.
    :param grad_finder:
    Callable function that computes the Gradient at a given point.
    :param func:
    Function whose Gradient and Hessian we want.
    :param ex:
    The point for which we want the Gradient and Hessian.
    :param dh:
    Step size on each variable.
    :return:
    Hessian Matrix for ex.
    """
    grad = grad_finder(func, ex, dh)
    dxj = np.where(grad < dh, dh, grad * dh)
    x_plus = np.repeat([ex], repeats=ex.size, axis=0) + dxj * np.eye(ex.size)
    hessian = np.empty(shape=(ex.size, ex.size), dtype=ex.dtype)
    for j in range(ex.size):
        hessian[j] = (grad_finder(func, x_plus[j], dh) - grad) / dxj[j]
    return hessian


def phi_maker(ex, pea):
    """
    This function returns a lambda function with the
    given parameters. It allows us to more easily treat
    phi as a function of a single variable.
    :param ex:
    Current x value in optimization.
    :param pea:
    Current search direction in optimization.
    :return:
    Lambda function of f at ex with pea in terms of alpha.
    """
    return lambda t: f(ex + t * pea)


def prime_maker(func, delta=1e-8):
    """
    This function return a lambda function of the
    numerically approximated derivative of the given
    function using a finite difference schema.
    :param func:
    The function whose derivative we want to approximate.
    :param delta:
    The small change in the independent variable we're using
    to approximate the derivative.
    :return:
    Lambda function that approximates the derivative of func.
    """
    return lambda t: (func(t + delta) - func(t - delta)) / (2 * delta)


def hermite_interpolate(a_low, a_high, a_k, func, d_func, vep_1=1e-8, vep_2=1e-8):
    """
    This function computes the minimum of the hermite cubic interpolant
    of func, with d_func as derivative, in the interval [a_low, a_high]
    :param a_low: 
    :param a_high: 
    :param a_k:
    Step-size from previous iteration of optimization.
    :param func:
    The function we want to interpolate.
    :param d_func:
    Approximation of the derivative of the function we want to interpolate.
    :param vep_1: 
    :param vep_2:
    Safeguard arguments, to ensure that step sizes do not become too small.
    :return: 
    """
    phi_prev, phi_curr = func(a_low), func(a_high)
    phi_p_prev, phi_p_curr = d_func(a_low), d_func(a_high)
    d_1 = phi_p_prev + phi_p_curr - 3 * (phi_prev - phi_curr) / (a_low - a_high)
    d_2 = np.sign(a_high - a_low) * np.sqrt(d_1 ** 2 - phi_p_prev * phi_p_curr)
    a_new = a_high - (a_high - a_low) * (phi_p_curr + d_2 - d_1) / (phi_p_curr - phi_p_prev + 2 * d_2)
    if np.abs(a_new - a_k) < vep_1 or np.abs(a_new) < vep_2:
        print("Safety!")
        a_new = a_k / 2
    return a_new


def zoom(a_low, a_high, a_k, func, d_func, c_1=1e-4, c_2=.9):
    """
    This function 'zooms in on' an interval in which we try to
    find minimizers of the function func.
    :param a_low:
    :param a_high:
    a_low and a_high are the bounds of the interval we want to
    investigate.
    :param a_k:
    The step length from the previous iteration of the overall code.
    :param func:
    The func we want to find a minimizer for.
    :param d_func:
    The numerically computed derivative of func.
    :param c_1:
    :param c_2:
    c_1 and c_2 are parameters for checking the Strong Wolfe conditions.
    :return:
    Minimizer in [a_low, a_high]
    """
    while True:
        a_j = hermite_interpolate(a_low, a_high, a_k, func, d_func)
        phi_j = func(a_j)
        if phi_j > func(0) + c_1 * a_j * d_func(0) or func(a_j) >= func(a_low):
            a_high = a_j
        else:
            phi_j = d_func(a_j)
            if np.abs(phi_j) <= -c_2 * d_func(0):
                return a_j
            if phi_j * (a_high - a_low) >= 0:
                a_high = a_low
            a_low = a_j


def LS(func, d_func, a_k, a_i=.5, a_max=1, c_1=1e-4, c_2=.9):
    """
    This function attempts to find an ideal step length that
    satisfies the Strong Wolfe conditions.
    :param func:
    The function we want to minimize
    :param d_func:
    The numerically approximated derivative of func.
    :param a_k:
    The step length of the previous iteration of our optiization schema.
    :param a_i:
    The intial guess we use to begin the algorithm.
    :param a_max:
    The largest step length we want to consider.
    :param c_1:
    :param c_2:
    c_1 and c_2 are parameters for checking the Strong Wolfe conditions.
    :return:
    A step length that satisfies the Strong Wolfe conditions.
    """
    a_prev = 0
    while True:
        phi_i = func(a_i)
        if phi_i > func(0) + c_1 * a_i * d_func(0) or (phi_i >= func(a_prev)):
            return zoom(a_prev, a_i, a_k, func, d_func)

        phi_i = d_func(a_i)
        if np.abs(phi_i) <= -c_2 * d_func(0):
            return a_i

        if phi_i >= 0:
            return zoom(a_i, a_prev, a_k, func, d_func)

        a_prev = a_i
        a_i = np.random.uniform(a_prev, a_max)
        # a_i = zoom(a_prev, a_i, func, d_func, c_1, c_2)


dx = 1e-8
n = int(3e4)
tolerance = 1e-8

x_steepest = [None, None]
x_newton = [None, None]
x_nought = [[1.2, 1.2], [-1.2, 1]]

np.random.seed(37 * 18 - 1)

# Steepest Descent Method for p
for j, x0 in enumerate(x_nought):
    xs = np.zeros(shape=(n, 2), dtype=np.float64)
    x = np.array(x0)
    xs[0] = x
    begin = datetime.now()

    nabla_f = get_grad(f, x, dx)
    p = -normalize(nabla_f)
    a_func = phi_maker(x, p)
    a_func_prime = prime_maker(a_func)
    a = LS(a_func, a_func_prime, 1e-4)
    prev_direction = np.dot(nabla_f, p)

    i = 1
    while np.abs(f(x)) > tolerance and np.linalg.norm(nabla_f, ord=2) > tolerance and i < n:
        x += a * p
        xs[i] = x
        nabla_f = get_grad(f, x, dx)
        p = -normalize(nabla_f)
        a_func = phi_maker(x, p)
        a_func_prime = prime_maker(a_func)
        a = LS(a_func, a_func_prime, a, a * prev_direction / np.dot(nabla_f, p))
        prev_direction = np.dot(nabla_f, p)

        i += 1

    print(f"Steepest Descent Method; starting at x0 = {x0}.")
    print(f"x_{i - 1}: {xs[i - 1]}, f at that point: {f(xs[i - 1])}")
    x_steepest[j] = np.copy(xs[:i])
    del xs
    print(f"First 6 values of x: \n{x_steepest[j][:6]}")
    print(f"Last 6 values of x: \n{x_steepest[j][-6:]}\n")
    print(f"That took: {datetime.now() - begin}\n")

# Newton's Method for p.
for j, x0 in enumerate(x_nought):
    xs = np.zeros(shape=(n, 2), dtype=np.float64)
    x = np.array(x0)
    xs[0] = x

    begin = datetime.now()

    nabla_f = get_grad(f, x, dx)
    hess = get_hessian(f, x, get_grad, dx)
    p = -np.dot(np.linalg.inv(hess), nabla_f)
    a_func = phi_maker(x, p)
    a_func_prime = prime_maker(a_func)
    prev_direction = np.dot(nabla_f, p)
    a = 1

    i = 1
    while np.abs(f(x)) > tolerance and np.linalg.norm(nabla_f, ord=2) > tolerance and i < n:
        x += a * p
        xs[i] = x
        nabla_f = get_grad(f, x, dx)
        hess = get_hessian(f, x, get_grad, dx)
        p = -np.dot(np.linalg.inv(hess), nabla_f)
        a_func = phi_maker(x, p)
        a_func_prime = prime_maker(a_func)
        a = LS(a_func, a_func_prime, a, a)
        prev_direction = np.dot(nabla_f, p)
        i += 1

    print(f"Newton's Method; starting at x0 = {x0}")
    print(f"x_{i - 1}: {xs[i - 1]}, f at that point: {f(xs[i - 1])}")
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
print(f"Rate of convergence, x0 = (-1.2, 1): {ps2[0]:5.6f}\n\n")

print("Newton's Method: ")
pn1 = np.polyfit(np.log10(x_n1[:-1]), np.log10(x_n1[1:]), 1)
print(f"Rate of convergence, x0 = (1.2, 1.2): {pn1[0]:5.6f}")
pn2 = np.polyfit(np.log10(x_n2[:-1]), np.log10(x_n2[1:]), 1)
print(f"Rate of convergence, x0 = (-1.2, 1): {pn2[0]:5.6f}")

# Remove the exit statement below to generate the plots relevant to the
# optimization above.
exit(0)


# Nothing but plotting below this point.
#-------------------------------------------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(12, 10))

ax.plot(np.log10(f(sols1.T)), '-k', label=r"$\vec{x}_0 = (1.2, 1.2)$")
ax.plot(np.log10(f(sols2.T)), '-r', label=r"$\vec{x}_0 = (-1.2, 1)$")
ax.set_xlabel(r"$k$", size=25)
ax.set_ylabel(r"$\log_{10}\left(f(\vec{x}_k)\right)$", size=25)
ax.tick_params(direction='in', width=2, length=8, labelsize=25)
ax.legend(loc='upper right', fontsize=25)
ax.set_title("Steepest Descent Algorithm", size=25)
ax.grid()

fig.savefig("HW2SDObjective")

fig, ax = plt.subplots(figsize=(12, 10))

ax.plot(np.log10(f(soln1.T)), '-ok', label=r"$\vec{x}_0 = (1.2, 1.2)$")
ax.plot(np.log10(f(soln2.T)), '-or', label=r"$\vec{x}_0 = (1.2, -1)$")
ax.set_xlabel(r"$k$", size=25)
ax.set_ylabel(r"$\log_{10}\left(f(\vec{x}_k)\right)$", size=25)
ax.tick_params(direction='in', width=2, length=8, labelsize=25)
ax.legend(loc='lower left', fontsize=25)
ax.set_title("Newton's Method Algorithm", size=25)
ax.grid()

fig.savefig("HW2NMObjective")

# Contour plot of Objective function below.
# 1
aleph = 1.3

c = .9
d = 1.3
beta = d + .2
X = np.linspace(c, d, 5 * 101)
Y = np.linspace(c, d, 5 * 101)
X, Y = np.meshgrid(X, Y)

Z = f((X, Y))
Z[Z > 10] = 10

fig, ax = plt.subplots(1, 1, figsize=(18, 14))

ax = plt.axes(projection='3d')
ax.plot(*sols1.T, f(sols1.T), '-r', lw=4, label="Optimization Path\nSteepest Descent\n"
                                                f"Steps: {sols1.shape[0]}")
ax.scatter([1.2, 1], [1.2, 1], [f((1.2, 1.2)), f((1, 1))], '*r', lw=10)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', alpha=.5)
ax.text(1.2, 1.2, f((1.2, 1.2)) + 1,
        f"Starting point: $({sols1[0, 0]}, {sols1[0, 1]}, {f(sols1[0]):3.2f})$",
        size=25, ha="center", va="top", color="red")
ax.text(1, 1, f((1, 1)) + 1,
        f"Minimum: $(1, 1, {f((1, 1))})$",
        size=25, ha="left", va="top", color="red")
ax.set_xlabel("$x$", size=30)
ax.set_ylabel("$y$", size=30)
ax.set_zlabel("$f(x,y)$", size=30)
ax.set_zlim(0, 10)
ax.tick_params(direction='in', width=2, length=8, labelsize=25)
ax.view_init(25, 235)
ax.legend(fontsize=25)

fig.suptitle(fr"Rosenbrock's Function on $[{c},{d}]\times [{c},{d}]$", size=30)

fig.savefig("HW2SD1Surface")

# 2
c = .25
d = 1.2
X = np.linspace(-d, d, 5 * 101)
Y = np.linspace(-c, d, 5 * 101)
X, Y = np.meshgrid(X, Y)

Z = f((X, Y))
Z[Z > 30] = 30

fig, ax = plt.subplots(1, 1, figsize=(18, 14))

ax = plt.axes(projection='3d')
ax.plot(*sols2.T, f(sols2.T), '-r', lw=4, label="Optimization Path\nSteepest Descent\n"
                                                f"Steps: {sols2.shape[0]}")
ax.scatter([-1.2, 1], [1, 1], [f((-1.2, 1)), f((1, 1))], '*r', lw=10)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', alpha=.5)
ax.text(-1.2, 1, f((-1.2, 1)) - 1,
        f"Starting point: $({sols2[0, 0]}, {sols2[0, 1]}, {f(sols2[0]):3.1f})$",
        size=25, ha="left", va="top", color="red", zorder=1)
ax.text(1, 1, f((1, 1)) - 2,
        f"Minimum: $(1, 1, {f((1, 1))})$",
        size=25, ha="left", va="bottom",
        color="red", zorder=1)
ax.set_xlabel("$x$", size=25)
ax.set_ylabel("$y$", size=25)
ax.set_zlabel("$f(x,y)$", size=25)
ax.set_zlim(0, 30)
ax.tick_params(direction='in', width=2, length=8, labelsize=25)
ax.legend(fontsize=25)
ax.view_init(40, 100)

fig.suptitle(fr"Rosenbrock's Function, $[{-d},{d}]\times [{-c},{d}]$",
             size=30)

fig.savefig("HW2SD2Surface")

# 3
c = .9
d = 1.3
X = np.linspace(c, d, 5 * 101)
Y = np.linspace(c, d + .15, 5 * 101)
X, Y = np.meshgrid(X, Y)

Z = f((X, Y))
Z[Z > 10] = 10

fig, ax = plt.subplots(1, 1, figsize=(18, 14))

ax = plt.axes(projection='3d')
ax.plot(*soln1.T, f(soln1.T), '-or', lw=2, label="Optimization Path\nNewton's Method\n"
                                                 f"Steps: {soln1.shape[0]}")
ax.scatter([1.2, 1], [1.2, 1], [f((1.2, 1.2)), f((1, 1))], '*r', lw=10)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', alpha=.5)
ax.text(1.2, 1.2, f((1.2, 1.2)) + 1,
        f"Starting point: $({soln1[0, 0]}, {soln1[0, 1]}, {f(soln1[0]):3.2f})$",
        size=25, ha="right", va="top", color="red")
ax.text(1, 1, f((1, 1)) - 1,
        f"Minimum: $(1, 1, {f((1, 1))})$",
        size=25, ha="left", va="bottom", color="red")
ax.set_xlabel("$x$", size=30)
ax.set_ylabel("$y$", size=30)
ax.set_zlabel("$f(x,y)$", size=30)
ax.set_zlim(0, 10)
ax.tick_params(direction='in', width=2, length=8, labelsize=25)
ax.view_init(25, 235)
ax.legend(fontsize=25)

fig.suptitle(fr"Rosenbrock's Function, $[{c},{d}]\times [{c},{d + .15}]$",
             size=30)

fig.savefig("HW2NM1Surface")

# 4
beta = 2.5
c = 1.5
d = -4
X = np.linspace(-c, c, 5 * 101)
Y = np.linspace(d, beta, 5 * 101)
X, Y = np.meshgrid(X, Y)

Z = f((X, Y))

fig, ax = plt.subplots(1, 1, figsize=(18, 14))

ax = plt.axes(projection='3d')
ax.plot(*soln2.T, f(soln2.T), '-or', lw=3, label="Optimization Path\nNewton's Method\n"
                                                 f"Steps: {soln2.shape[0]}")
ax.scatter([-1.2, 1], [1, 1], [f((-1.2, 1)), f((1, 1))], '*r', lw=4)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', alpha=.5)
ax.text(-1.2, 1, f((-1.2, 1)) - 1,
        f"Starting point: $({sols2[0, 0]}, {sols2[0, 1]}, {f(sols2[0]):3.1f})$",
        size=25, ha="center", va="top", color="red", zorder=1)
ax.text(1, 1, f((1, 1)) - 2,
        f"Minimum: $(1, 1, {f((1, 1))})$",
        size=25, ha="left", va="bottom", color="red", zorder=1)
ax.set_xlabel("$x$", size=25)
ax.set_ylabel("$y$", size=25)
ax.set_zlabel("$f(x,y)$", size=25)
ax.tick_params(direction='in', width=2, length=8, labelsize=25)
ax.legend(fontsize=25)
ax.view_init(40, 145)

fig.suptitle(fr"Rosenbrock's Function, $[{-c:2.1f},{c:2.1f}]\times [{d:2.1f},{beta:2.1f}]$",
             size=30)

fig.savefig("HW2NM2Surface")
