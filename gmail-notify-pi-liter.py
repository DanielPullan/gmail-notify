##################
##Lucky it's A####
##Family Py!######
##################

## Author: Daniel Pullan
## Twitter: @soundsarenoisy
## Github: /soundsarenoisy


## imports
import time
import feedparser

## global variables for gmail
## username = raw_input('Your gmail username is:')
username789 = "EMAIL@gmail.com"
password = "PASSWORD"
mail = int(feedparser.parse("https://" + username + ":" + password +
"@mail.google.com/gmail/feed/atom/")["feed"] ["fullcount"])
contact = int(feedparser.parse("https://" + username + ":" + password +
"@mail.google.com/gmail/feed/atom/LABEL-NAME")["feed"] ["fullcount"])

## everything else
## empty for now

