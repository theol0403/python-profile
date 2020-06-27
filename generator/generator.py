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
    pos = path.calc(0)
    theta = pos.theta
    curvature = path.curvature(0)
    vel = profile.v_at_t(dt)
    dist = 0
    while dist <= length and t < 1.0:
        t_n = path.t_at_dist_travelled(t, vel * dt)
        pos_new = path.calc(t_n)
        angular_vel = (pos_new.theta - pos.theta) / dt
        vel = np.min([vel, bot.max_lin_vel_at_angular_vel(angular_vel)])

        d_dist = vel * dt
        t = path.t_at_dist_travelled(t, d_dist)
        dist += d_dist

        trajectory.append(Step(pos, vel, angular_vel, curvature))

        pos = pos_new
        vel = profile.v_at_d(dist)
        curvature = path.curvature(t)
        vel = np.min([vel, bot.max_lin_vel_at_curvature(curvature)])

    # find wheel speeds
    lin_vel = np.array([step.v for step in trajectory])
    ang_vel = np.array([step.w for step in trajectory])
    left = lin_vel - (ang_vel * bot.track) / 2
    right = lin_vel + (ang_vel * bot.track) / 2

    return trajectory, profile, length, dt, (left, right)
