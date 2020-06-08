from path.functions import *
from path.point import Point
from generator.bot import Bot
from generator.generator import generate
from pint import UnitRegistry
from timeit import timeit


def time_generate():
    u = UnitRegistry()
    track = (11 * u.inch).to(u.meter).m
    diam = (4 * u.inch).to(u.meter).m
    weight = (20 * u.pounds).to(u.kilogram).m

    # path = new_bezier([Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0)])
    path = new_bezier([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)])

    # define bot
    bot = Bot(track=track, pose=path.calc(0))
    bot.set_theoretical_maxes(weight, 200, diam, 1)

    # generate the profile
    trajectory, profile, length, arcs, dt, wheel_speeds = generate(
        bot=bot, path=path, dt=0.01, arc_num=50
    )


if __name__ == "__main__":
    number = 10
    time = timeit(
        time_generate, setup="from main.timer import time_generate", number=number
    )
    print(f"{number} iterations took {time} seconds")
    print(f"Average time: {time/number} seconds")
