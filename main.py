from path.functions import *
from path.point import Point
from generator.bot import Bot
from generator.generator import generate
import matplotlib.pyplot as plt
from pint import UnitRegistry

u = UnitRegistry()
track = (2 * u.feet).to(u.meter).m
diam = (4 * u.inch).to(u.meter).m

max_lin, max_ang = Bot.max_vels_from_scales(200, diam, track)

bot = Bot(track=track, max_vel=max_lin, max_accel=1, max_ang_vel=max_ang)
dt = 0.01

path = new_bezier([Point(0, 0), Point(1, 0), Point(2, 3), Point(3, 3)])

# generate the profile
trajectory, profile, length, arcs = generate(bot=bot, path=path, dt=dt, arc_num=50)

# x axis for time plots
time_range = np.linspace(0, len(trajectory) * dt, len(trajectory))

plt.subplot(2, 3, 1)
plt.title("Path")
plt.grid()

x = [step.point.x for step in trajectory]
y = [step.point.y for step in trajectory]
plt.plot(x, y)

plt.subplot(2, 3, 2)
plt.title("Angle")
plt.grid()

t = [step.point.theta for step in trajectory]
plt.plot(time_range, t)

plt.subplot(2, 3, 3)
plt.title("Curvature")
plt.grid()

c = [step.curvature for step in trajectory]
plt.plot(time_range, c)

c = [step.curvature_lerp for step in trajectory]
plt.plot(time_range, c)

plt.subplot(2, 3, 4)
plt.title("Velocity")
plt.grid()

vels = [step.v for step in trajectory]
plt.plot(time_range, vels)

plt.subplot(2, 3, 5)
plt.title("Angular Velocity")
plt.grid()

vels = [step.w for step in trajectory]
plt.plot(time_range, vels)

plt.subplot(2, 3, 6)
plt.title("Wheel Speeds")
plt.grid()

vel = np.array([step.v for step in trajectory])
ang_vel = np.array([step.w for step in trajectory])
left_speeds = vel - (ang_vel * bot.track) / 2
right_speeds = vel + (ang_vel * bot.track) / 2

plt.plot(time_range, left_speeds)
plt.plot(time_range, right_speeds)

states = bot.simulate(np.array((left_speeds, right_speeds)), dt)
x = [s.x for s in states]
y = [s.y for s in states]

pos_err = bot.pose.dist(path.calc(1))
ang_err = bot.pose.theta - path.calc(1).theta
print(f"Position error: {pos_err:.05} meters")
print(f"Angle error: {ang_err:.05} meters")

plt.gcf().set_tight_layout(True)
plt.show()
