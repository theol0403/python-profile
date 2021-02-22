from .arc import *


class HybridArc(Path):
    def __init__(self, start, end):
        theta_end = (2*start.angle_to(end))-start.theta
        self.arc_start = Arc(start, Point(end.x, end.y, theta_end))
        theta_start = 2*start.angle_to(end)-end.theta
        self.arc_end = Arc(Point(start.x, start.y, theta_start), end)

    def calc(self, t):
        point_start = self.arc_start.calc(t)
        point_end = self.arc_end.calc(t)
        comb = point_start*(1-t) + point_end*t
        return comb

    # def curvature(self, t):
    #     if np.isinf(self.r):
    #         return 0
    #     else:
    #         return 1.0 / self.r


