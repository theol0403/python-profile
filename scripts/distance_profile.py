from generator.trapezoidal import Trapezoidal, TrapezoidalConstraints
import matplotlib.pyplot as plt
import numpy as np

constraints = TrapezoidalConstraints(max_vel=2, max_accel=1)
profile = Trapezoidal(constraints, 10)

x = np.linspace(0, profile.length, 101)
y = [profile.v_at_d(d) for d in x]

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Vel vs Distance")
plt.grid()

dt = 0.01
vels = []
dist = 0
vel = profile.v_at_t(dt)
while dist <= profile.length:
    vels.append(vel)
    dist += vel * dt
    vel = profile.v_at_d(dist)
vels.append(vel)

final_dist = np.sum(np.array(vels) * dt)
print(f"Final distance: {final_dist}")

plt.subplot(1, 2, 2)
plt.plot(np.linspace(0, profile.time, len(vels)), vels)
plt.title("Vel vs Time")
plt.grid()

plt.tight_layout()
plt.show()
