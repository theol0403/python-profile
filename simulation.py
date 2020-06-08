from main import *


x = [s.x for s in states]
y = [s.y for s in states]

ax = plt.axes()
plt.grid()
xmin, xmax = np.min(x), np.max(x)
ymin, ymax = np.min(y), np.max(y)
ax.set_xlim(xmin - 0.1 * (xmax - xmin), xmax + 0.1 * (xmax - xmin))
ax.set_ylim(ymin - 0.1 * (ymax - ymin), ymax + 0.1 * (ymax - ymin))
(line,) = ax.plot([], [], lw=2)


def animate(i):
    line.set_data(x[:i], y[:i])
    return (line,)


animation.FuncAnimation(plt.gcf(), animate, frames=len(x) + 50, interval=10, blit=True)

plt.show()
