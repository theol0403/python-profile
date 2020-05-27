from path.point import Point

class Bot:
    def __init__(self, wheel_track, orientation):
        self.wheel_track = wheel_track
        self.orientation = orientation

    def default15():
        return Bot(14, Point.origin())
    
    def default18():
        return Bot(17, Point.origin())

    def default24():
        return Bot(23, Point.origin())

    def move(left_vel, right_vel):
        self.orientation = self.orientation
