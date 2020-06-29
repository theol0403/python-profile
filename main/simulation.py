from main.__main__ import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = [s.x for s in states]
y = [s.y for s in states]

line = plt.gca().plot(x, y, lw=2)


def animate(i):
    line[0].set_data(x[:i], y[:i])
    return line


animation.FuncAnimation(
    plt.gcf(), animate, frames=len(x) + int(0.5 / dt), interval=dt * 1000, blit=True
)

plt.grid()
plt.title("Trajectory Simulation")
plt.gcf().set_tight_layout(True)
plt.show()
