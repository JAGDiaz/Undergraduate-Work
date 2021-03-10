import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['savefig.format'] = 'png'

phi = lambda ex: np.fromiter(map(lambda p: 1 if 0 <= p < 1 else 0, ex), dtype=np.float64)

psi = lambda ex: phi(2*ex) - phi(2*ex - 1)

psimn = lambda em, en, ex: (2.**(.5*em))*psi((2.**em)*ex - en)

t = np.linspace(-.5, 1.5, 1001)


fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax = ax.flatten()

ax[0].plot(t, phi(t), 'ob', label=r"$\varphi(x)$", ms=.5)
ax[0].plot(t, phi(t), '--k', alpha=.5, lw=.5)
ax[0].set_xlabel("$x$", size=25)
ax[0].set_ylabel(r"$\varphi(x)$", size=25)
ax[0].grid()
ax[0].tick_params(direction='in', labelsize=20)
ax[0].set_xlim(t.min(), t.max())


ax[1].plot(t, psi(t), 'or', label=r"$\psi(x)$", ms=.5)
ax[1].plot(t, psi(t), '--k', alpha=.5, lw=.5)

ax[1].set_xlabel("$x$", size=25)
ax[1].set_ylabel("$\psi(x)$", size=25)
ax[1].grid()
ax[1].tick_params(direction='in', labelsize=20)
ax[1].set_xlim(t.min(), t.max())

fig.tight_layout(pad=0)
#fig.savefig("phi_and_psi", bbox_inches='tight', dpi='figure')
plt.close()

ms = [0, 0, 1, -1]
ns = [1, 2, 0, 0]
colors = ['k', 'b', 'r', 'g']

s = np.linspace(-1, 4, 1001)

fig, ax = plt.subplots(2, 2, figsize=(12, 8))
ax = ax.flatten()

for i, (m, n, c) in enumerate(zip(ms, ns, colors)):
    ax[i].plot(s, psimn(m, n, s), f'o{c}', label=fr"$\varphi_{{{m},{n}}}(x)$", ms=.5)
    ax[i].plot(t, psimn(m, n, s), '--k', alpha=.5, lw=.5)

    ax[i].set_ylabel(fr"$\varphi_{{{m},{n}}}(x)$", size=25)
    ax[i].grid()
    ax[i].tick_params(direction='in', labelsize=20)
    ax[i].set_xlim(s.min(), s.max())

ax[-1].set_xlabel(r"$x$", size=25)
ax[-2].set_xlabel(r"$x$", size=25)

fig.tight_layout(pad=0)
#fig.savefig("psi_m_n", bbox_inches='tight', dpi='figure')
plt.close()
