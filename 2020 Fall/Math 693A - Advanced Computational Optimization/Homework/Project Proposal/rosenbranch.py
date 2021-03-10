import numpy as np
from interval import interval


rosenbrock = lambda x1, x2: 100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


I1 = interval([0, 11])
I2 = interval([-1, 2])

print(rosenbrock(I1, I2))
print(1 - I2)

I3 = interval([-1, 2], [2, 6])

print(I3[0].inf)
