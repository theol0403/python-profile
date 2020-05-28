from generator.trapezoidal import Trapezoidal
import matplotlib.pyplot as plt
import numpy as np


profile = Trapezoidal(1, 2, 10)

x = [d/10 for d in range(101)]
y = [profile.calc_at_d(d) for d in x]

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Vel vs Distance")
plt.grid()

vels = []
dt = 0.01
dist = 0.0000001
while dist <= profile.length:
    vel = profile.calc_at_d(dist)
    vels.append(vel)
    dist += vel * dt

time = len(vels) * dt

plt.subplot(1, 2, 2)
plt.plot(np.linspace(0, time, len(vels)), vels)
plt.title("Vel vs Time")
plt.grid()

plt.tight_layout()
plt.show()
