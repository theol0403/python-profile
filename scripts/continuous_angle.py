from path.arc import *
from path.functions import *
import matplotlib.pyplot as plt
from path.point import Point

# shows how the arc fitting does not produce continuous angle

plt.figure(dpi=70, figsize=(16, 8), num="Continuous Angle")
plt.subplot(1, 2, 1)
plt.title("Path")

path = new_bezier([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)])
path.plot("")

arcs = fit_arcs(path, 3)
arcs.plot("")

plt.subplot(1, 2, 2)
plt.title("Angle")

y = [p.theta for p in arcs.interpolate(100)]
x = [x / (len(y) - 1) for x in range(len(y))]
plt.plot(x, y)
plt.grid(True)

plt.tight_layout()
plt.show()
