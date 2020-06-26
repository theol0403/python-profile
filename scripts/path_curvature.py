from path.arc import *
from path.functions import *
import matplotlib.pyplot as plt
from path.point import Point

# shows how the arc fitting does not produce continuous angle

plt.figure(dpi=70, figsize=(16, 8), num="Bezier Curvature")
plt.subplot(1, 2, 1)
plt.title("Path")

path = new_bezier([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)])
path.plot("")

plt.subplot(1, 2, 2)
plt.title("Curvature")

y = [path.curvature(t/100) for t in range(101)]
plt.plot(y)
plt.grid(True)

plt.tight_layout()
plt.show()
