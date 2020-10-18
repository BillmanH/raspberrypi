# %%

import pandas as pd
import numpy as np
import yaml

# %%
with open("settings.yaml") as f:
    params = yaml.load(f)


xl = pd.ExcelFile(params['excel_file']).sheet_names


def get_excel(name):
    return pd.read_excel(params['excel_file'],
                         sheet_name=name,
                         headers=None)


led_lights = get_excel("Mask").iloc[0:18, 0:18]
pattern = get_excel("pattern 2").iloc[0:18, 0:18]
print(led_lights.shape, pattern.shape)


# %%
led_df = pd.DataFrame(led_lights.values.flatten(), columns=['led'])
led_df['color'] = pattern.values.flatten()
led_df = led_df.dropna().sort_values('led')

# %%


pattern = [[int(led_df.loc[i, 'led']),
            [int(c) for c in led_df.loc[i, 'color'].split(',')]
            ]
           for i in led_df.index]
pattern
# %%
