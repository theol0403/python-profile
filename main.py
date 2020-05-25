from path.functions.hermite import *
from point import Point

import matplotlib.pyplot as plt

path = new_hermite(CubicHermite, Point(0, 0, 0), Point(1, 1, 0))

points = [path.calc(i/100) for i in range(100)]
x = [p.x for p in points]
y = [p.y for p in points]

plt.plot(x, y)
plt.show()
