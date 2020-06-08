from generator.bot import *
from generator.trapezoidal import Trapezoidal
import matplotlib.pyplot as plt

bot = Bot.default15(max_vel=2, max_accel=1)
profile = Trapezoidal(bot, 10)

dt = 0.1
vels = [profile.v_at_t(dt)]
dist = vels[0] * dt
while dist <= profile.length:
    vel = profile.v_at_d(dist)
    vels.append(vel)
    dist += vel * dt
vels.append(0)

vels = np.tile(vels, (2, 1))

states = bot.simulate(vels, dt)
x = [s.x for s in states]
y = [s.y for s in states]

plt.scatter(x, y, marker=".")
plt.show()
