import numpy as np
from path import Path
from .point import Point
from .piecewise import Piecewise


class Arc(Path):
    def __init__(self, start, end):
        self.theta = end.theta - start.theta
        c = start.dist(end)

        if np.isclose(self.theta, 0.0):
            self.r = np.Infinity
            self.s = c
        else:
            self.r = c / (2.0 * np.sin(self.theta / 2.0))
            self.s = self.r * self.theta

        self.rotate = start.angle_to(end) - self.theta / 2.0
        self.origin = start

    def dist(self, t):
        return self.s * t

    def t_at_dist(self, d):
        return d / self.s

    def calc(self, t):
        x, y = 0, 0
        if np.isinf(self.r):
            y = self.s * t
        else:
            x = self.r * np.cos(t * self.theta) - self.r
            y = self.r * np.sin(t * self.theta)

        theta = self.rotate - np.pi / 2.0

        x_r = x * np.cos(theta) - y * np.sin(theta)
        y_r = y * np.cos(theta) + x * np.sin(theta)

        x_r += self.origin.x
        y_r += self.origin.y

        return Point(x_r, y_r, self.rotate + self.theta * t)


def fit_arcs(path, num):
    arcs = Piecewise()
    start = path.calc(0)
    for i in range(num):
        end = path.calc((1.0 / num) * (i + 1))
        arcs.arr.append(Arc(start, end))
        start = end
    return arcs
