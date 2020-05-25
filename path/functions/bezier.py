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
        return sum(map(lambda emum: basis(order, enum[0], x)*enum[1], self.ctrls))

    def calc_d(self, x):
        order = len(self.ctrls)
        it = iter(self.ctrls)
        itertools.islice(it, order)
        return sum(map(lambda power: basis(order - 1, power, x) * power
                       * self.ctrls[power + 1] - self.ctrls[power], it))


def basis(n, k, x):
    return comb(n, k) * (1.0-x) ** (n-k) * x ** k


def comb(n, k):
    res = 1
    for i in range(k):
        res = (res * (n - i)) / (i + 1)
    return res
