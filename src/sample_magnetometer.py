from Magnetometer import Magnetometer

mag = Magnetometer(24)
mag.turnOn()
x, y, z = mag.takeSample()
print("%f\n%f" % (x, y))
