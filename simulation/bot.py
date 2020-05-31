from path.point import Point
import numpy as np


class Bot:
    def __init__(self, *, track, max_vel, pose=Point.origin()):
        self.track = track
        self.max_vel = max_vel
        self.pose = pose

    # def rpm_to_linear_vel(self, rpm):
    #     return (rpm / 60.0) * self.gearing * self.wheel_diam * np.pi

    # def linear_vel_to_rpm(self, linear_vel):
    #     return (linear_vel * 60) / (self.gearing * self.wheel_diam * np.pi)

    # http://www.cs.columbia.edu/~allen/F15/NOTES/icckinematics.pdf
    # errors if wheeltrack == 0
    def move(self, left_vel, right_vel, dt):

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
    def default15():
        return Bot(track=14, max_vel=1)

    @staticmethod
    def default18():
        return Bot(track=17, max_vel=1)

    @staticmethod
    def default24():
        return Bot(track=23, max_vel=1)
