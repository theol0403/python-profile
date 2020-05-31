from simulation.bot import *
from generator.trapezoidal import DistanceTrapezoidal
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

bot = Bot(15, Point(0, 0, math.pi / 4), 1, 4)

print(bot.pose)

bot.move(2, 2.0001, 1)

print(bot.pose)

bot2 = Bot.default15()
start = bot2.pose

profile = DistanceTrapezoidal(1, 2, 10)
vels = [[], []]
dt = 0.001
dist = 0.0000001
while dist <= profile.length:
    vel = profile.calc_at_d(dist)
    vels[0].append(vel)
    vels[1].append(vel)
    dist += vel * dt


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

plt.scatter(x, y)
plt.show()
