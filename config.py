## Gmail related stuff
import feedparser

email = "insert_gmail_account_here" ## ensure low security is enabled in account settings
password = "please_don't_make_me_explain_this" ## please.


## Don't touch this, I'm curious whether I can remove it from each script
mail = int(feedparser.parse("https://" + email + ":" + password +
"@mail.google.com/gmail/feed/atom/")["feed"] ["fullcount"])

## SimplePush related stuff

salt = "insert_salt_here"
key = "insert_key_here"
