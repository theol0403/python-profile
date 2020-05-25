from path.functions.hermite import *
from point import Point
import matplotlib.pyplot as plt

plt.title("Path")
path = new_hermite(CubicHermite, Point(0, 0, 0), Point(1, 1, 0))
path.plot("hermite")

plt.legend()
plt.show()
