from path.functions import *
from path.point import Point
from generator.bot import Bot
from generator.generator import generate
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from generator.plot_profile import *
from pint import UnitRegistry

u = UnitRegistry()
track = (11 * u.inch).to(u.meter).m
diam = (4 * u.inch).to(u.meter).m
weight = (20 * u.pounds).to(u.kilogram).m

path = new_bezier([Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0)])
# path = new_bezier([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)])

# define bot
bot = Bot(track=track, pose=path.calc(0))
bot.set_theoretical_maxes(weight, 200, diam, 4)
print(f"Max velocity: {bot.max_vel}")
print(f"Max acceleration: {bot.max_accel}")

# generate the profile
trajectory, profile, length, arcs, dt, wheel_speeds = generate(
    bot=bot, path=path, dt=0.01, arc_num=50
)

# show everything
plot_profile(trajectory, path, dt, wheel_speeds)

# run the bot through all the steps
states = bot.simulate(np.array(wheel_speeds), dt)

pos_err = bot.pose.dist(path.calc(1))
ang_err = (bot.pose.theta - path.calc(1).theta) * 180 / np.pi
print(f"Position error: {pos_err:.05} meters")
print(f"Angle error: {ang_err:.05} degrees")

plt.gcf().set_tight_layout(True)
plt.show()

x = [s.x for s in states]
y = [s.y for s in states]

ax = plt.axes()
plt.grid()
xmin, xmax = np.min(x), np.max(x)
ymin, ymax = np.min(y), np.max(y)
ax.set_xlim(xmin - 0.1 * (xmax - xmin), xmax + 0.1 * (xmax - xmin))
ax.set_ylim(ymin - 0.1 * (ymax - ymin), ymax + 0.1 * (ymax - ymin))
(line,) = ax.plot([], [], lw=2)


def animate(i):
    line.set_data(x[:i], y[:i])
    return (line,)


animation.FuncAnimation(plt.gcf(), animate, frames=len(x) + 50, interval=10, blit=True)

plt.show()
