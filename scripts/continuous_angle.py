from path.arc import *
from path.functions import *
import matplotlib.pyplot as plt
from path.point import Point


# plt.figure(dpi=70, figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.title("Path")

path = new_bezier([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)])
path.plot("")

arcs = fit_arcs(path, 3)
arcs.plot("")

plt.subplot(1, 2, 2)
plt.title("Angle")

x = [x/152 for x in range(153)]
y = [p.theta for p in arcs.interpolate(50)]
plt.plot(x, y)

plt.tight_layout()
plt.show()
