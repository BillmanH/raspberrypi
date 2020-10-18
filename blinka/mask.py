# %%
import numpy as np

import board
import neopixel
import read_excel

# %%
pixels = neopixel.NeoPixel(board.D18, 165)

# %%
patterns = read_excel.pattern


def sparkle_mask():
    y = 0
    myRange = range(100)
    for i in myRange:
        pixels[y] = (0, 0, 0)
        y = np.random.randint(0, 165)
        rgb = (np.random.randint(0, 255),
               np.random.randint(0, 255),
               np.random.randint(0, 255))
        pixels[y] = rgb


def cycle_patterns():
    for pattern in patterns:
        for i in pattern:
            try:
                pixels[i[0]] = (i[1][0], i[1][1], i[1][2])
            except:
                pass
        sparkle_mask()


# pixels[[i[0] for i in read_excel.pattern]] = [
#     tuple(j for j in i[1]) for i in read_excel.pattern]
cycle_patterns()
