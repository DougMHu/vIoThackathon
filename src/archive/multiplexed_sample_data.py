import time
from gpiozero import LED
from sample_calibrated_data import writeCalibratedSamples
from sample_data import writeSamples

##################
# Input parameters 
##################
calibrated = True
calibration_file = "../data/calibrated/riverside_03-25-17.csv"
output_file = "../data/multiplexed/riverside_03-25-17.csv"
num_samples = 100
freq = 10
pins = [23, 24]

############################
# Begin multiplexed sampling
############################

magnetometers = [LED(x) for x in pins]
for magnetometer in magnetometers:
    print(magnetometer)

for magnetometer in magnetometers:
    magnetometer.on()
    while not magnetometer.is_lit:
        print("waiting for %r to turn on..." % magnetometer)
        time.sleep(0.1)
    print("Turned %r on" % magnetometer)
    time.sleep(5)
    if calibrated:
        infile = open("%s_mag%d%s" % (calibration_file[:-4], magnetometer.pin.number, calibration_file[-4:]), 'r')
        outfile = open("%s_mag%d%s" % (output_file[:-4], magnetometer.pin.number, output_file[-4:]), 'w')
        measurement = writeCalibratedSamples(num_samples, freq, infile, outfile)
    else:
        outfile = open("%s_mag%d%s" % (calibration_file[:-4], magnetometer.pin.number, calibration_file[-4:]), 'w')
        measurement = writeSamples(num_samples, freq, outfile)
    magnetometer.off()
    while magnetometer.is_lit:
        print("waiting for %r to turn off" % magnetometer)
        time.sleep(0.1)
    print(measurement)
    time.sleep(5)
