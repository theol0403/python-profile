from path.functions import *
from generator.profile import TrapezoidalConstraints
from generator.bot import Bot
from generator.generator import Generator

bot = Bot(track=1, max_vel=2)
constrants = TrapezoidalConstraints(max_vel=bot.max_vel, max_accel=1)
generator = Generator(constrants, bot)

path = new_hermite(QuinticHermite, Point(0, 0, 0), Point(1, 1, 0))

trajectory = generator.generate(path=path, dt=0.01, arcs=50)
