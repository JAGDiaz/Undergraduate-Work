import numpy as np
from sympy import ordered, Matrix
from sympy import hessian as h
from sympy.abc import x, y
from sympy.utilities.lambdify import lambdify
from numpy.linalg import norm
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['savefig.format'] = 'jpg'


def make_grad_hess(funkshun, *args):
    """
    This function uses the Sympy package to symbolically
    generate a gradient and hessian function for a given
    function.
    :param funkshun:
    The objective function we wish to generate a gradient
    and hessian for.
    :param args:
    Symbolic arguments for the funkshun.
    :return:
    lambda functions that call the symbolic gradient and
    hessian.
    """
    g = funkshun(*args)

    vars = list(ordered(g.free_symbols))
    gradient = lambda func, frees: Matrix([func]).jacobian(frees)

    gradi = lambdify(vars, gradient(g, vars))
    hessi = lambdify(vars, h(g, vars))

    return lambda ex: gradi(*ex).flatten(), lambda ex: hessi(*ex)


def rosenbrock_2Nd(ex, order=0, func=None, func_g=None, func_h=None):
    """
    This function computes a 2N dimensional sum of Rosenbrocks and can return
    an initial condition for an 18 dimensional Rosenbrock.
    :param ex:
    The 2N vector to evaluate func at.
    :param order:
    The order of the evaluation of func.
    :param func:
    A 2D Rosenbrock function, to be summed N times.
    :param func_g:
    A gradient function for the 2D Rosenbrock.
    :param func_h:
    A hessian function for the 2D Rosenbrock.
    :return:
    Numpy arrays of variable shape, scalars, or nothing; depending
    on the order parameter.
    """
    if order == -1:
        xN = np.array([1, 1])
        x0easy = np.array([1.2, 1.2])
        x0e2 = (xN + x0easy) * .5
        x0e3 = (xN + x0e2) * .5
        x0e4 = (xN + x0e3) * .5

        x0hard = np.array([-1.2, 1])
        x0h2 = (xN + x0hard) * .5
        x0h3 = (xN + x0h2) * .5
        x0h4 = (xN + x0h3) * .5
        x0h5 = 2 * x0hard

        return np.concatenate((x0easy, x0e2, x0e3, x0e4, x0hard, x0h2, x0h3, x0h4, x0h5))

    elif order == 0:
        return np.sum(func(ex[::2], ex[1::2]))

    elif order == 1:
        points = zip(ex[::2], ex[1::2])
        grads = map(func_g, points)
        return np.concatenate(tuple(grads))

    elif order == 2:
        points = np.reshape(ex, newshape=(ex.size // 2, 2))
        ceros = np.zeros((2, 2))
        hess = [[func_h(points[i]) if i == j else ceros for i in range(ex.size // 2)] for j in range(ex.size // 2)]
        return np.block(hess)

    else:
        print(f"Can\'t find a derivative of order {order}.\n")


def rosenbrock_caller(func, func_g, func_h):
    return lambda t, o: rosenbrock_2Nd(t, o, func, func_g, func_h)


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
    k = 0
    while funk(ex + alpha * pea, 0) > funk(ex, 0) + cee * alpha * np.dot(pea, grad):
        alpha *= rho
        k += 1
    return alpha, k


def newton(x0, func, epsilon=1e-8, n=1_000):
    """
    This function optimizes an objective function from a
    starting point using Newton's Method.
    :param x0:
    The starting point.
    :param func:
    A special function that can evaluate the objective
    function and it's derivatives at a given x.
    :param epsilon:
    The tolerance of our optimization scheme.
    :param n:
    Optional parameter for the size of list to
    store partial solutions per iteration.
    :return:
    Numpy arrays containing the partial solutions,
    step-sizes and step-size inner iterations.
    """
    x_array = [None] * n
    alpha_array = [None] * n
    k = 0
    k_inner = 0
    x_k = np.copy(x0).astype(dtype=np.float64)

    grad_k = func(x_k, 1)
    hess_k = func(x_k, 2)
    p_k = -np.linalg.inv(hess_k).dot(grad_k)
    alpha_k, temp = get_alpha(grad_k, func, x_k, p_k)
    k_inner += temp

    while norm(grad_k, ord=2) > epsilon:
        x_k += alpha_k * p_k

        grad_k = func(x_k, 1)
        hess_k = func(x_k, 2)
        p_k = -np.linalg.inv(hess_k).dot(grad_k)
        alpha_k, temp = get_alpha(grad_k, func, x_k, p_k)
        k_inner += temp
        x_array[k] = np.copy(x_k)
        alpha_array[k] = alpha_k
        k += 1

    return np.array(x_array[:k]), np.array(alpha_array[:k]), k_inner


def bfgs(x0, h0, func, epsilon=1e-8, n=1_000):
    """
    This function implements the BFGS method of optimization
    to optimize an objective function.
    :param x0:
    The starting point of our optimization.
    :param h0:
    Our initial guess for the Quasi-Newton matrix.
    :param func:
    A special function that can evaluate the objective
    function and it's derivatives at a given x.
    :param epsilon:
    The tolerance of our optimization.
    :param n:
    Optional parameter for the size of list to
    store partial solutions per iteration.
    :return:
    Numpy arrays containing the partial solutions, Quasi-Newton
    matrices, search directions, step-sizes, and step-size inner
    iterations.
    """
    x_array = [None] * n
    alpha_array = [None] * n
    bk_array = [None] * n
    pk_array = [None] * n
    k = 0
    k_inner = 0
    x_prev = np.copy(x0)
    h_k = np.copy(h0)
    identity = np.eye(h0.shape[0])
    grad_prev = func(x_prev, 1)
    while norm(grad_prev, ord=2) > epsilon:
        p_k = -h_k @ grad_prev

        alpha_k, temp = get_alpha(grad_prev, func, x_prev, p_k)
        k_inner += temp

        x_next = x_prev + alpha_k * p_k
        s_k = x_next - x_prev
        grad_next = func(x_next, 1)
        y_k = grad_next - grad_prev
        rho_k = 1 / y_k.dot(s_k)
        sy_outer = np.outer(s_k, y_k)

        h_k = (identity - rho_k * sy_outer) @ h_k @ (identity - rho_k * sy_outer.T) + \
              rho_k * np.outer(s_k, s_k)

        x_prev = x_next
        grad_prev = grad_next

        x_array[k] = np.copy(x_prev)
        alpha_array[k] = alpha_k
        bk_array[k] = np.copy(h_k)
        pk_array[k] = np.copy(p_k)

        k += 1

    return np.array(x_array[:k]), np.array(alpha_array[:k]),\
           np.array(bk_array[:k]), np.array(pk_array[:k]), k_inner


f = lambda x1, x2: 100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2

f_grad, f_hess = make_grad_hess(f, x, y)

bfgs_func = rosenbrock_caller(f, f_grad, f_hess)

x = rosenbrock_2Nd(1, order=-1)

h_nought = np.eye(x.shape[0])

print("BFGS")

x_ra, alpha_ra, bk_ra, pk_ra, inner_iters = bfgs(x, h_nought, bfgs_func)


hess_xstar = bfgs_func(x_ra[-1], 2)
bk_diff = bk_ra - hess_xstar
bk_diffp_k = np.array(list(map(np.matmul, bk_diff, pk_ra)))

QN = norm(bk_diffp_k, ord=2, axis=1)/norm(pk_ra, ord=2, axis=1)

for k, qn in enumerate(QN):
    print(f"{k+1} & {np.round(qn, decimals=4)} \\\\\n\\hline")

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(np.arange(QN.shape[0]) + 1, np.log10(QN), '-k')
ax.set_xlabel("$k$", size=20)
ax.set_ylabel(r"$\log_{10}\left(\frac{||(B_k - \nabla^2 f(x^*))p_k||}{||p_k||}\right)$",
              size=20)
ax.grid()
ax.set_title("Quasi-Newton Convergence", size=30)
fig.savefig("bkconvergence")

plt.close(fig)

print("Newton")

xn_ra, alphan_ra, innern_iters = newton(x, bfgs_func)
