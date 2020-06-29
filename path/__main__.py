import matplotlib.pyplot as plt
from .bezier import *
from .hermite import *
from .point import Point
from .piecewise import *


plt.figure(dpi=70, figsize=(8, 8))
plt.title("Path")

new_hermite(CubicHermite, Point(0, 0, 0), Point(1, 1, 0)).plot("Cubic Hermite")
new_hermite(QuinticHermite, Point(0, 0, 0), Point(1, 1, 0)).plot("Quintic Hermite")

new_bezier([Point(1, 0), Point(1, 1), Point(0, 1)]).plot("Quadratic Bezier")
new_bezier([Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0)]).plot("Cubic Bezier")

new_bezier(
    [
        Point(0.0, 0.0),
        Point(0.0, 1.0),
        Point(0.5, 0.0),
        Point(1.0, 1.0),
        Point(1.0, 0.0),
    ]
).plot("Quartic Bezier")

new_bezier(
    [
        Point(1.0, 0.0),
        Point(0.6, 0.0),
        Point(1.0, 1.0),
        Point(0.0, 0.6),
        Point(0.0, 1.0),
    ]
).plot("Quintic Bezier")

Piecewise.new_hermite(
    CubicHermite, [Point(0, 0, np.pi / 2), Point(0.5, 1, 0), Point(1, 0, -np.pi / 2)]
).plot("Piecewise Cubic Hermite")

Piecewise.new_hermite(
    QuinticHermite, [Point(0, 0, np.pi / 2), Point(0.5, 1, 0), Point(1, 0, -np.pi / 2)]
).plot("Piecewise Quintic Hermite")

new_bezier([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)]).plot("Cubic Bezier")

plt.legend()
plt.tight_layout()
plt.show()
