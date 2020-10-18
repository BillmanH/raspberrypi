# %%
import numpy as np

import board
import neopixel
import read_excel

# %%
pixels = neopixel.NeoPixel(board.D18, 165)

# %%
for i in read_excel.pattern:
    try:
        pixels[i[0]] = (i[1][0], i[1][1], i[1][2])
    except:
        pass


pixels[[i[0] for i in read_excel.pattern]] = [
    tuple(j for j in i[1]) for i in read_excel.pattern]
