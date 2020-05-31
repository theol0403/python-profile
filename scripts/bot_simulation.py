from simulation.bot import *
from generator.trapezoidal import Trapezoidal, TrapezoidalConstraints
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

bot = Bot(track=15, pose=Point(0, 0, math.pi / 4), max_vel=2)
print(bot.pose)
bot.move(2, 2.0001, 1)
print(bot.pose)

bot2 = Bot.default15()
start = bot2.pose

constraints = TrapezoidalConstraints(max_vel=bot.max_vel, max_accel=1)
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

orientations = bot2.simulate(vels, dt)
x = np.zeros(len(orientations) + 1)
y = np.zeros(len(orientations) + 1)
thetas = np.zeros(len(orientations) + 1)
x[0] = start.x
y[0] = start.y
thetas[0] = start.theta
for i in range(len(orientations)):
    print(orientations[i])
    x[i + 1] = orientations[i].x
    y[i + 1] = orientations[i].y
    thetas[i + 1] = orientations[i].theta

plt.scatter(x, y, marker=".")
plt.show()
