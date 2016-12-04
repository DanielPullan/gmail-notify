## Author: Daniel Pullan
## Github: GitHub.com/DanielPullan
## Website: DanielPullan.co.uk
## Device: Pimoroni PiGlow

from sense_emu import SenseHat
from time import sleep
import login
from login import mail, mail2

## Init the current device
from sense_emu import SenseHat

sense = SenseHat()

sense.show_message(mail2, text_colour=[255, 0, 0])

