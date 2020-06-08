from generator.trapezoidal import Trapezoidal
from path.arc import *


class Step:
    def __init__(self, point, v, w, curvature, curvature_lerp):
        self.point = point
        self.v = v
        self.w = w
        self.curvature = curvature
        self.curvature_lerp = curvature_lerp


def generate(*, bot, path, dt, arc_num):
    arcs = fit_arcs(path, arc_num).arr
    length = sum(a.length() for a in arcs)
    profile = Trapezoidal(bot, length)

    trajectory = []

    dist = profile.v_at_t(dt) * dt
    while dist <= length:
        i, arc, t = arc_t_at_dist(arcs, dist)
        pos = arc.calc(t)

        curvature = arc.curvature()
        curvature_lerp = interpolate_curvature(arcs, i, t)

        vel = profile.v_at_d(dist)
        max_linear_vel = bot.max_lin_vel_at_curvature(curvature_lerp)

        vel = np.min([vel, max_linear_vel])
        angular_vel = vel * curvature_lerp

        dist += vel * dt
        trajectory.append(Step(pos, vel, angular_vel, curvature, curvature_lerp))

    # last step is 0
    # trajectory.append(Step(arcs[-1].calc(1), 0, 0, 0))

    # find wheel speeds
    lin_vel = np.array([step.v for step in trajectory])
    ang_vel = np.array([step.w for step in trajectory])
    left = lin_vel - (ang_vel * bot.track) / 2
    right = lin_vel + (ang_vel * bot.track) / 2

    return trajectory, profile, length, arcs, dt, (left, right)
