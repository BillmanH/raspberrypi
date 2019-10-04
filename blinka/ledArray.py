import numpy as np
import pandas as pd

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
# NeoPixels must be connected to D10, D12, D18 or D21 to work.

# %%


class Screen:
    def __init__(self,
                 nrows,
                 ncols,
                 NeoPixel="dummy",
                 board="dummy",
                 alter_rows=True,
                 ):
        # The two main dataframes that you'll use:
        self.leds = pd.DataFrame()
        self.colors = pd.DataFrame()

        # However you can set it to Dummy to develop offline.
        self.board = board
        self.nrows = nrows
        self.ncols = ncols
        self.numled = nrows*ncols
        self.alter_rows = alter_rows

        # actvate and build dfs once the params are set.
        self.pixels = self.setPixels(NeoPixel)

    def __str__(self):
        return f"({self.nrows},{self.ncols}) screen"

    def paginate_df(self):
        for i in self.leds.index:
            if i % 2 == 0:
                pass
            else:
                self.leds.loc[i] = self.leds.loc[i].values[::-1]

    def setPixels(self, NeoPixel):
        if NeoPixel == "dummy":
            pixels = np.array([i for i in list(range(self.numled))])
        else:
            pixels = neopixel.NeoPixel(board, self.numled)
        df_shape = np.array([i for i in list(range(self.numled))])
        df_shape.shape = (self.nrows, self.ncols)
        self.leds = pd.DataFrame(df_shape)
        if self.alter_rows:
            self.paginate_df()
        self.colors = (pd.DataFrame(columns=range(shape[1]),
                                    index=range(shape[0]))
                       .fillna("0,0,0"))


s = Screen(20, 9)
print(s)
s.colors


# %%
s.leds

# %%


# %%


def df_to_leds(df):
    x = df.values
    return x.flatten()


def random_color():
    x = np.random.randint(0, 255), np.random.randint(
        0, 255), np.random.randint(0, 255)
    return x


def paginate_df(df):
    for i in df.index:
        if i % 2 == 0:
            pass
        else:
            df.loc[i] = df.loc[i].values[::-1]
    return df
