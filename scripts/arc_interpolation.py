from path.arc import *
from path.functions import *
import matplotlib.pyplot as plt
from path.point import Point

# demonstrates arc interpolation
plt.figure(dpi=70, figsize=(12, 12), num='Arc Interpolation')

path = new_bezier([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)])

plt.subplot(2, 2, 1)
plt.title("2 Arcs")
path.plot("")
arcs = fit_arcs(path, 2)
arcs.plot("")

plt.subplot(2, 2, 2)
plt.title("3 Arcs")
path.plot("")
arcs = fit_arcs(path, 3)
arcs.plot("")

plt.subplot(2, 2, 3)
plt.title("4 Arcs")
path.plot("")
arcs = fit_arcs(path, 4)
arcs.plot("")

plt.subplot(2, 2, 4)
plt.title("10 Arcs")
path.plot("")
arcs = fit_arcs(path, 10)
arcs.plot("")

plt.tight_layout()
plt.show()
