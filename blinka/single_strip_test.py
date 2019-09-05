import numpy as np

import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 60)

chosen = 1
for i in range(500):
    pixels[chosen] = (0,0,0)
    chosen = np.random.choice(np.array(range(60)))
    pixels[chosen] = (np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255))
    
pixels[chosen] = (0,0,0)

for i in range(10):
    for i in range(60):
        pixels[i] = (np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255))

    for i in range(60):
        pixels[59-i] = (0,0,0) 
