################## ##################
##Lucky it's A#### ##Gmail###########
##Family Py!###### #######Notify#####
################## ##################

## Author: Daniel Pullan
## Twitter: @soundsarenoisy
## Github: /soundsarenoisy

## Thanks to "Average Man" for the GPIO Mapping.


## imports
import time
import feedparser
import os 
import RPi.GPIO as GPIO  

## global variables for gmail
## username = raw_input('Your gmail username is:')
username789 = "EMAIL@gmail.com"
password = "PASSWORD"
mail = int(feedparser.parse("https://" + username + ":" + password +
"@mail.google.com/gmail/feed/atom/")["feed"] ["fullcount"])
contact = int(feedparser.parse("https://" + username + ":" + password +
"@mail.google.com/gmail/feed/atom/LABEL-NAME")["feed"] ["fullcount"])

# Define PiLITEr to GPIO mapping  
LED1 = 7  
LED2 = 11  
LED3 = 13   
LED4 = 12  
LED5 = 15  
LED6 = 16  
LED7 = 18  
LED8 = 22  
  
# Main program  
def main():  
 GPIO.setmode(GPIO.BCM) # Use BCM GPIO numbers  
 GPIO.setup(LED1, GPIO.OUT) #Set GPIO pin to output (to 'give' power)  
 GPIO.setup(LED2, GPIO.OUT) #Set GPIO pin to output (to 'give' power)  
 GPIO.setup(LED3, GPIO.OUT) #Set GPIO pin to output (to 'give' power)  
 GPIO.setup(LED4, GPIO.OUT) #Set GPIO pin to output (to 'give' power)  
 GPIO.setup(LED5, GPIO.OUT) #Set GPIO pin to output (to 'give' power)  
 GPIO.setup(LED6, GPIO.OUT) #Set GPIO pin to output (to 'give' power)  
 GPIO.setup(LED7, GPIO.OUT) #Set GPIO pin to output (to 'give' power)  
 GPIO.setup(LED8, GPIO.OUT) #Set GPIO pin to output (to 'give' power)  
         
 # Turn on LED 1  
 GPIO.output(LED1) == True  
  
if __name__ == '__main__':  
 main() 