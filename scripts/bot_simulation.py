from generator.bot import *
from generator.trapezoidal import Trapezoidal, TrapezoidalConstraints
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

bot = Bot(track=15, pose=Point(0, 0, math.pi / 4))
print(Bot.max_vels_from_scales(200, 0.05, 1, 0.3))
print(bot.max_lin_vel_at_curvature(0.5))

bot2 = Bot.default15(max_vel=2)
start = bot2.pose

constraints = TrapezoidalConstraints(max_vel=bot2.max_vel, max_accel=1)
profile = Trapezoidal(constraints, 10)

dt = 0.1
vels = []
dist = 0
vel = profile.v_at_t(dt)
while dist <= profile.length:
    vels.append(vel)
    dist += vel * dt
    vel = profile.v_at_d(dist)
vels.append(vel)

vels = np.tile(vels, (2, 1))

states = bot2.simulate(vels, dt)
x = np.zeros(len(states) + 1)
y = np.zeros(len(states) + 1)
thetas = np.zeros(len(states) + 1)
x[0] = start.x
y[0] = start.y
thetas[0] = start.theta
for i in range(len(states)):
    print(states[i])
    x[i + 1] = states[i].x
    y[i + 1] = states[i].y
    thetas[i + 1] = states[i].theta

plt.scatter(x, y, marker=".")
plt.show()
