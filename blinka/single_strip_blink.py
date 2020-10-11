import numpy as np

import board
import neopixel
import time

numled = 60 

pixels = neopixel.NeoPixel(board.D18, numled)

rgbset = [0,0,0]

def setColor(rgb):
    x = np.random.randint(0,2)
    rgb[x] = rgb[x]+10
    return rgb

print("starting program")
while True:
    pix = np.random.randint(0,numled)
    print(pix, end=", ")
    rgbset = setColor(rgbset) 
    pixels[pix] = (rgbset[0],rgbset[1],rgbset[2])
    print("writing to: ",pix,end=': ')
    time.sleep(.2)

    pixels[pix] = (0,0,0)



