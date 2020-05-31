import numpy as np


class Trapezoidal:
    def __init__(self, accel, vel, length):
        self.accel = accel
        self.vel = vel
        self.length = length

        self.t_accel = vel / accel
        self.t_cruise = (length - self.t_accel * vel) / vel

        if self.t_cruise < 0:
            self.t_accel += self.t_cruise / 2
            self.t_cruise = 0

        self.top_vel = accel * self.t_accel
        self.time = self.t_accel * 2 + self.t_cruise

        self.d_accel = 0.5 * accel * (self.t_accel ** 2)
        self.d_cruise = self.top_vel * self.t_cruise

    def v_at_t(self, t):
        if t <= self.t_accel:
            return self.accel * t
        elif t > self.t_accel and t < self.t_accel + self.t_cruise:
            return self.top_vel
        else:
            return self.top_vel - (t - self.t_accel - self.t_cruise) * self.accel

    def v_at_d(self, d):
        if d <= self.d_accel:
            return np.sqrt(2 * self.accel * d)
        elif d > self.d_accel and d < self.length - self.d_accel:
            return self.top_vel
        else:
            d_from_decel = d - self.d_accel - self.d_cruise
            return np.sqrt(self.top_vel ** 2 - 2 * self.accel * d_from_decel)
