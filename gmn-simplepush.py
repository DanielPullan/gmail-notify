## Author: Daniel Pullan
## Github: GitHub.com/DanielPullan
## Website: DanielPullan.co.uk

## This script should work, make sure you make changes to config.py

# i had to pip-install simplepush, if you have issues, installing python-dev
# fixed it for me
from simplepush import send_encrypted
# i made a config file defining key, password and salt so that I could upload
# it once and then gitignore it to avoid encryption keys being uploaded
import feedparser
from  config import email, password, salt, key

mail = int(feedparser.parse("https://" + email + ":" + password +
"@mail.google.com/gmail/feed/atom/")["feed"] ["fullcount"])


def alert():
        send_encrypted (key, password, salt, "Email", "New email")


if mail > 0:
        alert()
else:
        print ("There is nothing")
