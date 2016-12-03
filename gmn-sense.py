## Author: Daniel Pullan
## Github: GitHub.com/DanielPullan
## Website: DanielPullan.co.uk
## Device: Pi 3 with Sense HAT / AstroPi

from colorsys import hsv_to_rgb
from time import sleep
from sense_emu import SenseHat
from pyglow import PyGlow
import pygame
import time
import feedparser


# this bit is very import-ant.
from sense_emu import SenseHat

# starting up the hat
sense = SenseHat()

# set colours
red = (255, 0, 0)
green = (0, 255, 0) 
blue = (0, 0, 255) 

# time for my code to shine 
username = raw_input("Gmail address: ")
password = raw_input("Password: ")
mail = int(feedparser.parse("https://" + username + ":" + password +
"@mail.google.com/gmail/feed/atom/")["feed"] ["fullcount"])
mail2 = ("You have " + str(mail) + " messages")

# 1st pixel is 0.
# X, Y, Colour
sense.set_pixel(1, 0, red)
sense.set_pixel(2, 0, green)
sense.set_pixel(3, 0, blue)
