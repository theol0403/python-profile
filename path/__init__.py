import matplotlib.pyplot as plt
import numpy as np


# a path returns a point containing x,y as a function ot t
class Path:
    def calc(self, t):
        pass

    def derivative(self, t):
        pass

    def curvature(self, t):
        pass

    def interpolate(self, steps):
        return [self.calc(i / steps) for i in range(steps + 1)]

    def length(self):
        l = 0
        for t in np.arange(0, 1, 0.01):
            l += self.calc(t).dist(self.calc(t + 0.01))
        return l

    def t_at_dist_travelled(self, t, dist):
        s = 0
        while s < dist:
            s += self.calc(t).dist(self.calc(t + 0.0001))
            t += 0.0001
        return t
        # return t + dist / np.abs(self.derivative(t))

    def plot(self, title):
        points = self.interpolate(200)
        x = [p.x for p in points]
        y = [p.y for p in points]
        plt.grid(True)
        plt.axis("equal")
        plt.plot(x, y, label=title)
