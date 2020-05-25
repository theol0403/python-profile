import itertools
from path import Path
from .functions.bezier import *
from .functions.hermite import *


class Piecewise(Path):
    def __init__(self):
        self.arr = []

    def interpolate(self, steps):
        return sum((p.interpolate(steps) for p in self.arr), start=[])

    def new_hermite(hermite, points):
        path = Piecewise()
        it = enumerate(points)
        # there is one less hermite than points
        it = itertools.islice(it, len(points)-1)
        for i, p in it:
            path.arr.append(new_hermite(hermite, p, points[i+1]))
        return path

    def new_bezier(segments):
        path = Piecewise()
        for controls in segments:
            path.arr.append(new_bezier(controls))
