from .arc import *


class HybridArc(Path):
    def __init__(self, start, end):
        theta_end = (2 * start.angle_to(end)) - start.theta
        self.arc_start = Arc(start, Point(end.x, end.y, theta_end))
        theta_start = 2 * start.angle_to(end) - end.theta
        self.arc_end = Arc(Point(start.x, start.y, theta_start), end)

    def calc(self, t):
        point_start = self.arc_start.calc(t)
        point_end = self.arc_end.calc(t)
        comb = point_start * (1 - t) + point_end * t
        return comb

    def calc_d(self, t):
        point_start = self.arc_start.calc(t)
        point_end = self.arc_end.calc(t)
        d_start = self.arc_start.calc_d(t)
        d_end = self.arc_end.calc_d(t)
        comb = d_start * (1 - t) - point_start + d_end * t + point_end
        return comb

    def calc_d_2(self, t):
        d_start = self.arc_start.calc_d(t)
        d2_start = self.arc_start.calc_d_2(t)
        d_end = self.arc_end.calc_d(t)
        d2_end = self.arc_end.calc_d_2(t)
        comb = d2_start * (1 - t) - d_start - d_start + d2_end * t + d_end + d_end
        return comb

    def velocity(self, t):
        d = self.calc_d(t)
        return np.sqrt(d.x ** 2 + d.y ** 2)

    def curvature(self, t):
        x_d = self.calc_d(t).x
        y_d = self.calc_d(t).y
        x_d_2 = self.calc_d_2(t).x
        y_d_2 = self.calc_d_2(t).y
        return (x_d * y_d_2 - y_d * x_d_2) / np.sqrt(x_d ** 2 + y_d ** 2) ** 3

    # def curvature(self, t):
    #     start = self.arc_start.curvature(t)
    #     end = self.arc_end.curvature(t)
    #     comb = start * (1 - t) + end * t
    #     return comb

    # def curvature(self, t):
    #     if np.isinf(self.r):
    #         return 0
    #     else:
    #         return 1.0 / self.r
