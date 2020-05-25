import numpy as np


class Point:

    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta

    def origin():
        return Point(0, 0, 0)

    def dist(self, other):
        return np.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def angle_to(self, other):
        diff = other - self
        return np.arctan2(diff.y, diff.x)

    def __add__(self, other):
        return Point(self.x + other.x,
                     self.y + other.y, self.theta + other.theta)

    def __sub__(self, other):
        return Point(self.x - other.x,
                     self.y - other.y, self.theta - other.theta)

    def __mul__(self, other):
        return Point(self.x * other.x,
                     self.y * other.y, self.theta * other.theta)

    def __div__(self, other):
        return Point(self.x / other.x,
                     self.y / other.y, self.theta / other.theta)

    def __eq__(self, other):
        return self.x == other.x \
            and self.y == other.y and self.theta == other.theta
