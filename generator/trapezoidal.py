import numpy as np


class Trapezoidal:
    def __init__(self, accel, vel, length):
        self.accel = accel
        self.vel = vel
        self.length = length

        # the time it takes to accelerate to full speed
        self.t_accel = vel / accel
        # the time spent cruising at full speed
        self.t_cruise = (length - self.t_accel * vel) / vel
        # if cruise time is negative, time needs to be shaved off the acceleration
        # this is now a triangular profile
        if self.t_cruise < 0:
            self.t_accel += self.t_cruise / 2
            self.t_cruise = 0

        # maximum attainable speed given time constraints (if triangular)
        self.top_vel = accel * self.t_accel
        # the time it takes to complete the profile
        self.time = self.t_accel * 2 + self.t_cruise

        # the distance spent accelerate to full speed
        self.d_accel = 0.5 * accel * (self.t_accel ** 2)
        # the distance spent at full speed
        self.d_cruise = self.top_vel * self.t_cruise

    def v_at_t(self, t):
        if t <= self.t_accel:
            # acceleleration
            return self.accel * t
        elif t > self.t_accel and t < self.t_accel + self.t_cruise:
            # cruising
            return self.top_vel
        else:
            # deceleration
            return self.top_vel - (t - self.t_accel - self.t_cruise) * self.accel

    def v_at_d(self, d):
        if d <= self.d_accel:
            # acceleleration
            return np.sqrt(2 * self.accel * d)
        elif d > self.d_accel and d < self.length - self.d_accel:
            # cruising
            return self.top_vel
        else:
            # deceleration
            d_from_decel = d - self.d_accel - self.d_cruise
            return np.sqrt(self.top_vel ** 2 - 2 * self.accel * d_from_decel)
