import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 20, 1000)
zeta = 0.1
A = 1
omega1 = 2
omega2 = 3
phi = 0

x = A * np.exp(-zeta * omega1  * t) * np.cos(omega2 * t + phi)

fig=plt.figure()
plt.xlabel("Time (t)")
plt.ylabel("Displacement (x)")
plt.plot(t, x, zorder=2)
plt.axhline(y=0, color="black", zorder=1, linewidth=1)
plt.xlim(0,20)

plt.savefig('dhs.pdf', format='pdf')
plt.show()

