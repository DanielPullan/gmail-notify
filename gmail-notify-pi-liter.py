##################  ############
##Lucky it's A####  ##Pi-Liter##
##Family Py!######  ##Edition###
##################  ############

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
username = raw_input("Your gmail username is: ")
password = raw_input ("Your password is: ")
mail = int(feedparser.parse("https://" + username + ":" + password +
"@mail.google.com/gmail/feed/atom/")["feed"] ["fullcount"])

## contact = int(feedparser.parse("https://" + username + ":" + password +
## "@mail.google.com/gmail/feed/atom/LABEL-NAME")["feed"] ["fullcount"])

#Turn off GPIO Warnings
GPIO.setwarnings(False)

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
         
 # From here on, this is where the code lives.  
 if mail > 0:
        print('Item has sold!')

elif mail > 4:
        print('You have too many messages in your inbox')

elif mail > 0:
        print ('You have a message in your inbox')

else:
        print ('Nope, no mail yet!')
  
if __name__ == '__main__':  
 main() 