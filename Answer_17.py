# Display the last 25 liquor data of the dataset.

import pandas as pd

df = pd.read_csv('sample_iowa_liquor_sales.csv')
pd.set_option('display.max_columns', None)
print(df.tail(25))


"""Output:
    Invoice/Item Number        Date  Store Number  \
894        S25976200016  06-02-2015          4326   
895        S12095200005  05-08-2013          3013   
896        S24129700005  02/19/2015          3712   
897        S12946600041  06/24/2013          2835   
898        S26299700151  06/18/2015          2515   
899        S04680100053  03/21/2012          3825   
900        S15444500015  10/30/2013          4251   
901        S15833500007  11/20/2013          3986   
902        S22927800089  12/15/2014          3562   
903        S21552900002  10-02-2014          4647   
904        S16534000021  12/27/2013          4148   
905        S04572600041  03/15/2012          4280   
906        S11456900038  04-04-2013          2190   
907        S04354200031  03-01-2012          3719   
908        S19584700001  06/17/2014          4266   
909        S16906900003  01/20/2014          3612   
910        S18142000006  03/31/2014          3868   
911        S19772000013  06/26/2014          4948   
912        S22284900002  11-10-2014          3830   
913        S17966000051  03/19/2014          3495   
914        S26164400020  06/16/2015          3944   
915        S19675100022  06/25/2014          4008   
916        S12278000057  05/22/2013          3385   
917        S05694100030  05/23/2012          2487   
918        S23309100006  01-06-2015          4559   

                             Store Name                    Address  \
894               Stratford Food Center        829 SHAKESPEARE AVE   
895                       Keith's Foods            207 E LOCUST ST   
896                       Monte Spirits               109 N 4TH ST   
897    CVS Pharmacy #8538 / Cedar Falls         2302 WEST FIRST ST   
898   Hy-Vee Food Store #1 / Mason City             2400 4TH ST SW   
899             Shop N Save #2 / E 14th             1372 E 14TH ST   
900                  Aj's Liquor / Ames  4518 MORTENSON RD STE 109   
901                  Siouxland Beverage                  1203 5 ST   
902        Wal-Mart 0797 / W Burlington         324 WEST AGENCY RD   
903             B and B EAST / Waterloo            1615 BISHOP AVE   
904  Fareway Stores #479 / Independence            1400 3RD AVE SE   
905        Slagle's Grocery / Le Claire        1301 EAGLE RIDGE RD   
906           Central City Liquor, Inc.               1460 2ND AVE   
907        Wal-Mart 0581 / Marshalltown           2802 S CENTER ST   
908          Wal-Mart 1683 / Shenandoah              705 S FREMONT   
909          B and C Liquor / Maquoketa                509 E PLATT   
910              Wal-Mart 3630 / Marion      5491 BUSINESS HWY 151   
911                 Wheatland Day Break               102 W HWY 30   
912             Wal-Mart 1435 / Creston              806 LAUREL ST   
913                      Great Pastimes              228 N MAIN ST   
914           Sam's Club 4973 / Dubuque             4400 ASBURY RD   
915                Sioux Valley Spirits              116 E MAIN ST   
916      Sam's Club 8162 / Cedar Rapids    2605 BLAIRS FERRY RD NE   
917                Anamosa Family Foods              402 EAST MAIN   
918                 Osage Payless Foods              633, CHASE ST   

                City Zip Code  \
894        STRATFORD    50249   
895       BLOOMFIELD    52537   
896        MONTEZUMA    50171   
897      CEDAR FALLS    50613   
898       MASON CITY    50401   
899       DES MOINES    50316   
900             AMES    50014   
901       SIOUX CITY    51101   
902  WEST BURLINGTON    52655   
903         WATERLOO    50707   
904     INDEPENDENCE    50644   
905        LE CLAIRE    52753   
906       DES MOINES    50314   
907     MARSHALLTOWN    50158   
908       SHENANDOAH    51601   
909        MAQUOKETA    52060   
910           MARION    52302   
911        WHEATLAND    52777   
912          CRESTON    50801   
913       MONTICELLO    52310   
914          DUBUQUE    52002   
915           ANTHON    51004   
916     CEDAR RAPIDS    52402   
917          ANAMOSA    52205   
918            OSAGE    50461   

                                        Store Location  County Number  \
894  829 SHAKESPEARE AVE\nSTRATFORD 50249\n(42.2713...             40   
895  207 E LOCUST ST\nBLOOMFIELD 52537\n(40.752691,...             26   
896  109 N 4TH ST\nMONTEZUMA 50171\n(41.585429, -92...             79   
897  2302 WEST FIRST ST\nCEDAR FALLS 50613\n(42.539...              7   
898  2400 4TH ST SW\nMASON CITY 50401\n(43.148446, ...             17   
899  1372 E 14TH ST\nDES MOINES 50316\n(41.604893, ...             77   
900            4518 MORTENSON RD STE 109\nAMES 50014\n             85   
901  1203 5 ST\nSIOUX CITY 51101\n(42.495322, -96.3...             97   
902  324 WEST AGENCY RD\nWEST BURLINGTON 52655\n(40...             29   
903  1615 BISHOP AVE\nWATERLOO 50707\n(42.49807, -9...              7   
904  1400 3RD AVE SE\nINDEPENDENCE 50644\n(42.45563...             10   
905  1301 EAGLE RIDGE RD\nLE CLAIRE 52753\n(41.5873...             82   
906  1460 2ND AVE\nDES MOINES 50314\n(41.60566, -93...             77   
907  2802 S CENTER ST\nMARSHALLTOWN 50158\n(42.0129...             64   
908  705 S FREMONT\nSHENANDOAH 51601\n(40.760655, -...             73   
909  509 E PLATT\nMAQUOKETA 52060\n(42.069219, -90....             49   
910              5491 BUSINESS HWY 151\nMARION 52302\n             57   
911                    102 W HWY 30\nWHEATLAND 52777\n             23   
912  806 LAUREL ST\nCRESTON 50801\n(41.047716, -94....             88   
913  228 N MAIN ST\nMONTICELLO 52310\n(42.240132, -...             53   
914  4400 ASBURY RD\nDUBUQUE 52002\n(42.515282, -90...             31   
915  116 E MAIN ST\nANTHON 51004\n(42.388268, -95.8...             97   
916  2605 BLAIRS FERRY RD NE\nCEDAR RAPIDS 52402\n(...             57   
917  402 EAST MAIN\nANAMOSA 52205\n(42.108289, -91....             53   
918  633, CHASE ST\nOSAGE 50461\n(43.285134, -92.81...             66   

          County  Category              Category Name  Vendor Number  \
894     Hamilton   1011200  STRAIGHT BOURBON WHISKIES            461   
895        Davis   1031100            100 PROOF VODKA            300   
896    Poweshiek   1012100          CANADIAN WHISKIES            115   
897   Black Hawk   1032200      IMPORTED VODKA - MISC            370   
898  Cerro Gordo   1081335         RASPBERRY SCHNAPPS             65   
899         Polk   1081600            WHISKEY LIQUEUR            260   
900        Story   1011200  STRAIGHT BOURBON WHISKIES             65   
901     Woodbury   1012100          CANADIAN WHISKIES             55   
902   Des Moines   1041150              FLAVORED GINS            370   
903   Black Hawk   1031080             VODKA 80 PROOF            297   
904     Buchanan   1022100                    TEQUILA            421   
905        Scott   1022100                    TEQUILA            395   
906         Polk   1012200            SCOTCH WHISKIES            260   
907     Marshall   1031080             VODKA 80 PROOF            380   
908         Page   1012100          CANADIAN WHISKIES            115   
909      Jackson   1011200  STRAIGHT BOURBON WHISKIES            421   
910         Linn   1081200             CREAM LIQUEURS            260   
911      Clinton   1062310                 SPICED RUM            260   
912        Union   1062300               FLAVORED RUM            370   
913        Jones   1062300               FLAVORED RUM             35   
914      Dubuque   1031200             VODKA FLAVORED            380   
915     Woodbury   1042100          IMPORTED DRY GINS            260   
916         Linn   1032200      IMPORTED VODKA - MISC            370   
917        Jones   1012100          CANADIAN WHISKIES            115   
918     Mitchell   1031080             VODKA 80 PROOF            297   

                          Vendor Name  Item Number  \
894                     Campari(skyy)        22157   
895      Mccormick Distilling Company        36908   
896  Constellation Wine Company, Inc.        11788   
897  Pernod Ricard USA/Austin Nichols        34116   
898                   Jim Beam Brands        82836   
899                   Diageo Americas        67266   
900                   Jim Beam Brands        19068   
901             Sazerac North America        11936   
902  Pernod Ricard USA/Austin Nichols        33256   
903                 Laird And Company        35926   
904                 Sazerac Co., Inc.        89916   
905                           Proximo        87510   
906                   Diageo Americas         5350   
907         Phillips Beverage Company        37348   
908  Constellation Wine Company, Inc.        11788   
909                 Sazerac Co., Inc.        16518   
910                   Diageo Americas        68049   
911                   Diageo Americas        43336   
912  Pernod Ricard USA/Austin Nichols        42718   
913              Bacardi U.S.A., Inc.        43137   
914         Phillips Beverage Company        41705   
915                   Diageo Americas        28890   
916  Pernod Ricard USA/Austin Nichols        34029   
917  Constellation Wine Company, Inc.        11774   
918                 Laird And Company        35926   

                         Item Description  Pack  Bottle Volume (ml)  \
894                       Wild Turkey 101    12                1000   
895                   Mccormick Vodka Pet     6                1750   
896                          Black Velvet     6                1750   
897                       Absolut Mandrin    12                 750   
898             Dekuyper Raspberry Pucker    12                 750   
899           Yukon Jack Canadian Liqueur    12                 750   
900                              Jim Beam     6                1750   
901  Canadian Ltd Whisky Convenience Pack    12                 750   
902             Seagrams Lime Twisted Gin    12                 750   
903                Five O'clock PET Vodka    12                 750   
904                 Tortilla Gold Tequila    12                 750   
905                   1800 Silver Tequila    12                 750   
906                  Johnnie Walker Green     6                 750   
907                        Phillips Vodka     6                1750   
908                          Black Velvet     6                1750   
909                   Ancient Age Bourbon     6                1750   
910             Bailey's Vanilla Cinnamon    12                 750   
911        Captain Morgan Original Spiced    12                 750   
912                    Malibu Coconut Rum     6                1750   
913                         Bacardi Limon    12                1000   
914                 Uv Red (cherry) Vodka    12                1000   
915                 Tanqueray Rangpur Gin    12                 750   
916          Absolut Citron (lemon Vodka)    12                1000   
917                          Black Velvet    24                 375   
918                Five O'clock PET Vodka    12                 750   

     State Bottle Cost  State Bottle Retail  Bottles Sold  Sale (Dollars)  \
894              16.16                24.24             2           48.48   
895               7.46                11.19             6           67.14   
896               9.70                14.93             6           89.58   
897              11.00                16.49             3           49.47   
898               6.30                 9.45             2           18.90   
899               8.54                12.81             4           51.24   
900              18.42                28.14             2           56.28   
901               3.84                 6.01            12           72.12   
902               6.49                 9.74            12          116.88   
903               3.37                 5.06            12           60.72   
904               6.27                 9.40             2           18.80   
905              14.50                21.74             1           21.74   
906              36.75                55.12             2          110.24   
907               7.31                10.97             6           65.82   
908              10.45                15.67            12          188.04   
909              11.80                17.70             3           53.10   
910              13.00                19.50            12          234.00   
911               8.75                13.12             6           78.72   
912              16.49                24.74             6          148.44   
913              10.24                15.35             5           76.75   
914               7.50                11.25            12          135.00   
915              12.50                18.74             2           37.48   
916              15.00                22.49            60         1349.40   
917               3.07                 4.60            48          220.80   
918               3.37                 5.06            12           60.72   

     Volume Sold (Liters)  Volume Sold (Gallons)  
894                  2.00                   0.53  
895                 10.50                   2.77  
896                 10.50                   2.77  
897                  2.25                   0.59  
898                  1.50                   0.40  
899                  3.00                   0.79  
900                  3.50                   0.92  
901                  9.00                   2.38  
902                  9.00                   2.38  
903                  9.00                   2.38  
904                  1.50                   0.40  
905                  0.75                   0.20  
906                  1.50                   0.40  
907                 10.50                   2.77  
908                 21.00                   5.55  
909                  5.25                   1.39  
910                  9.00                   2.38  
911                  4.50                   1.19  
912                 10.50                   2.77  
913                  5.00                   1.32  
914                 12.00                   3.17  
915                  1.50                   0.40  
916                 60.00                  15.85  
917                 18.00                   4.76  
918                  9.00                   2.38
"""