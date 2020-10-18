# %%
import numpy as np

import board
import neopixel
import read_excel

# %%
pixels = neopixel.NeoPixel(board.D18, numled)

# %%
for i in read_excel.pattern:
    pixels[i[0]] = i[1]
