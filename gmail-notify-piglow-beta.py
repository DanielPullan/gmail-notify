## Author: Daniel Pullan
## Github: GitHub.com/DanielPullan
## Website: DanielPullan.co.uk

## imports  
from piglow import PiGlow
import pygame
import time
import feedparser

## TODO: migrate to PyGlow by benleb

## initialises
## global variables for pyglow
piglow = PiGlow()
pygame.mixer.init()
number = 0
val = 100
speedval = 90

## messages for setup
print "Please remember to have your Google account setup to allow login from non-secure sources."
print "I will look into fixing this in a future update."

## variables
username = raw_input("Your gmail username is: ")
password = raw_input ("Your password is: ")
mail = int(feedparser.parse("https://" + username + ":" + password +
"@mail.google.com/gmail/feed/atom/")["feed"] ["fullcount"])
mail2 = ("You have " + str(mail) + " messages")


b = input("Maximum brightness: ")
s = input("Speed in milliseconds (try 1000 as a default): ")

pyglow = PyGlow(brightness=int(b), speed=int(s), pulse=True)

pyglow.all(0)

if mail < 5:
	pyglow.arm1(10)
elif mail < 10:
	pyglow.arm1(10)
	pyglow.arm2(10)
elif mail < 15:
	pyglow.arm1(10)
	pyglow.arm2(10)
	piglow.arm3(10)
else:
	print "Uh oh"
	for x in range(0, 10):
		pyglow.all(100)
		sleep(0.5)