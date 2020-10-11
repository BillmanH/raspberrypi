import numpy as np

import board
import neopixel

numled = 600

pixels = neopixel.NeoPixel(board.D18, numled)


for i in range(3):
    print(i)
    for i in range(numled):
        print(i,end=" ")
        pixels[i] = (np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255))

    for i in range(numled):
        pixels[(numled-1)-i] = (0,0,0)




