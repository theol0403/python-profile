from path import Path
from .point import Point
import numpy as np


# a function is a one-dimensional calculation that maps x to y
class Function:
    def calc(self, x):
        """calculate y as a function of x"""
        pass

    def calc_d(self, x):
        """calculate y' as a function of x"""
        pass

    def calc_d_2(self, x):
        """calculate y'' as a function of x"""
        pass


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

    def velocity(self, t):
        return np.sqrt(self.x.calc_d(t) ** 2 + self.y.calc_d(t) ** 2)
