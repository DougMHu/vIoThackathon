from i2clibraries.i2c_hmc5883l import i2c_hmc5883l
import sys, time, argparse, logging
from gpiozero import OutputDevice

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Magnetometer(object):

    def __init__(self, pin, i2c_port=1):
        """
        Configures the GPIO pin powering the magnetometer.
        Initializes I2C communication to HMC5883L magnetometer. 
        """ 
        self.gpio = OutputDevice(pin)
        logger.info("Configured GPIO pin %d for magnetometer power" % pin)
        self.hmc = i2c_hmc5883l(i2c_port)
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
        x, y, z = hmc.getAxes()
        if any([math.isnan(i) for i in (x,y,z)]):
 

    def takeSamples(self, n=10, freq=5):
        pass
