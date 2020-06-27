import matplotlib.pyplot as plt
import numpy as np


# a path returns a point containing x,y as a function ot t
class Path:
    def calc(self, t):
        pass

    def curvature(self, t):
        pass

    def interpolate(self, steps):
        return [self.calc(i / steps) for i in range(steps + 1)]

    def length(self):
        s = 0
        for t in np.arange(0, 1, 0.001):
            s += self.calc(t).dist(self.calc(t + 0.001))
        return s

    def t_at_dist_travelled(self, t, dist):
        return t + dist / np.abs(self.velocity(t))

    def plot(self, title):
        points = self.interpolate(200)
        x = [p.x for p in points]
        y = [p.y for p in points]
        plt.grid(True)
        plt.axis("equal")
        plt.plot(x, y, label=title)
