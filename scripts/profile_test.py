from generator.trapezoidal import Trapezoidal
import matplotlib.pyplot as plt


profile = Trapezoidal(5, 5, 10)

x = [d/10 for d in range(101)]
y = [profile.calc_at_d(d) for d in x]

plt.plot(x, y)
plt.title("Vel vs Distance")
plt.grid()
plt.show()
