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

## boards
## 1 = pyglow
## 2 = pi-liter
## 3 = ledborg
## 4 = raw edition
## 5 = unknown

if board = 1:
    ## chose piglow
    ## put in pyglow.py settings
    "You chose piglow."
    
    ## global variables for pyglow
    pyglow = PyGlow()
    pygame.mixer.init()
    ## wtf is this number variable. fuck.
    number = 0
    val = raw_input ("Pick brightness from 0-100: ")
    speedval = raw_input ("Pick speed from 0-100: ")
    
    
    
    break
elif board = 2:
    ## chose pi-liter
    print "You chose pi-liter"
    break
elif board = 3:
    ## chose  ledborg
    print "You chose ledborg"
    break
elif board = 4:
    ## chose raw edition
    print "You chose raw edition. Good luck."
elif board = 5:
    ## unknown board
    print "This board currently isn't avaliable." 
    break
else:
    print "Sorry, that isn't a valid board."
    break