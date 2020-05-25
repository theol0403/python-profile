from parametric import Function


# a hermite is a one dimensional function that maps a group of coefficients to a power of t
class Hermite(Function):
    def calc(self, x):
        sum(map(lambda power, coef: x**power * coef, enumerate(self.coeffs)))

    def calc_d(self, x):
        sum(map(lambda power, coef: x**(power - 1) * power
                * coef, enumerate(self.coeffs).next()))
