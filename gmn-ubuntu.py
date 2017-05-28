## Author: Daniel Pullan
## Github: GitHub.com/DanielPullan
## Website: DanielPullan.co.uk

import feedparser
from time import sleep
from config import email, password, mail, salt, key
import subprocess as s
s.call(['notify-send','foo','bar'])

## create a function called alert
def alert():
        ## use notify-send to send a notification
        s.call(['notify-send','Email','New email recieved'])

## If there is an email at all (more than nothing)
if mail > 0:
        ## do the alert function
        alert()
## else (there is no emails)
else:
        ## print there is nothing, mainly for logging purposes
        print ("There is nothing")
