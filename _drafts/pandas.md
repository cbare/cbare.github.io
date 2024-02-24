import pandas as pd

SHOW_ALL = [
    'display.max_rows',500,
    'display.max_columns',500,
    'display.width',140,
]

with pd.option_context(*SHOW_ALL):
    display(df)


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 140)
