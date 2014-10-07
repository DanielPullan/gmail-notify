##################
##Lucky it's A####
##Family Py!######
##################

## Author: Daniel Pullan
## Twitter: @soundsarenoisy
## Github: /soundsarenoisy


## imports
from pyglow import PyGlow
import pygame
import time
import feedparser

## global variables for gmail
username = "EMAIL@gmail.com"
password = "PASSWORD"
mail = int(feedparser.parse("https://" + username + ":" + password +
"@mail.google.com/gmail/feed/atom/")["feed"] ["fullcount"])
contact = int(feedparser.parse("https://" + username + ":" + password +
"@mail.google.com/gmail/feed/atom/LABEL-NAME")["feed"] ["fullcount"])

## global variables for pyglow
pyglow = PyGlow()
pygame.mixer.init()
number = 0
val = 100
speedval = 90

if mail > 0 and \
contact > 0:
        pyglow.all(0)
        pyglow.pulse(1, 100, speedval)
        print('Item has sold!')

elif mail > 4:
        pyglow.all(0)
        pyglow.pulse(2, 100, speedval)
        print('You have too many messages in your inbox')

elif mail > 0:
        pyglow.all(0)
        pyglow.pulse(3, 100, speedval)
        print ('You have a message in your inbox')

else:
        pyglow.all(0)
        pyglow.pulse(4, 100, speedval)
        print ('Nope, no mail yet!')
