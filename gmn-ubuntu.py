## Author: Daniel Pullan
## Github: GitHub.com/DanielPullan
## Website: DanielPullan.co.uk

import feedparser
from time import sleep
from config import email, password, mail, salt, key
import subprocess as s

## create a function called alert
def noEmail():
        ## use notify-send to send a notification
        s.call(['notify-send','Nothing','Nothing there'])
        print ("No emails")
def lowEmail ():
        s.call(['notify-send', 'Low Emails', 'There is a low amount of emails'])
        print ("Low emails")
def mediumEmail():
        s.call(['notify-send', 'Medium Emails', 'There is a medium amount of emails'])
        print ("Medium emails")
def highEmail():
        s.call(['notify-send', 'High Emails', 'There is a high amount of emails'])
        print ("High emails")

if mail < 5:
        lowEmail()
elif mail < 10:
        mediumEmail()
elif mail < 15:
        highEmail()
else:
        ## print there is nothing, mainly for logging purposes
        noEmail()
