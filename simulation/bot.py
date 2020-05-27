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

    #http://www.cs.columbia.edu/~allen/F15/NOTES/icckinematics.pdf
    def move(left_vel, right_vel):

        # signed distance from the instantaneous center of curvature (ICC)
        r = (self.wheel_track/2)*((left_vel + right_vel)/(right_vel - left_vel))
        # angular velocity
        ang_vel = (right_vel - left_vel)/self.wheel_track

        self.orientation = self.orientation
