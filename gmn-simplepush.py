## Author: Daniel Pullan
## Github: GitHub.com/DanielPullan
## Website: DanielPullan.co.uk

from time import sleep
from config import email, password, mail, salt, key
from simplepush import send_encrypted

## create a function called alert
def alert():
        ## use send_encrypted from simplepush to send an alert
        send_encrypted (key, password, salt, "Email", "New email")

## If there is an email at all (more than nothing)
if mail > 0:
        ## do the alert function
        alert()
## else (there is no emails)
else:
        ## print there is nothing, mainly for logging purposes
        print ("There is nothing")
