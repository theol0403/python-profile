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

        dist = 0
        vel = profile.v_at_t(dt)
        while dist <= length:

            # find the arc and t along that arc given distance
            current_arc, arc_t = 0, 0
            dist_remaining = dist  # gets reduced until it fits in the length of an arc
            for arc in arcs:
                if dist_remaining > arc.length():
                    dist_remaining -= arc.length()
                else:
                    current_arc = arc
                    arc_t = arc.t_at_dist(dist_remaining)
                    break

            pos = current_arc.calc(arc_t)
            dist += vel * dt

            trajectory.append(Step(pos, vel, 0))
            vel = profile.v_at_d(dist)

        trajectory.append(Step(arcs[-1].calc(1), 0, 0))
        return trajectory
