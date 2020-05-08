# %%

import pandas as pd
import numpy as np
import yaml

# %%
with open("settings.yaml") as f:
    params = yaml.load(f)


def get_excel():
    return pd.read_excel(params['excel_file'], index_col=0)


# %%
