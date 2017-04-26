from i2clibraries.i2c_hmc5883l import i2c_hmc5883l
import sys, time, argparse, logging, math
from gpiozero import OutputDevice
from statistics import median

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Magnetometer(object):

    lower_bound = 0.88  # (in Gauss) setting for highest resolution (lowest conversion factor)
    low_factor = 0.73   # corresponding conversion factor (mGauss / least significant bit) 
    factor = low_factor

    def __init__(self, pin, i2c_port=1):
        """
        Configures the GPIO pin powering the magnetometer.
        Initializes I2C communication to HMC5883L magnetometer. 
        """ 
        self.gpio = OutputDevice(pin)
        logger.info("Configured GPIO pin %d for magnetometer power" % pin)
        self.hmc = i2c_hmc5883l(i2c_port, gauss=self.lower_bound)
        logger.info("Initialized I2C communication at port %d" % i2c_port)

    def turnOn(self):
        self.gpio.on()
        logger.info("Turned on GPIO pin %d" % self.gpio.pin.number)

    def turnOff(self):
        self.gpio.off()
        logger.info("Turned off GPIO pin %d" % self.gpio.pin.number)

    def togglePower(self):
        self.gpio.toggle()
        if self.gpio.value:
            state = "on"
        else:
            state = "off"        
        logger.info("Turned %s GPIO pin %d" % (state, self.gpio.pin.number))

    def takeSample(self):
        """
        Samples x, y, z values from HMC5883L using single-measurement mode.
        Returns (x,y,z)
        """
        self.hmc.setSingleShotMode()
        self.hmc.setScale(self.lower_bound)  # initialize to highest resolution
        self.factor = self.low_factor
        # Flush out the first 5 samples (holding old samples)
        # time.sleep(0.1)
        x, y, z = self.hmc.getAxes()
        # If scale is not large enough, lower resolution
        while any([math.isnan(i) for i in (x,y,z)]):
            logger.info("Magnetic field is strong... Increasing digital scale (decreasing resolution)")
            new_factor = self.hmc.upScale()
            if new_factor:
                self.factor = new_factor
                x, y, z = self.hmc.getAxes()
            # If scale cannot increase further, give up but warn the user
            else:
                logger.warning("Magnetic field too strong! Caused digital overflow! Outputing NaN measurements.")
                break
        logger.info("Got x=%f, y=%f, z=%f, factor=%f" % (x, y, z, self.factor))
        xGauss, yGauss, zGauss = [self.factor*i for i in (x,y,z)] # convert to Gauss
        return (xGauss, yGauss, zGauss)

    def takeMedianSample(self, n=7, freq=7):
        xs = []
        ys = []
        zs = []
        for i in list(range(n)):
            x, y, z = self.takeSample()
            xs.append(x)
            ys.append(y)
            zs.append(z)
            time.sleep(1/freq)
        return (median(xs), median(ys), median(zs))
