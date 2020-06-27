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

    dist = profile.v_at_t(dt) * dt
    t = 0
    theta = path.calc(0).theta
    while dist <= length and t < 1.0:
        pos = path.calc(t)
        curvature = path.curvature(t)

        vel = profile.v_at_d(dist)
        vel = np.min([vel, bot.max_lin_vel_at_curvature(curvature)])

        t_n = path.t_at_dist_travelled(t, vel * dt)

        pos_new = path.calc(t_n)
        angular_vel = (pos_new.theta - theta) / dt
        theta += angular_vel * dt

        vel = np.min([vel, bot.max_lin_vel_at_angular_vel(angular_vel)])

        d_dist = vel * dt
        t = path.t_at_dist_travelled(t, d_dist)
        dist += d_dist

        trajectory.append(Step(pos, vel, angular_vel, curvature))

    # find wheel speeds
    lin_vel = np.array([step.v for step in trajectory])
    ang_vel = np.array([step.w for step in trajectory])
    left = lin_vel - (ang_vel * bot.track) / 2
    right = lin_vel + (ang_vel * bot.track) / 2

    return trajectory, profile, length, dt, (left, right)
