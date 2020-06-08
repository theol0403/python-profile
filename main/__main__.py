from path.functions import *
from path.point import Point
from generator.bot import Bot
from generator.generator import generate
from pint import UnitRegistry

u = UnitRegistry()
track = (11 * u.inch).to(u.meter).m
diam = (4 * u.inch).to(u.meter).m
weight = (20 * u.pounds).to(u.kilogram).m

path = new_bezier([Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0)])
# path = new_bezier([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)])

# define bot
bot = Bot(track=track, pose=path.calc(0))
bot.set_theoretical_maxes(weight, 200, diam, 4)

# generate the profile
trajectory, profile, length, arcs, dt, wheel_speeds = generate(
    bot=bot, path=path, dt=0.01, arc_num=50
)

# run the bot through all the steps
states = bot.simulate(np.array(wheel_speeds), dt)

pos_err = bot.pose.dist(path.calc(1))
ang_err = (bot.pose.theta - path.calc(1).theta) * 180 / np.pi

print(f"Velocity: {bot.max_vel:.04}")
print(f"Acceleration: {bot.max_accel:.04}")
print(f"Angular Velocity: {bot.max_ang_vel*180/np.pi:.04}")
print("")
print(f"Length: {length:.04}")
print(f"Time: {len(trajectory)*dt:.04}")
print("")
print(f"Position error: {pos_err:.05} meters")
print(f"Angle error: {ang_err:.05} degrees")