from .parametric import Parametric, Function
import math


# a bezier is a funtion that maps a group of control pointer to a bezier basis
class Bezier(Function):
    def __init__(self, ctrls):
        self.ctrls = ctrls
        self.order = len(ctrls) - 1

    def calc(self, x):
        def calc_ctrl(i, ctrl):
            return basis(self.order, i, x) * ctrl

        return sum(map(lambda enum: calc_ctrl(enum[0], enum[1]), enumerate(self.ctrls)))

    def calc_d(self, x):
        order = self.order

        def calc_power(power):
            return (
                basis(order - 1, power, x)
                * order
                * (self.ctrls[power + 1] - self.ctrls[power])
            )

        return sum(map(calc_power, range(order)))

    def calc_d_2(self, x):
        order = len(self.ctrls) - 1

        def calc_power(power):
            return (
                basis(order - 2, power, x)
                * order
                * (order - 1)
                * (
                    self.ctrls[power + 2]
                    - 2 * self.ctrls[power + 1]
                    + self.ctrls[power]
                )
            )

        return sum(map(calc_power, range(order - 1)))


def basis(n, k, x):
    return comb(n, k) * (1.0 - x) ** (n - k) * x ** k


def comb(n, k):
    if k < 0 or k > n:
        return 0
    if k > n - k:
        k = n - k
    if k == 0 or n <= 1:
        return 1
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


# create a new parametric bezier using n control points
def new_bezier(ctrls):
    return Parametric(Bezier([c.x for c in ctrls]), Bezier([c.y for c in ctrls]))
