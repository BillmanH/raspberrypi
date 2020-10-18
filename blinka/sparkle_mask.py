# %%
import numpy as np

import board
import neopixel
import read_excel

# %%
pixels = neopixel.NeoPixel(board.D18, 165)

# %%
myRange = range(300)
for i in myRange:
    pixels[y] = (0,0,0)
    y = np.random.randint(0, 165)
    rgb = (np.random.randint(0, 255),
           np.random.randint(0, 255),
           np.random.randint(0, 255))
    pixels[y] = rgb
