# Display the number of rows and columns in the dataset separately.

import pandas as pd

df = pd.read_csv('sample_iowa_liquor_sales.csv')
# pd.set_option('display.max_columns', None)
print(f"Number of rows in the dataset: {df.shape[0]}")
print(f"\nNumber of columns in the dataset: {df.shape[1]}")


"""Output:
Number of rows in the dataset: 919

Number of columns in the dataset: 24
"""