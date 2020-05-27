from simulation.bot import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

bot = Bot(15, Point(0, 0, math.pi/4))

print(bot.orientation)

bot.move(2, 2.0001, 1)

print(bot.orientation)

bot2 = Bot.default15()
start = bot2.orientation
vels = np.array(((10, 10.995, 1.0001, 10.995, 10, 10.995, 1.0001), (10.0001, -10.995, 1, -10.995, 10.0001, -10.995, 1)))

orientations = bot2.simulate(vels, 1)
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
