# Reveal the bottom rows of the dataset.

import pandas as pd

df = pd.read_csv('sample_iowa_liquor_sales.csv')
pd.set_option('display.max_columns', None)
print(df.tail())


""""Output:
    Invoice/Item Number        Date  Store Number  \
914        S26164400020  06/16/2015          3944   
915        S19675100022  06/25/2014          4008   
916        S12278000057  05/22/2013          3385   
917        S05694100030  05/23/2012          2487   
918        S23309100006  01-06-2015          4559   

                         Store Name                  Address          City  \
914       Sam's Club 4973 / Dubuque           4400 ASBURY RD       DUBUQUE   
915            Sioux Valley Spirits            116 E MAIN ST        ANTHON   
916  Sam's Club 8162 / Cedar Rapids  2605 BLAIRS FERRY RD NE  CEDAR RAPIDS   
917            Anamosa Family Foods            402 EAST MAIN       ANAMOSA   
918             Osage Payless Foods            633, CHASE ST         OSAGE   

    Zip Code                                     Store Location  \
914    52002  4400 ASBURY RD\nDUBUQUE 52002\n(42.515282, -90...   
915    51004  116 E MAIN ST\nANTHON 51004\n(42.388268, -95.8...   
916    52402  2605 BLAIRS FERRY RD NE\nCEDAR RAPIDS 52402\n(...   
917    52205  402 EAST MAIN\nANAMOSA 52205\n(42.108289, -91....   
918    50461  633, CHASE ST\nOSAGE 50461\n(43.285134, -92.81...   

     County Number    County  Category          Category Name  Vendor Number  \
914             31   Dubuque   1031200         VODKA FLAVORED            380   
915             97  Woodbury   1042100      IMPORTED DRY GINS            260   
916             57      Linn   1032200  IMPORTED VODKA - MISC            370   
917             53     Jones   1012100      CANADIAN WHISKIES            115   
918             66  Mitchell   1031080         VODKA 80 PROOF            297   

                          Vendor Name  Item Number  \
914         Phillips Beverage Company        41705   
915                   Diageo Americas        28890   
916  Pernod Ricard USA/Austin Nichols        34029   
917  Constellation Wine Company, Inc.        11774   
918                 Laird And Company        35926   

                 Item Description  Pack  Bottle Volume (ml)  \
914         Uv Red (cherry) Vodka    12                1000   
915         Tanqueray Rangpur Gin    12                 750   
916  Absolut Citron (lemon Vodka)    12                1000   
917                  Black Velvet    24                 375   
918        Five O'clock PET Vodka    12                 750   

     State Bottle Cost  State Bottle Retail  Bottles Sold  Sale (Dollars)  \
914               7.50                11.25            12          135.00   
915              12.50                18.74             2           37.48   
916              15.00                22.49            60         1349.40   
917               3.07                 4.60            48          220.80   
918               3.37                 5.06            12           60.72   

     Volume Sold (Liters)  Volume Sold (Gallons)  
914                  12.0                   3.17  
915                   1.5                   0.40  
916                  60.0                  15.85  
917                  18.0                   4.76  
918                   9.0                   2.38  
"""