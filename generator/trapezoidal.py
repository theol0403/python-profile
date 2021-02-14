import numpy as np


class Trapezoidal:
    def __init__(self, limits, length, *, start_vel=0, end_vel=0):
        self.limits = limits
        self.length = length
        self.start_vel = start_vel
        self.end_vel = end_vel

        accel = self.limits.max_accel
        vel = self.limits.max_vel

        # the time it takes to accelerate to full speed
        self.t_accel = (vel - start_vel) / accel
        self.t_decel = (vel - end_vel) / accel
        # the distance it could travel while accelerating
        self.d_accel = start_vel * self.t_accel + 0.5 * accel * (self.t_accel ** 2)
        self.d_decel = vel * self.t_decel - 0.5 * accel * (self.t_decel ** 2)
        # the time spent cruising at full speed
        self.t_cruise = (length - self.d_accel - self.d_decel) / vel

        # if cruise time is negative, time needs to be shaved off the acceleration
        if self.t_cruise < 0:
            # this is a triangular profile
            self.t_cruise = 0
            # maximum attainable speed given time constraints (if triangular)
            # self.top_vel = np.sqrt(length * accel)
            self.top_vel = np.sqrt(accel * length + (start_vel ** 2 + end_vel ** 2) / 2)
            # time to accelerate to max speed
            self.t_accel = (self.top_vel - start_vel) / accel
            self.t_decel = (self.top_vel - end_vel) / accel
            if self.t_accel < 0 or self.t_decel < 0:
                raise ("Bad")
        else:
            # this is not a triangular profile
            self.top_vel = vel

        # the time it takes to complete the profile
        self.time = self.t_accel + self.t_decel + self.t_cruise

        # the distance to accelerate to full speed
        self.d_accel = start_vel * self.t_accel + 0.5 * accel * (self.t_accel ** 2)
        self.d_decel = vel * self.t_decel - 0.5 * accel * (self.t_decel ** 2)
        # the distance to cruise
        self.d_cruise = self.top_vel * self.t_cruise

    def v_at_t(self, t):
        # prevent decel below 0
        if t > self.time:
            t = self.time
        if t <= self.t_accel:
            # acceleleration
            return self.start_vel + self.limits.max_accel * t
        elif t > self.t_accel and t < self.t_accel + self.t_cruise:
            # cruising
            return self.top_vel
        else:
            # deceleration
            return (
                self.top_vel
                - (t - self.t_accel - self.t_cruise) * self.limits.max_accel
            )

    def v_at_d(self, d):
        if d <= self.d_accel:
            # acceleleration
            return np.sqrt(2 * self.limits.max_accel * d)
        elif d > self.d_accel and d < self.length - self.d_accel:
            # cruising
            return self.top_vel
        else:
            # deceleration
            d_from_decel = d - self.d_accel - self.d_cruise
            v_2 = self.top_vel ** 2 - 2 * self.limits.max_accel * d_from_decel
            if v_2 < 0:
                return 0
            else:
                return np.sqrt(v_2)
