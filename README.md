# Gmail-Notify

Written by Daniel Pullan (https://danielpullan.co.uk)

Project status: Not dead (May 2017).

**27/05/2017**: Since starting a new job, I've changed a lot of how I code. I got a working version for SimplePush and so will translate this style to the other devices.

### About Gmail-Notify
Gmail-Notify was originally written to be used with a Ledborg. After mine died, I rewrote it to run on a Piglow instead. After buying a Pi-Liter, I instead decided to write Gmail-Notify versions for all 3 platforms.  The list has since grown.

Gmail-Notify is currently in major development, it has been  in states of working and not working in the past, my goal of course is to get functionality on all platforms then add features when possible, with features working to the strengths of each platform

### A note before you read any further
Things probably don't work, there are definitely bugs. The documentation whilst being improved, still isn't great. I'm currently in the process of "Making Gmail-Notify Great Again!" however this will be a lengthy process.

Please do report things if you can see how I can im

### Targets

**SimplePush** - Working

**Ubuntu** - Not working, in development

**PiGlow** - Not working

**AstroPi** - Not working

**Pi-Liter** - Not working

**Ledborg** - Not working

**Raw LED** - Not working

### Requirements
You'll need Python installed (naturally!), python-pip to install some packages, python-dev potentially if you start having issues or if the script specifically asks for it.

For each board, you'll need to follow the board specific steps for setting up. If you're using the Ubuntu version you shouldn't need to install anything, if you're using the simplepush version you'll need to have simplepush installed using pip, you'll also need the android app as well as a key and salt from the app.

You'll also need feedparser (another one from pip).

I will try to make sure the script themselves have setup steps and solutions to common problems within them, however I may also make a Wiki if this ends up being a large amount of data.

### Personal Wishlist

- I would like to work out a way of using the Google Assistant on the Raspberry Pi to announce emails or at least be able to feed back if there are emails on request
- I would like platforms with lots of LED's to give more information than just "there's an email". Stuff like number of emails, email from a specific person or containing specific keywords could have bigger alerts for example.
