from main import *

x = [s.x for s in states]
y = [s.y for s in states]

line = plt.gca().plot(x, y, lw=2)


def animate(i):
    line[0].set_data(x[:i], y[:i])
    return line


animation.FuncAnimation(
    plt.gcf(), animate, frames=len(x) + 50, interval=dt * 1000, blit=True
)

plt.grid()
plt.show()
