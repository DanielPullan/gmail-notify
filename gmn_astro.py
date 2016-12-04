## Author: Daniel Pullan
## Github: GitHub.com/DanielPullan
## Website: DanielPullan.co.uk
## Device: Pimoroni PiGlow

from piglow import PiGlow
from time import sleep
import login
from login import mail

## Init the current device
piglow = PiGlow()

## Device parameters
piglow.all(0)

if mail == 0:
        print "no mail"
        piglow.all(0)
        sleep(0.5)
elif mail < 5:
        print "mail count low"
        piglow.arm1(10)
        sleep(0.5)
elif mail < 10:
        print "mail count medium"
        piglow.arm1(10)
        piglow.arm2(10)
        sleep(0.5)
elif mail < 15:
        print "mail count high"
        piglow.arm1(10)
        piglow.arm2(10)
        piglow.arm3(10)
        sleep(0.5)
else:
        print "too many emails"
        for x in range(0, 10):
                piglow.all(100)
                sleep(0.5)
