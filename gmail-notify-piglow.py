## Author: Daniel Pullan
## Github: GitHub.com/DanielPullan
## Website: DanielPullan.co.uk


## imports	
from pyglow import PyGlow
import pygame
import time
import feedparser

## global variables for gmail
username = raw_input("Your gmail username is: ")
password = raw_input ("Your password is: ")
mail = int(feedparser.parse("https://" + username + ":" + password +
"@mail.google.com/gmail/feed/atom/")["feed"] ["fullcount"])

## contact = int(feedparser.parse("https://" + username + ":" + password +
## "@mail.google.com/gmail/feed/atom/LABEL-NAME")["feed"] ["fullcount"])

## global variables for pyglow
pyglow = PyGlow()
pygame.mixer.init()
number = 0
val = 100
speedval = 90


## Option chooser. It may not be pretty, it may not even work,
## I did it myself without looking anything up. Airplane mode wooo.
option = raw_input("Pick an option [1,2,3] for version. 1 - easy, 
2 - light per email, 3 - with contact mode")

if option == 1:
	easyMode
	break

elif option == 2: 
	hardMode
	break

elif option == 3:
	print("Refer to readme to setup contact function")
	contactMode
	break

else:
	print("Come on man, we spoke about this. Try again friend.")
	break
	
## Contact Mode
if true:
	print("You have " + mail + " messages in inbox and " + contact
	+ " are from your Contact.")

## Easy Mode
if mail > 0
	print("You got mail buddy")
	break


## Hard Mode
if mail == 1: 
        pyglow.all(0)
        pyglow.pulse(1, 100, speedval)
        print('Item has sold')

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
