# Check details for index numbers in the dataset.

import pandas as pd

df = pd.read_csv('retail_data.csv')
# pd.set_option('display.max_columns', None)
print(df.index)


"""Output:
RangeIndex(start=0, stop=293911, step=1)
"""