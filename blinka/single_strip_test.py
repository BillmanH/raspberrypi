import numpy as np

import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 180)


numled = 180

chosen = 1
for i in range(200):
    pixels[chosen] = (0,0,0)
    chosen = np.random.choice(np.array(range(numled)))
    pixels[chosen] = (np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255))
    print(chosen)

pixels[chosen] = (0,0,0)

for i in range(3):
    for i in range(numled):
        pixels[i] = (np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255))

    for i in range(numled):
        pixels[(numled-1)-i] = (0,0,0) 