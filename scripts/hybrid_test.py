from numpy import pi
from path.hybridarc import *
from path.bezier import *
from path.hermite import *
import matplotlib.pyplot as plt
from path.point import Point

# demonstrates arc interpolation
plt.figure(figsize=(6, 6), num="Hybrid Arc")
plt.grid()

start = Point(0, 0)
end = Point(2, 1, pi / 2)
arc = Arc(start, end)
arc.plot("")

print(f"Length: { arc.length()}")
print(f"Velocity: { arc.velocity(0.4)}")
print(f"Curv: { arc.curvature(0.6)}")
print(f"CCurv: { 1.0 / arc.r}")

# theta_end = (2 * start.angle_to(end)) - start.theta
# Arc(start, Point(end.x, end.y, theta_end)).plot("")
# theta_start = 2 * start.angle_to(end) - end.theta
# Arc(Point(start.x, start.y, theta_start), end).plot("")


plt.tight_layout()
plt.show()
