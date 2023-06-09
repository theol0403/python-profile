from generator.trapezoidal import Trapezoidal
from generator.bot import Bot
import matplotlib.pyplot as plt
import numpy as np

bot = Bot(track=1, max_vel=1, max_accel=1)
profile = Trapezoidal(bot, 3, start_vel=0.5, end_vel=0.5)
print(vars(profile))

dt = 0.01
x = np.arange(0, profile.time + dt, dt)
vels = [profile.v_at_t(t) for t in x]

print(f"Distance: {np.sum(vels)*dt}")

plt.plot(x, vels)
plt.title("Vel vs Time")
plt.grid()

plt.tight_layout()
plt.show()
