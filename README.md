# raspberrypi
My personal tech framework for Raspbery Pis. Most everything should work on any python envoronmet. 

## Currently building for the Raspberry Pi 4
However I have some stuff for a pi_zero build as well.

## Two major sections
**webapp** localhosted flask app for buttons and controlls

**blinka** Manipulating LEDs using adafruit neopixel library.
**note** the LEDs that I'm using require PWM to activate. Not all GPIO pins support PWM. Make sure you are using the right pins. 

# Running the web app
```
sudo python3 app.py
```

# command line scripts for blinking apps: 

| file name | purpose | command line example |
|---|---|---|
| `grid_test.py` | testing led array. two `int` arguments are the length of the array and the position of the last led light. I use this to make sure my soldering was done correctly. | `sudo python3 grid_test.py 20 15` |
| `read_excel.py` | reads a color matrix from an excel file. That way you can use an Excel sheet to 'draw' your pattern. | not used directly. this is imported in other scritps.  |
| `mask.py` | continuous loop that loads the patterns from excel and 'builds' the faces. | `sudo python3 mask.py` |

