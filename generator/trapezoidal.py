import numpy as np


class Trapezoidal:
    def __init__(self, accel, vel, length):
        self.accel = accel
        self.vel = vel
        self.length = length

        # the distance it takes to accelerate from 0 to full vel
        a_dist = (vel**2)/(2*accel)
        # the cruising at max vel distance
        c_dist = length - a_dist * 2
        # if cruise is negative, acceleration is too long and this is a triangular profile
        if c_dist < 0:
            a_dist += c_dist/2
            c_dist = 0

        self.a_dist = a_dist
        self.c_dist = c_dist
        self.top_vel = np.sqrt(2 * accel * a_dist)

    def calc_at_d(self, d):
        if d < 0 or d > self.length:
            print(f"Bad d: {d}")

        vel = 0
        if d <= self.a_dist:
            # we are accelerating
            vel = np.sqrt(2 * self.accel * d)
        elif d > self.a_dist and d < self.length - self.a_dist:
            # we are cruising
            vel = self.top_vel
        else:
            # we are decelerating
            vel = np.sqrt(self.top_vel**2 - 2 * self.accel *
                          (d - self.a_dist - self.c_dist))

        return vel
