from path.arc import *
from path.functions import *
import matplotlib.pyplot as plt
from path.point import Point
import matplotlib.animation as animation

# demonstrates arc interpolation
plt.figure(dpi=70, figsize=(12, 12), num="Arc Interpolation")

path = new_bezier([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)])

arcs = fit_arcs(path, 20)

x = [arcs.calc(t).x for t in np.linspace(0.0, 1.0, 201)]
y = [arcs.calc(t).y for t in np.linspace(0.0, 1.0, 201)]

line = plt.gca().plot(x, y, lw=2)


def animate(i):
    line[0].set_data(x[:i], y[:i])
    return line


animation.FuncAnimation(plt.gcf(), animate, frames=len(x) + 50, interval=10, blit=True)

plt.show()
