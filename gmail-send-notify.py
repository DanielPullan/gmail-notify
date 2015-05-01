#!/usr/bin/python


## imports  
from gi.repository import Notify
import time
import feedparser

## initialises
Notify.init ("Hello world")

## messages for setup
print "Please remember to have your Google account setup to allow login from non-secure sources."
print "I will look into fixing this in a future update."

## variables
username = raw_input("Gmail address: ")
password = raw_input("Password: ")
mail = int(feedparser.parse("https://" + username + ":" + password +
"@mail.google.com/gmail/feed/atom/")["feed"] ["fullcount"])
mail2 = ("You have " + str(mail) + " messages")

messagesLow=Notify.Notification.new ("Few messages", mail2 ,"emblem-default")
messagesMed=Notify.Notification.new ("Lots of messages",mail2 ,"emblem-default")
messagesHigh=Notify.Notification.new ("Mayday, Mayday",mail2 ,"emblem-default")


## Big red button.
## Change to equal to or below?

if mail < 5:
	messagesLow.show ()
elif mail < 10:
	messagesMid.show ()
elif mail < 15:
	messagesHigh.show ()
else:
	print "Uh oh"
