from generator.trapezoidal import Trapezoidal
from path.arc import *


class Step:
    def __init__(self, point, v, w):
        self.point = point
        self.v = v
        self.w = w


class Generator:
    def __init__(self, constraints, drive):
        self.constraints = constraints
        self.drive = drive

    def generate(self, *, path, dt, arc_num):
        arcs = fit_arcs(path, arc_num).arr
        length = sum(a.length() for a in arcs)
        profile = Trapezoidal(self.constraints, length)

        trajectory = []

        dist = profile.v_at_t(dt) * dt
        while dist <= length:
            arc, t = arc_t_at_dist(arcs, dist)
            pos = arc.calc(t)

            vel = profile.v_at_d(dist)

            curvature = arc.curvature()
            angular_vel = vel * curvature

            dist += vel * dt
            trajectory.append(Step(pos, vel, angular_vel))

        # last step is 0
        trajectory.append(Step(arcs[-1].calc(1), 0, 0))
        return trajectory
