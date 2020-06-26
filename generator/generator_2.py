from generator.trapezoidal import Trapezoidal
from path.arc import Interpolator
from path.arc import *


class Step:
    def __init__(self, point, v, w, curvature):
        self.point = point
        self.v = v
        self.w = w
        self.curvature = curvature


def generate(*, bot, path, dt):
    length = path.length()
    profile = Trapezoidal(bot, length)

    trajectory = []

    dist = profile.v_at_t(dt) * dt
    t = 0.0001
    while dist <= length:
        pos = path.calc(t)

        curvature = path.curvature(t)

        vel = profile.v_at_d(dist)
        max_linear_vel = bot.max_lin_vel_at_curvature(curvature)

        vel = np.min([vel, max_linear_vel])
        angular_vel = vel * curvature

        d_dist = vel * dt
        dist += d_dist
        t = path.t_at_dist_travelled(t, d_dist)
        trajectory.append(Step(pos, vel, angular_vel, curvature))

    # last step is 0
    # trajectory.append(Step(arcs[-1].calc(1), 0, 0, 0))

    # find wheel speeds
    lin_vel = np.array([step.v for step in trajectory])
    ang_vel = np.array([step.w for step in trajectory])
    left = lin_vel - (ang_vel * bot.track) / 2
    right = lin_vel + (ang_vel * bot.track) / 2

    return trajectory, profile, length, dt, (left, right)
