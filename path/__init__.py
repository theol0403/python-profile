import matplotlib.pyplot as plt


# a path returns a point containing x,y as a function ot t
class Path:
    def calc(self, t):
        pass

    def interpolate(self, steps):
        return [self.calc(i / steps) for i in range(steps + 1)]

    def plot(self, title):
        points = self.interpolate(200)
        x = [p.x for p in points]
        y = [p.y for p in points]
        plt.grid(True)
        plt.axis('equal')
        plt.plot(x, y, label=title)
