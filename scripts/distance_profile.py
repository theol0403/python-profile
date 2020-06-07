from generator.trapezoidal import Trapezoidal
from generator.bot import Bot
import matplotlib.pyplot as plt
import numpy as np

bot = Bot(track=1, max_vel=2, max_accel=1)
profile = Trapezoidal(bot, 3)

x = np.linspace(0, profile.length, 101)
y = [profile.v_at_d(d) for d in x]

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Vel vs Distance")
plt.grid()

dt = 0.01
vels = [profile.v_at_t(dt)]
dist = vels[0] * dt
while dist <= profile.length:
    vel = profile.v_at_d(dist)
    vels.append(vel)
    dist += vel * dt
vels.append(0)

final_dist = np.sum(np.array(vels) * dt)
print(f"Final distance: {final_dist}")

plt.subplot(1, 2, 2)
plt.plot(np.linspace(0, profile.time, len(vels)), vels)
plt.title("Vel vs Time")
plt.grid()

plt.tight_layout()
plt.show()
