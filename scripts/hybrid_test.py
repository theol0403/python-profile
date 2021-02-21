from numpy import pi
from path.hybridarc import *
from path.bezier import *
from path.hermite import *
import matplotlib.pyplot as plt
from path.point import Point

# demonstrates arc interpolation
plt.figure(figsize=(6, 6), num="Hybrid Arc")
plt.grid()

arc = HybridArc(Point(0, 0), Point(2, 1, pi/2))

arc.plot("")

plt.tight_layout()
plt.show()
