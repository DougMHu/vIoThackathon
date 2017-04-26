from Magnetometer import Magnetometer

# calibration file name must be consistent with sample_magnetometer's
calibration_file = "calibrate_corners.csv"

# Initialize and turn on magnetometer
mag = Magnetometer(24)
mag.turnOn()

# Prompt user to place magnet at closest corner
input("Place magnet at closest corner, then press Enter")

x, y, z = mag.takeMedianSample()
with open(calibration_file, 'w') as f:
    f.write("%f,%f,%f\n" % (x, y, z))

# Prompt user to place magnet at 2nd closest corner
input("Place magnet at 2nd closest corner, then press Enter")
x, y, z = mag.takeMedianSample()
with open(calibration_file, 'a') as f:
    f.write("%f,%f,%f\n" % (x, y, z))

# Prompt user to place magnet at 2nd furthest corner
input("Place magnet at 2nd furthest corner, then press Enter")
x, y, z = mag.takeMedianSample()
with open(calibration_file, 'a') as f:
    f.write("%f,%f,%f\n" % (x, y, z))

# Prompt user to place magnet at furthest corner
input("Place magnet at furthest corner, then press Enter")
x, y, z = mag.takeMedianSample()
with open(calibration_file, 'a') as f:
    f.write("%f,%f,%f\n" % (x, y, z))
