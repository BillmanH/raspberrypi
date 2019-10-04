# raspberrypi
My personal tech framework for Raspbery Pis. Most everything should work on any python envoronmet. 

# Currently building for the Raspberry Pi 4
However I have some stuff for a pi_zero build as well.

## Two major sections
**webapp** localhosted flask app for buttons and controlls

**blinka** Manipulating LEDs using adafruit neopixel library.


# Running the web app
```
sudo python3 app.py
```

# command line scripts for blinking apps: 
```
sudo python3 blinka/pulse_grid.py
```

the connection is the same as the IP address that you use for SSH. 
