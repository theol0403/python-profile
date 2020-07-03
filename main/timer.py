from main.__main__ import *
from timeit import timeit


def time_generate():
    generate(bot=bot, path=path, dt=0.01)


if __name__ == "__main__":
    number = 100
    time = timeit(time_generate, number=number)
    print("")
    print(f"{number} iterations took {time:.4} seconds")
    print(f"Average time: {time/number*1000:.5} ms")
