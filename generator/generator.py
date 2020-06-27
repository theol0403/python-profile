from generator.trapezoidal import Trapezoidal
import numpy as np


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

    t = 0
    vel = profile.v_at_t(dt)
    pos = path.calc(t)
    theta = pos.theta
    curvature = path.curvature(t)
    dist = 0

    while dist <= length and t < 1.0:
        d_dist = vel * dt
        dist += d_dist
        vel = profile.v_at_d(dist)

        t = path.t_at_dist_travelled(t, d_dist)
        pos_new = path.calc(t)
        curvature = path.curvature(t)

        angular_vel = (pos_new.theta - theta) / dt
        theta += angular_vel * dt
        vel = np.min([vel, bot.max_lin_vel_at_angular_vel(angular_vel)])

        trajectory.append(Step(pos, vel, angular_vel, curvature))
        pos = pos_new

    # find wheel speeds
    lin_vel = np.array([step.v for step in trajectory])
    ang_vel = np.array([step.w for step in trajectory])
    left = lin_vel - (ang_vel * bot.track) / 2
    right = lin_vel + (ang_vel * bot.track) / 2

    return trajectory, profile, length, dt, (left, right)
