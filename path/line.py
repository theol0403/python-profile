from path import Path


class Line(Path):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        theta = start.angle_to(end)
        self.start.theta = theta
        self.end.theta = theta

    def calc(self, t):
        return self.start + (self.end - self.start) * t

    def curvature(self, t):
        return 0

    def length(self):
        return self.start.dist(self.end)
