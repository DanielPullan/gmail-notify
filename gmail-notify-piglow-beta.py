## Author: Daniel Pullan
## Github: GitHub.com/DanielPullan
## Website: DanielPullan.co.uk

## imports  
from PyGlow import PyGlow
import pygame
from time import sleep
import feedparser

## initialises
## global variables for pyglow
pyglow = PyGlow()
b = 100
s = 1000
pyglow = PyGlow(brightness=int(b), speed=int(s), pulse=True)
pyglow.all(0)

## messages for setup
print "Please remember to have your Google account setup to allow login from non-secure sources."

## variables
username = raw_input("Your gmail username is: ")
password = raw_input ("Your password is: ")
mail = int(feedparser.parse("https://" + username + ":" + password +
"@mail.google.com/gmail/feed/atom/")["feed"] ["fullcount"])

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