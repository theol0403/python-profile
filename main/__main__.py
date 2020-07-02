from path.bezier import *
from path.hermite import *
from path.line import *
from path.point import Point
from generator.bot import Bot
from generator.generator import generate
from pint import UnitRegistry

u = UnitRegistry()
track = (11 * u.inch).to(u.meter).m
diam = (4 * u.inch).to(u.meter).m
weight = (20 * u.pounds).to(u.kilogram).m

# path = new_bezier([Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0)])
path = new_bezier([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)])
# path = new_bezier(
#     [
#         Point(1.0, 0.0),
#         Point(0.6, 0.0),
#         Point(1.0, 1.0),
#         Point(0.0, 0.6),
#         Point(0.0, 1.0),
#     ]
# )
# path = new_hermite(QuinticHermite, Point(0, 0, 0), Point(1, 1, 0))
# path = Line(Point(0, 0), Point(1, 0))
# path = new_bezier([Point(0, 1), Point(0.851, 0), Point(0.5, 1)])
# path = new_bezier([Point(0, 1), Point(2, 0), Point(0.5, 1)])


# define bot
bot = Bot(track=track, pose=path.calc(0))
bot.set_theoretical_maxes(weight, 200, diam, 4)

# generate the profile
trajectory, profile, length, dt, wheel_speeds = generate(bot=bot, path=path, dt=0.01)

# run the bot through all the steps
states = bot.simulate(np.array(wheel_speeds), dt)

pos_err = bot.pose.dist(path.calc(1)) * 1000
coord_err = (bot.pose - path.calc(1)) * 1000
ang_err = (bot.pose.theta - path.calc(1).theta) * 180 / np.pi

print(f"Velocity: {bot.max_vel:.4} m/s")
print(f"Acceleration: {bot.max_accel:.4} m/s2")
print(f"Angular Velocity: {bot.max_ang_vel*180/np.pi:.4} deg/s")
print("")
print(f"Length: {length:.4} m")
print(f"Time: {len(trajectory)*dt:.4} s")
print("")
print(f"Position error: {pos_err:.5} mm")
print(f"X error: {coord_err.x:.3} mm")
print(f"Y error: {coord_err.y:.3} mm")
print(f"Angle error: {ang_err:.5} degrees")
