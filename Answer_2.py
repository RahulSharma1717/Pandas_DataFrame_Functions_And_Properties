# Check the number of rows and columns in the dataset.

import pandas as pd

df = pd.read_csv('retail_data.csv')
# pd.set_option('display.max_columns', None)
print(df.shape)


"""Output:
(293911, 30)
"""