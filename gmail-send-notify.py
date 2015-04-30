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
username = raw_input("gmail address: ")
password = raw_input("password: ")
mail = int(feedparser.parse("https://" + username + ":" + password +
"@mail.google.com/gmail/feed/atom/")["feed"] ["fullcount"])

Hello=Notify.Notification.new ("Hello world","you have 21 messages" ,"emblem-default")
Goodbye=Notify.Notification.new ("Hello world","you have less than 21 messages" ,"emblem-default")

messagesLow=Notify.Notification.new ("Few messages","You have a few messages." ,"emblem-default")
messagesMed=Notify.Notification.new ("Lots of messages","You have quite a few messages." ,"emblem-default")
messagesHigh=Notify.Notification.new ("Mayday, Mayday","You have a tonne of messages." ,"emblem-default")


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
