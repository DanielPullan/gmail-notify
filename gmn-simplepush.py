## Author: Daniel Pullan
## Github: GitHub.com/DanielPullan
## Website: DanielPullan.co.uk

## This script should work, make sure you make changes to config.py

# i had to pip-install simplepush, if you have issues, installing python-dev
# fixed it for me
from simplepush import send_encrypted
import feedparser
# i made a config file defining key, password and salt so that I could upload
# it once and then gitignore it to avoid encryption keys being uploaded
from  config import email, password, salt, key

## create an int using feedparser to parse the fullcount from the email feed
mail = int(feedparser.parse("https://" + email + ":" + password +
"@mail.google.com/gmail/feed/atom/")["feed"] ["fullcount"])

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
