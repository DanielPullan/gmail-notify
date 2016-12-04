## Author: Daniel Pullan
## Github: GitHub.com/DanielPullan
## Website: DanielPullan.co.uk

## This is the login script.

import feedparser

username = raw_input("Your gmail username is: ")
password = raw_input ("Your password is: ")
mail = int(feedparser.parse("https://" + username + ":" + password +
"@mail.google.com/gmail/feed/atom/")["feed"] ["fullcount"])
mail2 = str(mail)

