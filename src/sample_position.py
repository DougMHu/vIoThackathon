from Magnetometer import Magnetometer
# import numpy as np

# calibration file name must be consistent with sample_magnetometer's
calibration_file = "calibrate_corners.csv"

# Store calibration values in a dictionary
xmin = 0
xmax = 0.5
ymin = -0.5
ymax = 0.5
corners = [(xmin,ymin), (xmax,ymin), (xmin,ymax), (xmax,ymax)]
value = {}

def distance(a, b):
    diff = [i-j for i,j in zip(a, b)]
    dist = diff[0]**2 + diff[1]**2
    return dist

def closestCorner(meas):
    dist =[]
    for corner in corners:
        dist.append(distance(meas, value[corner]))
    newmin = 1e9
    index = 0
    for i in list(range(len(corners))):
        if dist[i] < newmin:
            newmin = dist[i]
            index = i
    # index = np.argmin(dist)
    return corners[index]

def xDisplacement(meas):
    slope = xmax/(value[(xmax,ymin)][0] - value[(xmin, ymin)][0]) 
    return slope*(meas[0] - value[(xmin, ymin)][0])

def yDisplacement(meas):
    slope = ymax/(value[(xmin,ymax)][1] - value[(xmin, ymin)][1]) 
    return slope*(meas[1] - value[(xmin, ymin)][1])

# Initialize and turn on magnetometer
mag = Magnetometer(24)
mag.turnOn()

# Read calibration file
with open(calibration_file, 'r') as f:
    text = f.read()
    lines = text.split("\n")
    for j in list(range(len(corners))):
        value[corners[j]] = [float(i) for i in lines[j].split(',')]

# Take a magnetometer sample
x, y, z = mag.takeMedianSample()
meas = [x, y, z]
print(xDisplacement(meas))
print(yDisplacement(meas))
