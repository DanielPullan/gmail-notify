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

	Then make sure the following is at the end of the file.
	```i2c-dev ```
	```i2c-bcm2708 ``` 
    
   and then CTRL+O to save the file. Make sure you say yes to the prompt. CTRL+Z to exit.
   
   Then (Yes there's more, sorry)
   
   ```sudo nano /etc/modprobe.d/raspi-blacklist.conf```
   
   and ensure that every line that has text, begins with a hashtag. If it doesn't, add them. Same again, CTRL+O to save, yes to prompt, CTRL+Z to exit.
   
   Reboot the Pi to make sure everything has been enabled.
   ```sudo reboot```

- Install PiGlow
	Create and change to piglow directory.
    ```mkdir piglow```
	```cd piglow```
    
    Download piglow.
    ```wget https://raw.github.com/Boeeerb/PiGlow/master/piglow.py```

(more coming)



### How it works
Here, how it works will be explained