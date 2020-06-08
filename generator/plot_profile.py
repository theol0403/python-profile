import matplotlib.pyplot as plt
import numpy as np


def plot_profile(trajectory, path, dt, wheel_speeds):
    # x axis for time-based plots
    time_range = np.linspace(0, len(trajectory) * dt, len(trajectory))

    # path
    plt.subplot(2, 3, 1)
    plt.title("Path")

    path.plot("Path")
    x = [step.point.x for step in trajectory]
    y = [step.point.y for step in trajectory]
    plt.plot(x, y, label="Arcs")

    # plt.grid() # grid in path.plot
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.legend()

    # angle
    plt.subplot(2, 3, 2)
    plt.title("Angle")

    a = [step.point.theta * 180 / np.pi for step in trajectory]
    plt.plot(time_range, a, label="Arc Angle")

    plt.xlabel("Time (s)")
    plt.ylabel("Degrees")
    plt.grid()
    plt.legend()

    # curvature
    plt.subplot(2, 3, 3)
    plt.title("Curvature")

    c = [step.curvature for step in trajectory]
    plt.plot(time_range, c, label="Raw")

    c = [step.curvature_lerp for step in trajectory]
    plt.plot(time_range, c, label="Interpolated")

    plt.xlabel("Time (s)")
    plt.ylabel("Curvature (1/r)")
    plt.grid()
    plt.legend()

    # velocity
    plt.subplot(2, 3, 4)
    plt.title("Velocity")

    v = [step.v for step in trajectory]
    plt.plot(time_range, v)

    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.grid()

    # angular velocity
    plt.subplot(2, 3, 5)
    plt.title("Angular Velocity")

    w = [step.w * 180 / np.pi for step in trajectory]
    plt.plot(time_range, w)

    plt.xlabel("Time (s)")
    plt.ylabel("Angular Velocity (deg/s)")
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
