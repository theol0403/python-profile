from path.point import Point
import math
import numpy as np

class Bot:
    def __init__(self, wheel_track, orientation):
        self.wheel_track = wheel_track
        self.orientation = orientation

    @staticmethod
    def default15():
        return Bot(14, Point.origin())
    
    @staticmethod
    def default18():
        return Bot(17, Point.origin())

    @staticmethod
    def default24():
        return Bot(23, Point.origin())

    #http://www.cs.columbia.edu/~allen/F15/NOTES/icckinematics.pdf
    #errors if wheeltrack == 0
    def move(self, left_vel, right_vel, dt):
        # signed distance from the instantaneous center of curvature (ICC)
        r = 0

        # angular velocity
        ang_vel = 0

        #edge cases
        if left_vel == right_vel:
            r = np.Infinity
        elif left_vel == -right_vel:
            r = 0
        elif left_vel == 0 or right_vel == 0:
            r = self.wheel_track/2
        else:
            r = (self.wheel_track/2)*((left_vel + right_vel)/(right_vel - left_vel))
            ang_vel = (right_vel - left_vel)/self.wheel_track



        icc = Point(self.orientation.x - r * math.sin(self.orientation.theta), self.orientation.y + r * math.cos(self.orientation.theta))

        new_x = math.cos(ang_vel * dt) * (self.orientation.x - icc.x) - math.sin(ang_vel * dt) * (self.orientation.y - icc.y) + icc.x
        new_y = math.sin(ang_vel * dt) * (self.orientation.x - icc.x) + math.cos(ang_vel * dt) * (self.orientation.y - icc.y) + icc.y
        new_theta = self.orientation.theta + ang_vel * dt 

        self.orientation = Point(new_x, new_y, new_theta)
