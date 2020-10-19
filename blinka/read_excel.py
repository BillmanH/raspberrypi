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
                         index_col=0)


rows = [i+1 for i in range(19)]
columns = [i+1 for i in range(18)]
led_lights = get_excel("Mask").loc[rows, columns]

# %%
# Getting patterns
pattern_sheets = [x for x in xl if 'pattern' in x]
pats = [get_excel(pattern).loc[rows, columns] for pattern in pattern_sheets]


# %%
# Parsing out patterns
def get_pattern(pat):
    led_df = pd.DataFrame(led_lights.values.flatten(), columns=['led'])
    led_df['color'] = pat.values.flatten()
    led_df = led_df.dropna().sort_values('led')
    try:
        pattern = [[int(led_df.loc[i, 'led']),
                    [int(c) for c in led_df.loc[i, 'color'].split(',')]
                    ]
                   for i in led_df.index]
    except:
        print(led_df.values)
        print("cannot parse int")
    return pattern


pattern = [get_pattern(pat) for pat in pats]
