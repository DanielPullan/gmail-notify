# gmail-notify
Written by Dan [@soundarenoisy](http://twitter.com/soundsarenoisy).

This readme page is the entire documentation, if you spot any issues, please file a bug.

### Requirements

- A networked Raspberry Pi, Wired connection preferred.
- A up to date copy of Raspbian
- A PiGlow. [Buy from Pimoroni Shop](http://shop.pimoroni.com/products/piglow)

### Software
A little long, but you can use most of these in other projects.
- Python 2.6 (Default in Raspbian)
- Python-Dev and Python-Pip 
- feedparser (A pip package)
- PyGlow [Download from Github](https://github.com/Boeeerb/PiGlow)
- Pygame (Default in Raspbian)
- Git


### Setup

- Setup your Pi [elinux.org Wiki Guide](http://elinux.org/RPi_Easy_SD_Card_Setup)
- Install Python-Dev, Python-Pip, Feedparser, Git, python-smbus and python-psutil
 ```sudo apt-get install python-dev```
``` sudo apt-get install python-pip```
``` sudo pip install feedparser```
``` sudo apt-get install git```
``` sudo apt-get install python-smbus```
``` sudo apt-get install python-psutil```
- Enable i2c driver
``` sudo nano /etc/modules```
(more coming)
- Install Pyglow



### How it works
Here, how it works will be explained