## Author: Daniel Pullan
## Github: GitHub.com/DanielPullan
## Website: DanielPullan.co.uk
## Device: Sense HAT / Astro Pi

from sense_emu import SenseHat
from time import sleep
import login
from login import mail

## Init the current device
sense = SenseHat()

## Device parameters

sense.show_message(mail, text_colour=[255, 0, 0])