from main.__main__ import *
from timeit import timeit


def time_generate():
    # path = new_bezier([Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0)])
    path = new_bezier([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)])
    # path = new_hermite(CubicHermite, Point(0, 0, 0), Point(1, 1, 0))

    generate(bot=bot, path=path, dt=0.01, arc_num=50)


if __name__ == "__main__":
    number = 200
    time = timeit(time_generate, number=number)
    print("")
    print(f"{number} iterations took {time:.4} seconds")
    print(f"Average time: {time/number*1000:.5} ms")
