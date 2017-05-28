## Gmail related stuff

email = "insert_gmail_account_here" ## ensure low security is enabled in account settings
password = "please_don't_make_me_explain_this" ## please.


## Don't touch this, I'm curious whether I can remove it from each script
mail = int(feedparser.parse("https://" + email + ":" + password +
"@mail.google.com/gmail/feed/atom/")["feed"] ["fullcount"])

## SimplePush related stuff

salt = "insert_salt_here" ## recommended you play matchmaking on csgo for adequate amounts of salt
key = "insert_key_here"
