# Display the first few rows of the dataset.

import pandas as pd

df = pd.read_csv('sample_iowa_liquor_sales.csv')
pd.set_option('display.max_columns', None)
print(df.head())


"""Output:
  Invoice/Item Number        Date  Store Number  \
0        S28865700001  11-09-2015          2538   
1        S29339300091  11/30/2015          2662   
2        S28866900001  11-11-2015          3650   
3        S29134300126  11/18/2015          3723   
4        S29282800048  11/23/2015          2642   

                          Store Name                Address       City  \
0    Hy-Vee Food Store #3 / Waterloo       1422 FLAMMANG DR   WATERLOO   
1  Hy-Vee Wine & Spirits / Muscatine  522 MULBERRY, SUITE A  MUSCATINE   
2         Spirits, Stogies and Stuff     118 South Main St.   HOLSTEIN   
3                 J D Spirits Liquor           1023  9TH ST      ONAWA   
4    Hy-Vee Wine and Spirits / Pella        512 E OSKALOOSA      PELLA   

  Zip Code                                     Store Location  County Number  \
0    50702  1422 FLAMMANG DR\nWATERLOO 50702\n(42.459938, ...              7   
1    52761           522 MULBERRY, SUITE A\nMUSCATINE 52761\n             70   
2    51025  118 South Main St.\nHOLSTEIN 51025\n(42.490073...             47   
3    51040  1023 9TH ST\nONAWA 51040\n(42.025841, -96.095845)             67   
4    50219  512 E OSKALOOSA\nPELLA 50219\n(41.397023, -92....             63   

       County  Category                   Category Name  Vendor Number  \
0  Black Hawk   1701100  DECANTERS & SPECIALTY PACKAGES            962   
1   Muscatine   1701100  DECANTERS & SPECIALTY PACKAGES             65   
2         Ida   1701100  DECANTERS & SPECIALTY PACKAGES            962   
3      Monona   1081200                  CREAM LIQUEURS            305   
4      Marion   1701100  DECANTERS & SPECIALTY PACKAGES            962   

                         Vendor Name  Item Number  \
0  Duggan's Distillers Products Corp          238   
1                    Jim Beam Brands          173   
2  Duggan's Distillers Products Corp          238   
3                            MHW Ltd          258   
4  Duggan's Distillers Products Corp          238   

               Item Description  Pack  Bottle Volume (ml)  State Bottle Cost  \
0  Forbidden Secret Coffee Pack     6                1500              11.62   
1   Laphroaig w/ Whiskey Stones    12                 750              19.58   
2  Forbidden Secret Coffee Pack     6                1500              11.62   
3           Rumchata "GoChatas"     1                6000              99.00   
4  Forbidden Secret Coffee Pack     6                1500              11.62   

   State Bottle Retail  Bottles Sold  Sale (Dollars)  Volume Sold (Liters)  \
0                17.43             6          104.58                   9.0   
1                29.37             4          117.48                   3.0   
2                17.43             1           17.43                   1.5   
3               148.50             1          148.50                   6.0   
4                17.43             6          104.58                   9.0   

   Volume Sold (Gallons)  
0                   2.38  
1                   0.79  
2                   0.40  
3                   1.59  
4                   2.38
"""