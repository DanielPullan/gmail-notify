################## ##################
##Lucky it's A#### ##Gmail###########
##Family Py!###### #######Notify#####
################## ##################

## Author: Daniel Pullan
## Twitter: @soundsarenoisy
## Github: /soundsarenoisy

## imports
import time
import feedparser

## global variables for gmail
## same for all versions of gmail-notify
username = "EMAIL@gmail.com"
password = "PASSWORD"
mail = int(feedparser.parse("https://" + username + ":" + password +
"@mail.google.com/gmail/feed/atom/")["feed"] ["fullcount"])
contact = int(feedparser.parse("https://" + username + ":" + password +
"@mail.google.com/gmail/feed/atom/LABEL-NAME")["feed"] ["fullcount"])

## everything else
## empty for now