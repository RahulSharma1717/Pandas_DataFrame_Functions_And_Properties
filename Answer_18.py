# Show a detailed summary of the dataset, highlighting key metrics such as mean, median, standard deviation, minimum,
# maximum, and count for each numerical column, as well as unique counts for categorical variables.

import pandas as pd

df = pd.read_csv('sample_iowa_liquor_sales.csv')
pd.set_option('display.max_columns', None)
print(df.describe())


"""Output:
       Store Number  County Number      Category  Vendor Number  \
count    919.000000     919.000000  9.190000e+02     919.000000   
mean    3510.945593      55.944505  1.055505e+06     273.323177   
std      861.839393      26.879060  9.464502e+04     160.723409   
min     2106.000000       3.000000  1.011100e+06      35.000000   
25%     2614.000000      31.000000  1.022100e+06     115.000000   
50%     3666.000000      57.000000  1.032080e+06     260.000000   
75%     4201.500000      77.000000  1.062310e+06     389.000000   
max     5181.000000      99.000000  1.701100e+06     971.000000   

         Item Number        Pack  Bottle Volume (ml)  State Bottle Cost  \
count     919.000000  919.000000          919.000000         919.000000   
mean    45061.603917   12.150163          986.751904          10.207998   
std     48146.068812   12.938571          617.957560           9.340595   
min       173.000000    1.000000          100.000000           0.000000   
25%     27934.500000    6.000000          750.000000           5.775000   
50%     40682.000000   12.000000          750.000000           7.990000   
75%     57152.500000   12.000000         1000.000000          11.800000   
max    988063.000000  336.000000         6000.000000          99.950000   

       State Bottle Retail  Bottles Sold  Sale (Dollars)  \
count           919.000000    919.000000      919.000000   
mean             15.341012      9.672470      141.239565   
std              14.006247     21.921488      589.045174   
min               0.000000      1.000000        0.000000   
25%               8.670000      3.000000       33.180000   
50%              12.290000      6.000000       69.930000   
75%              17.700000     12.000000      137.160000   
max             149.920000    480.000000    15840.000000   

       Volume Sold (Liters)  Volume Sold (Gallons)  
count            919.000000             919.000000  
mean               9.118020               2.408781  
std               26.681196               7.048362  
min                0.200000               0.050000  
25%                2.000000               0.530000  
50%                6.000000               1.590000  
75%               10.500000               2.770000  
max              588.000000             155.330000
"""