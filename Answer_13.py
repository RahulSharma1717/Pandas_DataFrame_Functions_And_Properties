# Check out the number of data and data-type of each column in the dataset.

import pandas as pd

df = pd.read_csv('sample_iowa_liquor_sales.csv')
# pd.set_option('display.max_columns', None)
print(df.info())


"""Output:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 919 entries, 0 to 918
Data columns (total 24 columns):
 #   Column                 Non-Null Count  Dtype  
---  ------                 --------------  -----  
 0   Invoice/Item Number    919 non-null    object 
 1   Date                   919 non-null    object 
 2   Store Number           919 non-null    int64  
 3   Store Name             919 non-null    object 
 4   Address                919 non-null    object 
 5   City                   919 non-null    object 
 6   Zip Code               919 non-null    object 
 7   Store Location         919 non-null    object 
 8   County Number          919 non-null    int64  
 9   County                 919 non-null    object 
 10  Category               919 non-null    int64  
 11  Category Name          919 non-null    object 
 12  Vendor Number          919 non-null    int64  
 13  Vendor Name            919 non-null    object 
 14  Item Number            919 non-null    int64  
 15  Item Description       919 non-null    object 
 16  Pack                   919 non-null    int64  
 17  Bottle Volume (ml)     919 non-null    int64  
 18  State Bottle Cost      919 non-null    float64
 19  State Bottle Retail    919 non-null    float64
 20  Bottles Sold           919 non-null    int64  
 21  Sale (Dollars)         919 non-null    float64
 22  Volume Sold (Liters)   919 non-null    float64
 23  Volume Sold (Gallons)  919 non-null    float64
dtypes: float64(5), int64(8), object(11)
memory usage: 172.4+ KB
None
"""