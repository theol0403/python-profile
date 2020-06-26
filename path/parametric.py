from path import Path
from .point import Point
import numpy as np


# a parametric contains two functions that map t to x and y.
# It therefore qualifies as a path.
class Parametric(Path):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self, t):
        x = self.x.calc(t)
        y = self.y.calc(t)

        x1 = self.x.calc_d(t)
        y1 = self.y.calc_d(t)

        return Point(x, y, np.arctan2(y1, x1))

    def curvature(self, t):
        x_d = self.x.calc_d(t)
        y_d = self.y.calc_d(t)
        x_d_2 = self.x.calc_d_2(t)
        y_d_2 = self.y.calc_d_2(t)
        return (x_d * y_d_2 - y_d * x_d_2) / np.sqrt(x_d ** 2 + y_d ** 2) ** 3

    def derivative(self, t):
        y = self.y.calc_d(t)
        x = self.x.calc_d(t)
        return y / x

    def t_at_dist(self, t, dist):
        s = 0
        while s < dist:
            s += self.calc(t).dist(self.calc(t + 0.0001))
            t += 0.0001
        return t
        # return t + dist / np.abs(self.derivative(t))

    def length(self):
        l = 0
        for t in np.arange(0, 1, 0.01):
            l += self.calc(t).dist(self.calc(t + 0.01))
        return l
