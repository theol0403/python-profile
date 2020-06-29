from .parametric import Parametric, Function
import numpy as np


# a hermite is a one dimensional function that maps a group of coefficients to a power of t
class Hermite(Function):
    def calc(self, x):
        def f(power, coeff):
            return coeff * x ** power

        return sum(map(lambda enum: f(enum[0], enum[1]), enumerate(self.coeffs)))

    def calc_d(self, x):
        def f(power, coeff):
            return coeff * power * x ** (power - 1)

        it = enumerate(self.coeffs)
        next(it)
        return sum(map(lambda enum: f(enum[0], enum[1]), it))

    def calc_d_2(self, x):
        def f(power, coeff):
            return coeff * power * power * x ** (power - 2)

        it = enumerate(self.coeffs)
        next(it)
        next(it)
        return sum(map(lambda enum: f(enum[0], enum[1]), it))


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
