## Author: Daniel Pullan
## Github: GitHub.com/DanielPullan
## Website: DanielPullan.co.uk

from time import sleep
from mote import Mote


mail = int(feedparser.parse("https://" + email + ":" + password + "@mail.google.com/gmail/feed/atom/")["feed"] ["fullcount"])
mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

# stripnumber, pixel number (0 is first), red, green, blue
# mote.set_pixel(1, 1, 255, 0 0) = on first strip, second pixel, red = 255, blue and green = 0

mote.clear()
for pixel in range(16):
    mote.set_pixel(1, pixel, 0,0,0)
    mote.show()

