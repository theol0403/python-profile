from path.functions.hermite import *
from path.functions.bezier import *
from point import Point
import matplotlib.pyplot as plt

plt.title("Path")

path = new_hermite(CubicHermite, Point(0, 0, 0), Point(1, 1, 0))
path.plot("hermite")

path = new_bezier([Point(0, 0, 0), Point(1, 0, 0),
                   Point(0, 1, 0), Point(1, 1, 0)])
path.plot("bezier")

plt.legend()
plt.show()
