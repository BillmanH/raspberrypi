import numpy as np
import pandas as pd

def dummy_pixels(n):
    pixels = np.array([i for i in list(range(n))])
    return pixels
        
def leds_to_df(l,s):
    l.shape = s
    df = pd.DataFrame(l)
    return df

def df_to_leds(df):
    x = df.values
    return x.flatten()

def random_color():
    x = np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255)
    return x

def paginate_df(df):
    for i in df.index:
        if i % 2 == 0:
            pass
        else:
            df.loc[i] = df.loc[i].values[::-1]
    return df