import itertools
from path import Path
from .functions import *


# a piecewise contains an array of paths
class Piecewise(Path):
    def __init__(self):
        self.arr = []

    def interpolate(self, steps):
        return sum((p.interpolate(steps) for p in self.arr), start=[])

    def calc(self, t):
        i = int(np.floor(t * len(self.arr)))
        if i == len(self.arr):
            i = len(self.arr) - 1
        x = t * len(self.arr) - i
        return self.arr[i].calc(x)

    # create a piecewise hermite path from a list of points
    def new_hermite(hermite, points):
        path = Piecewise()
        it = enumerate(points)
        # there is one less hermite than points
        it = itertools.islice(it, len(points) - 1)
        for i, p in it:
            path.arr.append(new_hermite(hermite, p, points[i + 1]))
        return path

    # create a piecewise bezier path from a 2 dimensional list of points
    def new_bezier(segments):
        path = Piecewise()
        for controls in segments:
            path.arr.append(new_bezier(controls))
