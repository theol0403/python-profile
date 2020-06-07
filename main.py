from path.functions import *
from path.point import Point
from generator.bot import Bot
from generator.generator import generate
import matplotlib.pyplot as plt

bot = Bot(track=1, max_vel=1, max_accel=0.5, max_ang_vel=1)

path = new_bezier([Point(0, 0), Point(1, 0), Point(2, 3), Point(3, 3)])

# generate the profile
trajectory, profile, length, arcs = generate(bot=bot, path=path, dt=0.01, arc_num=5)

# x axis for time plots
time_range = np.linspace(0, len(trajectory) * 0.01, len(trajectory))

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
l = vel + (ang_vel * bot.track) / 2
r = vel - (ang_vel * bot.track) / 2

plt.plot(time_range, l)
plt.plot(time_range, r)

plt.gcf().set_tight_layout(True)
plt.show()
