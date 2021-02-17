import matplotlib.pyplot as plt
import numpy as np


# a path returns a point containing x,y as a function ot t
class Path:
    def calc(self, t):
        pass

    def curvature(self, t):
        pass

    # the distance traveled per change in t
    # the hypotenuse of the derivatives of the x and y functions
    # ds/dt
    def velocity(self, t):
        return self.length()

    def interpolate(self, steps):
        return [self.calc(i / steps) for i in range(steps + 1)]

    def length(self):
        res = 0.01
        s = 0
        for t in np.arange(0, 1, res):
            s += self.calc(t).dist(self.calc(t + res))
        return s

    #    def length(self):
    #        return fit_arcs(self, 500).length()

    def t_at_dist_travelled(self, t, dist):
        return t + dist / np.abs(self.velocity(t))

    def plot(self, title):
        points = self.interpolate(200)
        x = [p.x for p in points]
        y = [p.y for p in points]
        plt.grid(True)
        plt.axis("equal")
        plt.plot(x, y, label=title)
