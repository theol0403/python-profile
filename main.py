from path.functions.hermite import *
from path.functions.bezier import *
from point import Point
import matplotlib.pyplot as plt

plt.title("Path")

new_hermite(CubicHermite, Point(0, 0, 0), Point(1, 1, 0)).plot("Cubic Hermite")
new_hermite(QuinticHermite, Point(0, 0, 0),
            Point(1, 1, 0)).plot("Quintic Hermite")

new_bezier([Point(1, 0), Point(1, 1), Point(0, 1)]).plot("Quadratic Bezier")

new_bezier([Point(0, 0), Point(0, 1),
            Point(1, 1), Point(1, 0)]).plot("Cubic Bezier")

new_bezier([Point(0.0, 0.0),
            Point(0.0, 1.0),
            Point(0.5, 0.0),
            Point(1.0, 1.0),
            Point(1.0, 0.0)]).plot("Quartic Bezier")

new_bezier([Point(1.0, 0.0),
            Point(0.6, 0.0),
            Point(1.0, 1.0),
            Point(0.0, 0.6),
            Point(0.0, 1.0)]).plot("Quintic Bezier")

# new_bezier([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)]).plot("bezier")

plt.legend()
plt.show()
