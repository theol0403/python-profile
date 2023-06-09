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

    def calc_d(self, t):
        x, y = 0, 0
        if np.isinf(self.r):
            y = self.s
        else:
            x = self.r * self.theta * -np.sin(t * self.theta)
            y = self.r * self.theta * np.cos(t * self.theta)

        theta = self.rotate - np.pi / 2.0

        x_r = x * np.cos(theta) - y * np.sin(theta)
        y_r = y * np.cos(theta) + x * np.sin(theta)

        return Point(x_r, y_r)

    def calc_d_2(self, t):
        x, y = 0, 0
        if np.isinf(self.r):
            y = 0
        else:
            x = self.r * self.theta ** 2 * -np.cos(t * self.theta)
            y = self.r * self.theta ** 2 * -np.sin(t * self.theta)

        theta = self.rotate - np.pi / 2.0

        x_r = x * np.cos(theta) - y * np.sin(theta)
        y_r = y * np.cos(theta) + x * np.sin(theta)

        return Point(x_r, y_r)

    def curvature(self, t):
        if np.isinf(self.r):
            return 0
        else:
            return 1.0 / self.r

    def length(self):
        return self.s

    def dist(self, t):
        return self.s * t

    def t_at_dist(self, d):
        return d / self.s

    def velocity(self, t):
        d = self.calc_d(t)
        return np.sqrt(d.x ** 2 + d.y ** 2)

    # def curvature(self, t):
    #     x_d = self.calc_d(t).x
    #     y_d = self.calc_d(t).y
    #     x_d_2 = self.calc_d_2(t).x
    #     y_d_2 = self.calc_d_2(t).y
    #     return (x_d * y_d_2 - y_d * x_d_2) / np.sqrt(x_d ** 2 + y_d ** 2) ** 3


def fit_arcs(path, num):
    arcs = Piecewise()
    start = path.calc(0)
    for i in range(num):
        end = path.calc((1.0 / num) * (i + 1))
        arcs.arr.append(Arc(start, end))
        start = end
    return arcs


def arc_t_at_dist(arcs, dist):
    # find the arc and t along that arc given distance
    dist_remaining = dist  # gets reduced until it fits in the length of an arc
    for i, arc in enumerate(arcs):
        if dist_remaining > arc.length():
            dist_remaining -= arc.length()
        else:
            return i, arc, arc.t_at_dist(dist_remaining)


class Interpolator:
    @staticmethod
    def none(arcs, i, t):
        return arcs[i].curvature(t)

    @staticmethod
    def midpoint(arcs, i, t):
        start = arcs[i].curvature(t)
        end = start
        if i > 0:
            start = (start + arcs[i - 1].curvature(t)) / 2
        if i < len(arcs) - 1:
            end = (start + arcs[i + 1].curvature(t)) / 2
        return start + t * (end - start)

    @staticmethod
    def left(arcs, i, t):
        if i < len(arcs) - 1:
            start_c = arcs[i].curvature(t)
            end_c = arcs[i + 1].curvature(t)
            return start_c + t * (end_c - start_c)
        else:
            return arcs[i].curvature(t)

    @staticmethod
    def right(arcs, i, t):
        if i > 0:
            start_c = arcs[i - 1].curvature(t)
            end_c = arcs[i].curvature(t)
            return start_c + t * (end_c - start_c)
        else:
            return arcs[i].curvature(t)

    @staticmethod
    def trapezoidal(arcs, i, t):
        left = Interpolator.left(arcs, i, t)
        right = Interpolator.right(arcs, i, t)
        return (left + right) / 2
