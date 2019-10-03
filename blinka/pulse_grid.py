import numpy as np
import pandas as pd

from ast import literal_eval
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 180)


#local libraries
import ledArray as led

numled = 180
shape = (9,20)

leds = led.dummy_pixels(numled)
df = led.leds_to_df(leds,shape)
df = led.paginate_df(df)

df_rgb = pd.DataFrame(columns=range(shape[1]),
                        index=range(shape[0])).fillna("0,0,0")

print(df)
print(df_rgb)

for i in range(500):
    y = np.random.randint(0,shape[1])
    x = np.random.randint(0,shape[0])
    #print(f"x: {x}, y:{y}")
    p = df.loc[x,y]
    rgb = df_rgb.loc[x,y].split(",")
    rgb = [int(n) for n in rgb]
    rgb = (rgb[0]+10,rgb[1]+10,rgb[2]+10)
    df_rgb.loc[x,y] = ','.join([str(n) for n in rgb])
    #print(f"{i}: printing {p} to : {rgb}")
    pixels[p] = rgb

a = [[aa for aa in range(20)] for ab in range(10)]

for y in a:
    x = df.index.tolist()
    p = np.array(df.loc[x,y].values).flatten()
    rgb = (np.random.randint(0,255),
            np.random.randint(0,255),
            np.random.randint(0,255))
    for i in p:
        pixels[i] = rgb

#now turn the lights out
for i in range(numled):
    pixels[i] = (0,0,0)

