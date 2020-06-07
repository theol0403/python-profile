import unittest
from generator.bot import Bot
from generator.trapezoidal import Trapezoidal
import matplotlib.pyplot as plt
import numpy as np


class TestBotMethods(unittest.TestCase):

    def test_max_vels_from_scales(self):
        self.assertEqual(0, 0)


class TestDistanceProfile(unittest.TestCase):

    def test_max_negative_cruise(self):
        bot = Bot(track=1, max_vel=2, max_accel=1)
        profile = Trapezoidal(bot, 3)

        dt = 0.01
        x = np.arange(0, profile.time + dt, dt)
        vels = [profile.v_at_t(t) for t in x]
        self.assertAlmostEqual(np.sum(vels)*dt, 3, places=3)


if __name__ == '__main__':
    unittest.main()
