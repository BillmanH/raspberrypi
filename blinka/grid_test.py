import numpy as np

import board
import sys
import neopixel

myargs = sys.argv
numled = int(myargs[1])
end_led = int(myargs[2])


# not all of the grid tests can read PWM (Pulse width modulation)
pixels = neopixel.NeoPixel(board.D18, numled)



for i in range(3):
    print(i)
    for i in range(numled):
        pixels[i] = (100,100,100)

    for i in range(numled):
        pixels[(numled-1)-i] = (0,0,0)


pixels[end_led] = (100,100,100)

