
class Path:
    def calc(self, t):
        pass

    def interpolate(self, steps):
        return [self.calc(i / steps) for i in range(steps)]
