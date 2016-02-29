## Author: Daniel Pullan
## Github: GitHub.com/DanielPullan
## Website: DanielPullan.co.uk

## imports
import time
import feedparser

## global variables for gmail
username = raw_input("Your gmail username is: ")
password = raw_input ("Your password is: ")
mail = int(feedparser.parse("https://" + username + ":" + password +
"@mail.google.com/gmail/feed/atom/")["feed"] ["fullcount"])

## contact = int(feedparser.parse("https://" + username + ":" + password +
## "@mail.google.com/gmail/feed/atom/LABEL-NAME")["feed"] ["fullcount"])


## everything else
## empty for now