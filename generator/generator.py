from generator.trapezoidal import Trapezoidal
from path.arc import Arc


class Generator:
    def __init__(self, constraints, drive):
        self.constraints = constraints
        self.drive = drive

    def generate(self, *, path, dt, arcs):
        return []
