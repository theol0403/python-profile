from ..parametric import Parametric
from . import Function
import numpy as np
import itertools


# a bezier is a funtion that maps a group of control pointer to a bezier basis
class Bezier(Function):
    def __init__(self, ctrls):
        self.ctrls = ctrls

    def calc(self, x):
        order = len(self.ctrls)
        return sum(map(lambda enum: basis(order, enum[0], x)*enum[1], enumerate(self.ctrls)))

    def calc_d(self, x):
        order = len(self.ctrls)
        return sum(map(lambda power: basis(order - 1, power, x) * power
                       * self.ctrls[power + 1] - self.ctrls[power], range(order - 1)))


def basis(n, k, x):
    return comb(n, k) * (1.0-x) ** (n-k) * x ** k


def comb(n, k):
    res = 1
    for i in range(k):
        res = (res * (n - i)) / (i + 1)
    return res


def new_bezier(ctrls):
    return Parametric(Bezier([c.x for c in ctrls]), Bezier([c.y for c in ctrls]))
