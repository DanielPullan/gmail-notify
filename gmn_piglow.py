## Author: Daniel Pullan
## Github: GitHub.com/DanielPullan
## Website: DanielPullan.co.uk
## Device: Pimoroni PiGlow

from PyGlow import PyGlow
import pygame
from time import sleep
import feedparser
from login import login

## Init the current device
pyglow = PyGlow()

## Device parameters
b = 100
s = 1000
pyglow = PyGlow(brightness=int(b), speed=int(s), pulse=True)
pyglow.all(0)

if mail < 5:
        print "mail count low"
        pyglow.arm1(10)
elif mail < 10:
        print "mail count medium"
        pyglow.arm1(10)
        pyglow.arm2(10)
elif mail < 15:
        print "mail count high"
        pyglow.arm1(10)
        pyglow.arm2(10)
        piglow.arm3(10)
else:
        print "too many emails"
        for x in range(0, 10):
                pyglow.all(100)
                sleep(0.5)