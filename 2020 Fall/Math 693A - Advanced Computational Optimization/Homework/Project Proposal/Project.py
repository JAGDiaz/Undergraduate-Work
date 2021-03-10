import numpy as np
from interval import interval
import matplotlib.pyplot as plt


def size(region):
    ex, why = region
    return max(ex[0].sup-ex[0].inf, why[0].sup-why[0].inf)


def mid(region):
    ex, why = region
    mids = ex.midpoint[0], why.midpoint[0]
    return mids[0].inf, mids[1].inf


def split(region):
    ex, why = region
    x_mid, y_mid = ex.midpoint[0].inf, why.midpoint[0].inf
    extrema = *ex.extrema, *why.extrema
    if extrema[1].inf - extrema[0].inf > extrema[3].inf - extrema[2].inf:
        return (interval([extrema[0].inf, x_mid]), interval([extrema[2].inf, extrema[3].inf])), \
               (interval([x_mid, extrema[1].inf]), interval([extrema[2].inf, extrema[3].inf]))
    else:
        return (interval([extrema[0].inf, extrema[1].inf]), interval([extrema[2].inf, y_mid])), \
               (interval([extrema[0].inf, extrema[1].inf]), interval([y_mid, extrema[3].inf]))


def low_bound(func, region):
    ex, why = region
    f_int = func(ex, why)
    print(f"f_int: {f_int}")
    return f_int[0].inf


int1 = interval([-25, 25])
int2 = interval([-50, 50])
reg = (int1, int2)

rosenbrock = lambda x1, x2: 100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


states = [reg]
possibles = []
S = rosenbrock(*mid(reg))
print(low_bound(rosenbrock, reg))

while len(states) > 0:
    reg = states.pop()
    print(f"reg: {reg}")
    if size(reg) < 1 and low_bound(rosenbrock, reg) < S:
        S = rosenbrock(*mid(reg))
        possibles.append(mid(reg))
    else:
        reg1, reg2 = split(reg)
        print(f"reg1: {reg1}, reg2: {reg2}")
        low_1, low_2 = low_bound(rosenbrock, reg1), low_bound(rosenbrock, reg2)
        print(f"low_1: {low_1}, low_2: {low_2}")
        if low_1 < S:
            states.insert(0, reg1)
        elif low_2 < S:
            states.insert(0, reg2)

print(S)
print(possibles)

