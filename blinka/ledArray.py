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
        self.pixels = self.setPixels()

    def __str__(self):
        return f"({self.nrows},{self.ncols}) screen"

    def paginate_df(self):
        for i in self.leds.index:
            if i % 2 == 0:
                pass
            else:
                self.leds.loc[i] = self.leds.loc[i].values[::-1]

    def setPixels(self):
        if self.board == "dummy":
            pixels = np.array([i for i in list(range(self.numled))])
        else:
            pixels = neopixel.NeoPixel(self.board, self.numled)
        df_shape = np.array([i for i in list(range(self.numled))])
        df_shape.shape = (self.nrows, self.ncols)
        self.leds = pd.DataFrame(df_shape)
        if self.alter_rows:
            self.paginate_df()
        self.colors = (pd.DataFrame(columns=range(df_shape.shape[1]),
                                    index=range(df_shape.shape[0]))
                       .fillna("0,0,0"))
    
    def get_vals(self,x,y):
        l = [self.leds.loc[x,y].values.flatten(),
            self.colors.loc[x,y].applymap(self.to_set).values.flatten()]
        return [[l[0][i],l[1][i]] for i in range(len(l[0]))]
    
    def set_vals(self,x,y,rgb):
        rgb = self.to_str(rgb)
        self.colors.loc[y,x] = rgb
        
    def random_color(self):
        x = np.random.randint(0, 255), np.random.randint(
            0, 255), np.random.randint(0, 255)
        return x

    #Value cleaners and transformers
    def to_set(self,c):
        '''
        where c is a color
        '''
        c = [int(i) for i in c.split(",")]
        return tuple(c)

    def to_str(self,c):
        '''
        where c is a color (r,g,b) tuple
        '''
        def cap(c):
            # if it can't be an int, then it is zero
            try:
                c = int(c)
            except: 
                c = 0
            if c > 255:
                c = 255

            return str(c)

        c = ",".join([cap(i) for i in c])
        return c

