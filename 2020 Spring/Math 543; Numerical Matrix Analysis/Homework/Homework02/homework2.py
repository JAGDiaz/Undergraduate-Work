#! /usr/bin/python3

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse 
import matplotlib.axes as AXES
plt.rcParams['text.usetex'] = True
plt.rcParams['savefig.format'] = 'jpg'
plt.rcParams['figure.figsize'] = (12, 12)

a = np.array([[3,0], [0, -2]])

b = np.array([[2, 0], [0, 3]])

c = np.array([[0, 2], [0, 0], [0, 0]])

d = np.array([[1,1], [0, 0]])

e = np.array([[1, 1], [1, 1]])

f = np.array([[1, 2], [0, 2]])

ra = np.array([a, b, d, e, f])

print("The SVD of\n", c, "is:\n")
u, s, vh = np.linalg.svd(c)
print(u, "\n*", s, "\n*", vh)
print("\n")

for i in ra:
	print("The SVD of\n", i, "is:\n")
	u, s, vh = np.linalg.svd(i, full_matrices=True)
	print(u, "\n*", s, "\n*", vh)
	print("\n")
	vh = np.transpose(vh)
	
	fig, ax = plt.subplots(1,1)

	if(s[0] >= 1e-6):
		a1 = ax.arrow(0,0, s[0]*u[0, 0], s[0]*u[1, 0], shape='full', width=.05, color='y', 
					length_includes_head=True, label=r"$\sigma_1\vec{u}_1$")
	if(s[1] >= 1e-6):
		a2 = ax.arrow(0,0, s[1]*u[0, 1], s[1]*u[1, 1], shape='full', width=.05, color='b', 
					length_includes_head=True, label=r"$\sigma_2\vec{u}_2$")

	a3 = ax.arrow(0,0, vh[0, 0], vh[1, 0], shape='full', width=.05, color='r', 
				length_includes_head=True, label=r"$\vec{v}_1$")
	a4 = ax.arrow(0,0, vh[0, 1], vh[1, 1], shape='full', width=.05, color='g', 
				length_includes_head=True, label=r"$\vec{v}_2$")
	ax.grid()

	ellipse = Ellipse((0,0), width=2*s[0], height=2*s[1], angle=(180/np.pi)*np.arctan2(u[1,0],u[0,0]), fc='none', ec='cyan')
	circle = Ellipse((0,0), width=2, height=2, fc='none', ec='purple')
	ax.add_patch(ellipse)
	ax.add_patch(circle)
	ax.set_xlim(-3, 3)
	ax.set_ylim(-3, 3)
	ax.set_title("Unitary Matrices' column vectors", size=20)
	ax.legend(loc='lower right', handles=[a1, a2, a3, a4], fontsize=20)
	ax.set_xlabel("$x$", size = 20)
	ax.set_ylabel("$y$", size = 20)
	fig.tight_layout()
#	fig.savefig("H2UnitaryVecs%03d.jpg" % (i+1))
	plt.show()




	
