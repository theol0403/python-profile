from path.point import Point
import numpy as np


class Bot:
    def __init__(
        self, *, track, max_vel=1, max_ang_vel=1, max_accel=1, pose=Point.origin()
    ):
        self.track = track
        self.max_vel = max_vel
        self.max_ang_vel = max_ang_vel
        self.max_accel = max_accel
        self.pose = pose

    def set_theoretical_maxes(self, weight, rpm, wheel_diam, num_motors):
        lin_vel, ang_vel = Bot.max_vels_from_scales(rpm, wheel_diam, self.track)
        self.max_vel = lin_vel
        self.max_ang_vel = ang_vel
        # v5 100rpm motors have 2.1Nm of torque at stall
        torque = (2.1 * num_motors * 0.15) / (rpm / 100.0)
        lin_force = torque / (wheel_diam / 2)
        self.max_accel = lin_force / weight

    @staticmethod
    def max_vels_from_scales(rpm, wheel_diam, track):
        lin_vel = rpm / 60.0 * wheel_diam * np.pi
        ang_vel = 2 * lin_vel / track
        return lin_vel, ang_vel

    def max_lin_vel_at_curvature(self, curvature):
        return (self.max_ang_vel * self.max_vel) / (
            np.abs(curvature) * self.max_vel + self.max_ang_vel
        )

    def max_lin_vel_at_angular_vel(self, angular_vel):
        return np.max(
            [self.max_vel - (self.max_vel * np.abs(angular_vel)) / self.max_ang_vel, 0]
        )
        # return self.max_vel * (1.0 - (np.abs(angular_vel) / self.max_ang_vel))

    # http://www.cs.columbia.edu/~allen/F15/NOTES/icckinematics.pdf
    # errors if wheeltrack == 0
    def move(self, left_vel, right_vel, dt):

        if (
            np.abs(left_vel) > self.max_vel + 1e-7
            or np.abs(right_vel) > self.max_vel + 1e-7
        ):
            print("Error: Wheel Saturation")

        if left_vel == right_vel:
            new_x = self.pose.x + np.cos(self.pose.theta) * left_vel * dt
            new_y = self.pose.y + np.sin(self.pose.theta) * left_vel * dt

            self.pose = Point(new_x, new_y, self.pose.theta)
            return self.pose

        # signed distance from the instantaneous center of curvature (ICC)
        r = 0

        # edge cases
        if left_vel == -right_vel:
            r = 0
        elif left_vel == 0 or right_vel == 0:
            r = self.track / 2
        else:
            r = (self.track / 2) * (left_vel + right_vel) / (right_vel - left_vel)

        ang_vel = (right_vel - left_vel) / self.track

        icc = Point(
            self.pose.x - r * np.sin(self.pose.theta),
            self.pose.y + r * np.cos(self.pose.theta),
        )

        new_x = (
            np.cos(ang_vel * dt) * (self.pose.x - icc.x)
            - np.sin(ang_vel * dt) * (self.pose.y - icc.y)
            + icc.x
        )

        new_y = (
            np.sin(ang_vel * dt) * (self.pose.x - icc.x)
            + np.cos(ang_vel * dt) * (self.pose.y - icc.y)
            + icc.y
        )

        new_theta = self.pose.theta + ang_vel * dt

        self.pose = Point(new_x, new_y, new_theta)
        return self.pose

    def simulate(self, vels, dt):
        states = []
        for i in range(len(vels[0])):
            states.append(self.move(vels[0][i], vels[1][i], dt))

        return states

    @staticmethod
    def default15(**kwargs):
        return Bot(track=14, **kwargs)

    @staticmethod
    def default18(**kwargs):
        return Bot(track=17, **kwargs)

    @staticmethod
    def default24(**kwargs):
        return Bot(track=23, **kwargs)

    # def rpm_to_linear_vel(self, rpm):
    #     return (rpm / 60.0) * self.gearing * self.wheel_diam * np.pi

    # def linear_vel_to_rpm(self, linear_vel):
    #     return (linear_vel * 60) / (self.gearing * self.wheel_diam * np.pi)
