import matplotlib.pyplot as plt


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
        plt.plot(x, y, label=title)
