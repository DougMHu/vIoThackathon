Wakaama (formerly liblwm2m) is an implementation of the Open Mobile Alliance's LightWeight M2M
protocol (LWM2M).

Dependency : wiringPi
** how to install  - http://wiringpi.com/download-and-install/
** answer Y for all questions asked by installer
** ex Do you want to continue? [Y/n] y

sudo apt-get purge wiringpi
hash -r
sudo apt-get install git-core
* ignore the following message and go to next step
* git-core is already the newest version.

sudo apt-get update
sudo apt-get upgrade
cd
git clone git://git.drogon.net/wiringPi
cd ~/wiringPi
git pull origin
./build

Test wiringPi installation
--------------------------

run the gpio command to check the installation:

 gpio -v
 gpio readall

** you will see following output (pi2/pi3)
pi@attsws01:~/wiringPi $ gpio readall
 +-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 | ALT0 | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 | ALT0 | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI | ALT0 | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO | ALT0 | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK | ALT0 | 0 | 23 || 24 | 1 | OUT  | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | OUT  | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |   IN | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+

Compiling Wakaama
-----------------

download wakaama.tar

install cmake 
-------------
sudo apt-get install cmake

### Test client example
cd wakaama

cmake .

* Create a build directory and change to that.

cd examples/client
cmake .
-- Check if the system is big endian
-- Searching 16 bit integer
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of unsigned short
-- Check size of unsigned short - done
-- Using unsigned short
-- Check if the system is big endian - little endian
-- Configuring done
-- Generating done
-- Build files have been written to: /home/pi/wakaama


 * ``make``
 * ``./lwm2mclient [Options]``


Options are:
- -n NAME	Set the endpoint name of the Client. Default: testlwm2mclient
- -l PORT	Set the local UDP port of the Client. Default: 56830
- -h HOST	Set the hostname of the LWM2M Server to connect to. Default: localhost
- -p HOST	Set the port of the LWM2M Server to connect to. Default: 5683
- -4		Use IPv4 connection. Default: IPv6 connection
- -t TIME	Set the lifetime of the Client. Default: 300
- -b		Bootstrap requested.
- -c		Change battery level over time.
  
***
If you want to run your own server
1. you need jdk1.8
2. download leshan-server-demo-0.1.11-M14-SNAPSHOT-jar-with-dependencies.jar
3. execure 
nohup java -jar leshan-server-demo-0.1.11-M14-SNAPSHOT-jar-with-dependencies.jar &

To launch a cliet session:
ex demoClient
sudo nohup ./lwm2mclient -4 -n demoClient -h 135.213.190.106 &

check your registered client on server (using browser)
http://135.213.190.106:8080/#/clients/demoClient

