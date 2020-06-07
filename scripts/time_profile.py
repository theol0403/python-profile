from generator.trapezoidal import Trapezoidal
from generator.bot import Bot
import matplotlib.pyplot as plt
import numpy as np

bot = Bot(track=1, max_vel=2, max_accel=1)
profile = Trapezoidal(bot, 7)

dt = 0.01
x = np.arange(0, profile.time + dt, dt)
vels = [profile.v_at_t(t) for t in x]

plt.plot(x, vels)
plt.title("Vel vs Time")
plt.grid()

plt.tight_layout()
plt.show()
