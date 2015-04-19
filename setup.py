################## ##################
##Lucky it's A#### ##Gmail###########
##Family Py!###### #######Notify#####
################## ##################

## Author: Daniel Pullan
## Twitter: @soundsarenoisy
## Github: /soundsarenoisy

## This is the setup file. You input your board type and gmail details here.
## It's only going to be a CLI setup since you can then set it up whilst remoted in via Putty or something.


## imports
import time
import feedparser


## Setup email details.
print "let's login to gmail!"


## to import this into the board scripts type:
##  from setup.py import username
##  from setup.py import password
##  from setup.py import mail

## global variables for gmail
username = raw_input("What is your gmail address? (x@gmail.com) ")
password = raw_input ("What is your gmail password? ")
mail = int(feedparser.parse("https://" + username + ":" + password +
"@mail.google.com/gmail/feed/atom/")["feed"] ["fullcount"])

print "details done!"

## future: work out a way of choosing from numbers. 1 = pyglow, 2 = raw edition etc
## then do the whole if, elif, else to do specfic setup. (ex. if pyglow: brightness = raw_input ("from 1-100, how bright do you want your LEDs") etc.

board= raw_input("What board are you using today? ")


