# Generate a sample dataset containing 30 rows based on the current dataset.

import pandas as pd

df = pd.read_csv('sample_iowa_liquor_sales.csv')
pd.set_option('display.max_columns', None)
print(df.sample(30))


"""Output:
    Invoice/Item Number        Date  Store Number  \
697        S11187900040  03/21/2013          3829   
143        S25028600099  04/13/2015          2591   
129        S22743400064  12-04-2014          2959   
350        S21049400056  09-04-2014          4969   
299        S23569700019  01/20/2015          4891   
523        S13056200014  06/27/2013          2620   
144        S07729600031  09/13/2012          2545   
251        S26919400055  07/22/2015          3417   
508        S07309000002  08/27/2012          2190   
824        S03979500031  02-08-2012          3614   
360        S09922700017  01-08-2013          4156   
120        S19128800024  05/22/2014          4165   
569        S22528700015  11/21/2014          3696   
403        S19609100072  06/18/2014          3723   
262        S20763800029  08/20/2014          5010   
630        S27230800061  08-10-2015          2535   
885        S05005500068  04-11-2012          2536   
87         S19553400063  06/16/2014          4829   
496        S16455500107  12/21/2013          2619   
156        S11435500030  04-03-2013          3735   
765        S21574800010  10-08-2014          3354   
477        S29053900020  11/18/2015          5181   
111        S09979300008  01-10-2013          2529   
497        S18878400073  05-12-2014          4152   
145        S19385800095  06-05-2014          4829   
557        S13480400070  07/22/2013          2591   
660        S11360200006  04-01-2013          4430   
757        S27081200011  08-04-2015          4358   
128        S12219300026  05/14/2013          3774   
774        S06497200010  07-10-2012          3717   

                               Store Name                      Address  \
697              Gary's Foods / Mt Vernon               715  1ST AVE S   
143    Hy-Vee Wine and Spirits / Atlantic              1602 E. 7TH ST.   
129                    Dahl's / Merle Hay          4343 MERLE HAY ROAD   
350         Lake Liquors Wine and Spirits               910 N 8TH ST W   
299                     Schottsy's Liquor                   109 5th ST   
523              Hy-Vee / Windsor Heights          7101 UNIVERSITY AVE   
144          Hy-Vee Drugstore / Iowa City                 310 N 1ST ST   
251                      Big G Food Store     PO BOX 261  310 W DILLON   
508             Central City Liquor, Inc.                 1460 2ND AVE   
824                  Ida Grove Food Pride             200 OAK GROVE DR   
360         Fareway Stores #412 / Oelwein              102  2ND AVE SE   
120                 I-35 Spirits / Ankeny  113 SE DELAWARE AVE STE 101   
569            Wal-Mart 1723 / Des Moines              5101 SE 14TH ST   
403                    J D Spirits Liquor                 1023  9TH ST   
262                   Sac City Food Pride                106 S 16TH ST   
630            Hy-Vee Food Store #1 / WDM          1700 VALLEY WEST DR   
885                HY-VEE / PLEASANT HILL             4815 MAPLE DRIVE   
87                         Central City 2            1501 MICHIGAN AVE   
496         Hy-Vee Wine and Spirits / WDM                1725  74TH ST   
156                            C B Liquor              1202 A AVE EAST   
765           Sam's Club 8238 / Davenport             3845 ELMORE AVE.   
477  Casey's General Store #3434  /  Denv           1101, JEFFERSON ST   
111    Hy-Vee Drugstore #4 / Cedar Rapids          4825 JOHNSON AVE NW   
497  Food Land Super Markets / Missouri V                  407 W HURON   
145                        Central City 2            1501 MICHIGAN AVE   
557    Hy-Vee Wine and Spirits / Atlantic              1602 E. 7TH ST.   
660             Kum & Go #87 / Fort Dodge          1601 FIFTH AVENUE S   
757               Kum & Go #553 / Clarion            300 CENTRAL AVE W   
128        Eagle Country Market / Dubuque                  1800 ELM ST   
774              The Liquor Stop / Sumner                 201 W 1st ST   

                City Zip Code  \
697     MOUNT VERNON    52314   
143         ATLANTIC    50022   
129       DES MOINES    50310   
350       CLEAR LAKE    50428   
299           SIBLEY    51249   
523  WINDSOR HEIGHTS    50311   
144        IOWA CITY    52245   
251          MARENGO    52301   
508       DES MOINES    50314   
824        IDA GROVE    51445   
360          OELWEIN    50662   
120           ANKENY    50023   
569       DES MOINES    50315   
403            ONAWA    51040   
262         SAC CITY    50583   
630  WEST DES MOINES    50265   
885    PLEASANT HILL    50317   
87        DES MOINES    50314   
496  WEST DES MOINES    50266   
156        OSKALOOSA    52577   
765        DAVENPORT    52807   
477           DENVER    50622   
111     CEDAR RAPIDS    52405   
497  MISSOURI VALLEY    51555   
145       DES MOINES    50314   
557         ATLANTIC    50022   
660       FORT DODGE    50501   
757          CLARION    50525   
128          DUBUQUE    52001   
774           SUMNER    50674   

                                        Store Location  County Number  \
697  715 1ST AVE S\nMOUNT VERNON 52314\n(41.91673, ...             57   
143  1602 E. 7TH ST.\nATLANTIC 50022\n(41.403856, -...             15   
129  4343 MERLE HAY ROAD\nDES MOINES 50310\n(41.637...             77   
350  910 N 8TH ST W\nCLEAR LAKE 50428\n(43.142775, ...             17   
299  109 5th ST\nSIBLEY 51249\n(43.403935, -95.759951)             72   
523  7101 UNIVERSITY AVE\nWINDSOR HEIGHTS 50311\n(4...             77   
144  310 N 1ST ST\nIOWA CITY 52245\n(41.665693, -91...             52   
251           PO BOX 261 310 W DILLON\nMARENGO 52301\n             48   
508  1460 2ND AVE\nDES MOINES 50314\n(41.60566, -93...             77   
824  200 OAK GROVE DR\nIDA GROVE 51445\n(42.349486,...             47   
360  102 2ND AVE SE\nOELWEIN 50662\n(42.677024, -91...             33   
120  113 SE DELAWARE AVE STE 101\nANKENY 50023\n(41...             77   
569  5101 SE 14TH ST\nDES MOINES 50315\n(41.537606,...             77   
403  1023 9TH ST\nONAWA 51040\n(42.025841, -96.095845)             67   
262  106 S 16TH ST\nSAC CITY 50583\n(42.422404, -95...             81   
630       1700 VALLEY WEST DR\nWEST DES MOINES 50265\n             77   
885            4815 MAPLE DRIVE\nPLEASANT HILL 50317\n             77   
87   1501 MICHIGAN AVE\nDES MOINES 50314\n(41.60556...             77   
496  1725 74TH ST\nWEST DES MOINES 50266\n(41.59851...             77   
156  1202 A AVE EAST\nOSKALOOSA 52577\n(41.296286, ...             10   
765  3845 ELMORE AVE.\nDAVENPORT 52807\n(41.559724,...             82   
477                 1101, JEFFERSON ST\nDENVER 50622\n              9   
111  4825 JOHNSON AVE NW\nCEDAR RAPIDS 52405\n(41.9...             57   
497  407 W HURON\nMISSOURI VALLEY 51555\n(41.557404...             43   
145  1501 MICHIGAN AVE\nDES MOINES 50314\n(41.60556...             77   
557  1602 E. 7TH ST.\nATLANTIC 50022\n(41.403856, -...             15   
660  1601 FIFTH AVENUE S\nFORT DODGE 50501\n(42.501...             94   
757  300 CENTRAL AVE W\nCLARION 50525\n(42.731643, ...             99   
128  1800 ELM ST\nDUBUQUE 52001\n(42.511105, -90.66...             31   
774  201 W 1st ST\nSUMNER 50674\n(42.847479, -92.09...              9   

          County  Category                     Category Name  Vendor Number  \
697         Linn   1011200         STRAIGHT BOURBON WHISKIES             65   
143         Cass   1081390                 IMPORTED SCHNAPPS            421   
129         Polk   1062310                        SPICED RUM            259   
350  Cerro Gordo   1011300                TENNESSEE WHISKIES             85   
299      Osceola   1011500             STRAIGHT RYE WHISKIES            255   
523         Polk   1031080                    VODKA 80 PROOF            380   
144      Johnson   1031080                    VODKA 80 PROOF            260   
251         Iowa   1032080                    IMPORTED VODKA            115   
508         Polk   1081330                    PEACH SCHNAPPS             65   
824          Ida   1062300                      FLAVORED RUM            370   
360      Fayette   1031200                    VODKA FLAVORED            380   
120         Polk   1031080                    VODKA 80 PROOF            260   
569         Polk   1031100                   100 PROOF VODKA            260   
403       Monona   1081365           TROPICAL FRUIT SCHNAPPS             65   
262          Sac   1042100                 IMPORTED DRY GINS            260   
630         Polk   1031080                    VODKA 80 PROOF            260   
885         Polk   1012100                 CANADIAN WHISKIES            971   
87          Polk   1081300               PEPPERMINT SCHNAPPS             65   
496         Polk   1012100                 CANADIAN WHISKIES            260   
156     Buchanan   1031080                    VODKA 80 PROOF            297   
765        Scott   1011100                  BLENDED WHISKIES             65   
477       Bremer   1062310                        SPICED RUM            260   
111         Linn   1011100                  BLENDED WHISKIES            297   
497     Harrison   1022100                           TEQUILA            434   
145         Polk   1081305                    APPLE SCHNAPPS             65   
557         Cass   1051010           AMERICAN GRAPE BRANDIES             85   
660      Webster   1011500             STRAIGHT RYE WHISKIES            255   
757       Wright   1081600                   WHISKEY LIQUEUR             85   
128      Dubuque   1012200                   SCOTCH WHISKIES             35   
774       Bremer   1062200  PUERTO RICO & VIRGIN ISLANDS RUM             35   

                          Vendor Name  Item Number  \
697                   Jim Beam Brands        19112   
143                 Sazerac Co., Inc.        69636   
129                Heaven Hill Brands        43028   
350          Brown-Forman Corporation        26828   
299               Wilson Daniels Ltd.        27102   
523         Phillips Beverage Company        37347   
144                   Diageo Americas        37991   
251  Constellation Wine Company, Inc.        35435   
508                   Jim Beam Brands        82847   
824  Pernod Ricard USA/Austin Nichols        42703   
360         Phillips Beverage Company        41693   
120                   Diageo Americas        38008   
569                   Diageo Americas        39866   
403                   Jim Beam Brands        82857   
262                   Diageo Americas        28866   
630                   Diageo Americas        37994   
885       Hood River Distillers, Inc.        14192   
87                    Jim Beam Brands        80687   
496                   Diageo Americas        11294   
156                 Laird And Company        35918   
765                   Jim Beam Brands        24457   
477                   Diageo Americas        43334   
111                 Laird And Company        23827   
497                    Luxco-St Louis        87938   
145                   Jim Beam Brands        82607   
557          Brown-Forman Corporation        52806   
660               Wilson Daniels Ltd.        27102   
757          Brown-Forman Corporation        86884   
128              Bacardi U.S.A., Inc.         4866   
774              Bacardi U.S.A., Inc.        43127   

                                Item Description  Pack  Bottle Volume (ml)  \
697                         Jim Beam Devil's Cut    12                 750   
143           Dr. Mcgillicuddy's Cherry Schnapps    12                 750   
129                    Admiral Nelson Spiced Rum     6                1750   
350                Jack Daniels Old #7 Black Lbl     6                1750   
299                                Templeton Rye     6                 750   
523                               Phillips Vodka    12                1000   
144                   Smirnoff Vodka 80 Prf Mini    12                 500   
251                              Svedka Traveler    12                 750   
508                           Dekuyper Peachtree    12                1000   
824                         Malibu Pineapple Rum    12                 750   
360                    Uv Blue (raspberry) Vodka    12                 750   
120                    Smirnoff Vodka 80 Prf Pet     6                1750   
569                       Smirnoff Vodka 100 Prf    12                 750   
403                 Dekuyper Island Punch Pucker    12                1000   
262                                Tanqueray Gin    12                 750   
630                        Smirnoff Vodka 80 Prf    24                 375   
885                    Pendleton Canadian Whisky    12                 750   
87   Dekuyper Blustery Peppermint Burst Schnapps    12                1000   
496                  Crown Royal Canadian Whisky    24                 375   
156                           Five O'clock Vodka     6                1750   
765                        Kessler Blend Whiskey    12                1000   
477                    Captain Morgan Spiced Rum    24                 375   
111                                    Five Star    12                1000   
497                        Juarez Tequila Silver     6                1750   
145                          Dekuyper Sour Apple    12                1000   
557                                Korbel Brandy    12                 750   
660                                Templeton Rye     6                 750   
757                             Southern Comfort    24                 375   
128                    Dewars White Label Scotch    12                 750   
774                         Bacardi Superior Rum    12                1000   

     State Bottle Cost  State Bottle Retail  Bottles Sold  Sale (Dollars)  \
697              15.22                22.84             1           22.84   
143               8.67                13.01            12          156.12   
129              11.55                17.33             6          103.98   
350              28.69                43.04             6          258.24   
299              18.09                27.14             6          162.84   
523               4.28                 6.42            12           77.04   
144               7.47                11.20             1           11.20   
251               8.25                12.38             4           49.52   
508               7.35                11.02            12          132.24   
824               6.90                10.35             3           31.05   
360               6.50                 9.74            12          116.88   
120              14.75                22.12             2           44.24   
569               8.75                13.13            12          157.56   
403               7.62                11.43             2           22.86   
262              12.25                18.38             3           55.14   
630               4.75                 7.13            24          171.12   
885              13.10                19.65             1           19.65   
87                3.86                 5.78            12           69.36   
496               7.65                11.48             6           68.88   
156               7.20                10.79             6           64.74   
765               7.08                10.62            24          254.88   
477               5.00                 7.50            24          180.00   
111               4.40                 6.59            12           79.08   
497              13.00                19.50             1           19.50   
145               7.62                11.43            48          548.64   
557               5.69                 8.54             2           17.08   
660              18.08                27.13            12          325.56   
757               4.78                 7.17            24          172.08   
128              13.73                20.59             3           61.77   
774               9.43                14.14             1           14.14   

     Volume Sold (Liters)  Volume Sold (Gallons)  
697                  0.75                   0.20  
143                  9.00                   2.38  
129                 10.50                   2.77  
350                 10.50                   2.77  
299                  4.50                   1.19  
523                 12.00                   3.17  
144                  0.50                   0.13  
251                  3.00                   0.79  
508                 12.00                   3.17  
824                  2.25                   0.59  
360                  9.00                   2.38  
120                  3.50                   0.92  
569                  9.00                   2.38  
403                  2.00                   0.53  
262                  2.25                   0.59  
630                  9.00                   2.38  
885                  0.75                   0.20  
87                  12.00                   3.17  
496                  2.25                   0.59  
156                 10.50                   2.77  
765                 24.00                   6.34  
477                  9.00                   2.38  
111                 12.00                   3.17  
497                  1.75                   0.46  
145                 48.00                  12.68  
557                  1.50                   0.40  
660                  9.00                   2.38  
757                  9.00                   2.38  
128                  2.25                   0.59  
774                  1.00                   0.26
"""