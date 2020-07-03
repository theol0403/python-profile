import itertools
from path import Path
from .bezier import new_bezier
from .hermite import new_hermite


# a piecewise contains an array of paths
class Piecewise(Path):
    def __init__(self):
        self.arr = []

    def calc(self, t):
        return self.split(t, "calc")

    def curvature(self, t):
        return self.split(t, "curvature")

    def velocity(self, t):
        return self.split(t, "velocity") * len(self.arr)

    def interpolate(self, steps):
        return sum((p.interpolate(steps) for p in self.arr), start=[])

    def length(self):
        return sum(p.length() for p in self.arr)

    def split(self, t, f):
        # split up t into arc_count sections
        c = len(self.arr)
        i = int(t * c)  # which arc to use
        if i == c:
            # use t = 1 for the last arc
            i = c - 1
        x = t * c - i  # which t to use
        return getattr(self.arr[i], f)(x)

    # create a piecewise bezier path from a 2 dimensional list of points
    def new_bezier(segments):
        path = Piecewise()
        for controls in segments:
            path.arr.append(new_bezier(controls))

    # create a piecewise hermite path from a list of points
    def new_hermite(hermite, points):
        path = Piecewise()
        it = enumerate(points)
        # there is one less hermite than points
        it = itertools.islice(it, len(points) - 1)
        for i, p in it:
            path.arr.append(new_hermite(hermite, p, points[i + 1]))
        return path
