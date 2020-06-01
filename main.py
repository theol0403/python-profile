from path.functions import *
from path.point import Point
from generator.trapezoidal import TrapezoidalConstraints
from generator.bot import Bot
from generator.generator import Generator
import matplotlib.pyplot as plt

bot = Bot(track=1, max_vel=1)
constrants = TrapezoidalConstraints(max_vel=bot.max_vel, max_accel=0.5)
generator = Generator(constrants, bot)

path = new_bezier([Point(0, 0), Point(2, 0), Point(1, 3), Point(3, 3)])

trajectory = generator.generate(path=path, dt=0.01, arc_num=50)

time_range = np.linspace(0, len(trajectory) * 0.01, len(trajectory))

plt.subplot(2, 2, 1)
plt.title("Path")
plt.grid()

x = [step.point.x for step in trajectory]
y = [step.point.y for step in trajectory]
plt.plot(x, y)

plt.subplot(2, 2, 2)
plt.title("Angle")
plt.grid()

t = [step.point.theta for step in trajectory]
plt.plot(time_range, t)

plt.subplot(2, 2, 3)
plt.title("Velocity")
plt.grid()

vels = [step.v for step in trajectory]
plt.plot(time_range, vels)

plt.subplot(2, 2, 4)
plt.title("Angular Velocity")
plt.grid()

vels = [step.w for step in trajectory]
plt.plot(time_range, vels)

plt.tight_layout()
plt.show()
