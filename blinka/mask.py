# %%
import numpy as np

import board
import neopixel
import read_excel

# %%
pixels = neopixel.NeoPixel(board.D18, 165)

# %%
for i in read_excel.pattern:
    print(i)
    pixels[i[0]] = (i[1][0], i[1][1], i[1][2])
