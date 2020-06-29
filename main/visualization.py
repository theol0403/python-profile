from main.__main__ import *
import matplotlib.pyplot as plt

# x axis for time-based plots
time_range = np.linspace(0, len(trajectory) * dt, len(trajectory))

# path
plt.subplot(2, 3, 1)
plt.title("Path")

path.plot("Path")
x = [step.point.x for step in trajectory]
y = [step.point.y for step in trajectory]
plt.plot(x, y, label="Trajectory")

# plt.grid() # grid in path.plot
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.legend()

# angle
plt.subplot(2, 3, 2)
plt.title("Angle")

a = [step.point.theta * 180 / np.pi for step in trajectory]
plt.plot(time_range, a)

plt.xlabel("Time (s)")
plt.ylabel("Degrees")
plt.grid()

# curvature
plt.subplot(2, 3, 3)
plt.title("Curvature")

c = [step.curvature for step in trajectory]
plt.plot(time_range, c)

plt.xlabel("Time (s)")
plt.ylabel("Curvature (1/r)")
plt.grid()

# velocity
plt.subplot(2, 3, 4)
plt.title("Velocity")

v = [step.p_vel for step in trajectory]
plt.plot(time_range, v, label="Raw")
v = [step.v for step in trajectory]
plt.plot(time_range, v, label="Limited")

plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid()
plt.legend()

# angular velocity
plt.subplot(2, 3, 5)
plt.title("Angular Velocity")

w = [step.w for step in trajectory]
plt.plot(time_range, w)

plt.xlabel("Time (s)")
plt.ylabel("Angular Velocity (rad/s)")
plt.grid()

# wheel speeds
plt.subplot(2, 3, 6)
plt.title("Wheel Speeds")

plt.plot(time_range, wheel_speeds[0], label="Left")
plt.plot(time_range, wheel_speeds[1], label="Right")

plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid()
plt.legend()

plt.gcf().set_tight_layout(True)
plt.show()
