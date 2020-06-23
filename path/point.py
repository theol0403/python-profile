import numpy as np


class Point:
    def __init__(self, x, y, theta=0):
        self.x = x
        self.y = y
        self.theta = theta

    @staticmethod
    def origin():
        return Point(0, 0, 0)

    def dist(self, other):
        return np.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def angle_to(self, other):
        diff = other - self
        return np.arctan2(diff.y, diff.x)

    # used for simulation
    @staticmethod
    def from_array(arr):
        return Point(arr[0], arr[1], arr[2])

    # used for simulation
    def to_np_array(self, arr):
        return np.array((self.x, self.y, self.theta))

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.theta + other.theta)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.theta - other.theta)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other, self.theta * other)

    def __div__(self, other):
        return Point(self.x / other, self.y / other, self.theta / other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.theta == other.theta

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.theta) + ")"
