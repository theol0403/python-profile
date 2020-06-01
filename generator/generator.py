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
        arcs = fit_arcs(path, arc_num)
        length = sum(a.length() for a in arcs.arr)
        profile = Trapezoidal(self.constraints, length)

        trajectory = []

        dist = 0
        vel = profile.v_at_t(dt)
        while dist <= length:

            current_arc, arc_t = 0, 0
            dist_remaining = dist
            for arc in arcs.arr:
                if dist_remaining > arc.length():
                    dist_remaining -= arc.length()
                else:
                    current_arc = arc
                    arc_t = arc.t_at_dist(dist_remaining)
                    break

            pos = current_arc.calc(arc_t)

            dist += vel * dt
            vel = profile.v_at_d(dist)

            trajectory.append(Step(pos, vel, 0))

        return []
