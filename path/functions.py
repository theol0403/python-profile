from .parametric import Parametric
import numpy as np


# a function is a one-dimensional calculation that maps x to y
class Function:
    def calc(self, x):
        """calculate y as a function of x"""
        pass

    def calc_d(self, x):
        """calculate y' as a function of x"""
        pass


# a bezier is a funtion that maps a group of control pointer to a bezier basis
class Bezier(Function):
    def __init__(self, ctrls):
        self.ctrls = ctrls

    def calc(self, x):
        order = len(self.ctrls) - 1
        return sum(
            map(lambda enum: basis(order, enum[0], x) * enum[1], enumerate(self.ctrls))
        )

    def calc_d(self, x):
        order = len(self.ctrls) - 1
        return sum(
            map(
                lambda power: basis(order - 1, power, x)
                * order
                * (self.ctrls[power + 1] - self.ctrls[power]),
                range(order),
            )
        )

    def calc_d_2(self, x):
        order = len(self.ctrls) - 1
        return sum(
            map(
                lambda power: basis(order - 2, power, x)
                * order
                * (order - 1)
                * (
                    self.ctrls[power + 2]
                    - 2 * self.ctrls[power + 1]
                    + self.ctrls[power]
                ),
                range(order - 1),
            )
        )


def basis(n, k, x):
    return comb(n, k) * (1.0 - x) ** (n - k) * x ** k


def comb(n, k):
    res = 1
    for i in range(k):
        res = (res * (n - i)) / (i + 1)
    return res


# create a new parametric bezier using n control points
def new_bezier(ctrls):
    return Parametric(Bezier([c.x for c in ctrls]), Bezier([c.y for c in ctrls]))


# a hermite is a one dimensional function that maps a group of coefficients to a power of t
class Hermite(Function):
    def calc(self, x):
        return sum(map(lambda enum: x ** enum[0] * enum[1], enumerate(self.coeffs)))

    def calc_d(self, x):
        it = enumerate(self.coeffs)
        next(it)
        return sum(map(lambda enum: x ** (enum[0] - 1) * enum[0] * enum[1], it))

    def calc_d_2(self, x):
        it = enumerate(self.coeffs)
        next(it)
        next(it)
        return sum(map(lambda enum: x ** (enum[0] - 2) * enum[0] * enum[1], it))


class CubicHermite(Hermite):
    def __init__(self, start, start_t, end, end_t):
        u = end - start

        a3 = 3.0 * u - 2.0 * start_t - end_t
        a4 = -2.0 * u + start_t + end_t

        self.coeffs = [start, start_t, a3, a4]


class QuinticHermite(Hermite):
    def __init__(self, start, start_t, end, end_t):
        u = end - start - start_t
        v = end_t - start_t

        a3 = 10.0 * u - 4.0 * v
        a4 = -15.0 * u + 7.0 * v
        a5 = 6.0 * u - 3.0 * v

        self.coeffs = [start, start_t, 0.0, a3, a4, a5]


# create a new parametric hermite
def new_hermite(hermite, start, end):
    x_start_t = np.cos(start.theta)
    y_start_t = np.sin(start.theta)

    x_end_t = np.cos(end.theta)
    y_end_t = np.sin(end.theta)

    return Parametric(
        hermite(start.x, x_start_t, end.x, x_end_t),
        hermite(start.y, y_start_t, end.y, y_end_t),
    )


# create a new parametric hermite with tangent stretch
def new_hermite_t(hermite, start, end, stretch):
    x_start_t = np.cos(start.theta) * stretch
    y_start_t = np.sin(start.theta) * stretch

    x_end_t = np.cos(end.theta)
    y_end_t = np.sin(end.theta)

    return Parametric(
        hermite(start.x, x_start_t, end.x, x_end_t),
        hermite(start.y, y_start_t, end.y, y_end_t),
    )
