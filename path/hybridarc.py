import numpy as np
from path import Path
from .point import Point


class HybridArc(Path):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def calc(self, t):
        c=self.start.dist(self.end)

        theta_start = self.start.theta
        theta_rot = self.start.theta
        theta_end = (2*self.start.angle_to(self.end))-theta_start
        theta_delta = theta_end - theta_start
        r = c / (2.0 * np.sin(theta_delta / 2.0))
        
        x_local = r*np.sin(t*theta_delta)
        y_local = r-r*np.cos(t*theta_delta)
        x_global_1 = self.start.x+x_local*np.cos(theta_rot)-y_local*np.sin(theta_rot)
        y_global_1 = self.start.y+x_local*np.sin(theta_rot)+y_local*np.cos(theta_rot)
        
        theta_end = self.end.theta
        theta_start = 2*self.start.angle_to(self.end)-theta_end
        theta_rot = theta_start
        theta_delta = theta_end - theta_start
        r = c / (2.0 * np.sin(theta_delta / 2.0))
        
        x_local = r*np.sin(t*theta_delta)
        y_local = r-r*np.cos(t*theta_delta)
        x_global_2 = self.start.x+x_local*np.cos(theta_rot)-y_local*np.sin(theta_rot)
        y_global_2 = self.start.y+x_local*np.sin(theta_rot)+y_local*np.cos(theta_rot)
        
        x_comb = (1-t)*x_global_1+t*x_global_2
        y_comb = (1-t)*y_global_1+t*y_global_2
        
        return Point(x_comb, y_comb)


    # def curvature(self, t):
    #     if np.isinf(self.r):
    #         return 0
    #     else:
    #         return 1.0 / self.r

    # def length(self):
    #     return self.s

    # def dist(self, t):
    #     return self.s * t

    # def t_at_dist(self, d):
    #     return d / self.s

