from generator.trapezoidal import Trapezoidal
import numpy as np


class Step:
    def __init__(self, point, v, w, curvature, p_vel):
        self.point = point
        self.v = v
        self.w = w
        self.curvature = curvature
        self.p_vel = p_vel


def generate(*, bot, path, dt):
    length = path.length()
    profile = Trapezoidal(bot, length)

    trajectory = []

    # set up the state at the beginning of the trajectory
    t = 0
    dist = 0
    pos = path.calc(t)
    vel = profile.v_at_t(dt)
    while dist <= length and t <= 1.0:
        p_vel = vel
        # limit velocity according to approximation of the curvature during the next timeslice
        curvature = path.curvature(t)
        vel_max = np.min([vel, bot.max_lin_vel_at_curvature(curvature)])
        # project where along the path we will be after dt, given approximate velocity
        t_n = path.t_at_dist_travelled(t, vel_max * dt)
        pos_new = path.calc(t_n)

        # find out how fast we need to turn to achieve change in theta to reach next point in dt
        angular_vel = (pos_new.theta - pos.theta) / dt
        # limit profiled velocity to angular velocity
        vel = np.min([vel, bot.max_lin_vel_at_angular_vel(angular_vel)])

        # calculate distance traveled
        d_dist = vel * dt
        dist += d_dist
        # calculate where along the path we will be at the end of the timeslice
        t = path.t_at_dist_travelled(t, d_dist)

        # save trajectory
        trajectory.append(Step(pos, vel, angular_vel, curvature, p_vel))

        # update new position
        pos = pos_new
        # calculate new velocity
        vel = profile.v_at_d(dist)

    # find wheel speeds
    lin_vel = np.array([step.v for step in trajectory])
    ang_vel = np.array([step.w for step in trajectory])
    left = lin_vel - (ang_vel * bot.track) / 2
    right = lin_vel + (ang_vel * bot.track) / 2

    return trajectory, profile, length, dt, (left, right)
