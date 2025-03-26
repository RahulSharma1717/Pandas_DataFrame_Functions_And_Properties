# Create a sample dataset of 10 rows from the existing dataset.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.sample(10))


"""Output:
        Transaction_ID  Customer_ID                Name                Email  \
192955         9361161        73632      Richard Jordan  Brianna15@gmail.com   
180598         9020837        34072      Carl Hernandez   Andrew43@gmail.com   
155353         8450347        48219        Charles King   Robert99@gmail.com   
196310         7073474        33315  Christopher Benton  Michael72@gmail.com   
11087          2666014        72082      Laura Anderson  Michael49@gmail.com   
158551         8068169        46483        Sheila Garza    Jacob23@gmail.com   
55852          5987798        83167       Stephen Gomez   Joseph29@gmail.com   
101477         5434604        12981    Christine Fowler   Cheryl36@gmail.com   
19124          8898067        52955       Julie Mcclain  Desiree65@gmail.com   
103767         2305318        84151        Melvin Brown   Charles9@gmail.com   

             Phone                           Address        City  \
192955  4590704162                669 Mcdonald Walks    Hamilton   
180598  8497349050             0515 Courtney Valleys      Austin   
155353  7105881397                  98090 Scott Fall      Boston   
196310  8949535405       70450 Vicki Lodge Suite 736    New York   
11087   4807523831      182 Justin Prairie Suite 464  Portsmouth   
158551  6067123194        017 Parker Forge Suite 451    New York   
55852   5748663726     41880 Smith Gateway Suite 965     Geelong   
101477  3094935076      66018 Cross Course Suite 517      Hobart   
19124   8667069861  93884 Kimberly Centers Suite 143  Fort Worth   
103767  2341937931                   2100 Young Wall     Belfast   

                  State  Zipcode    Country  Age  Gender  Income  \
192955          Ontario    87334     Canada   28    Male     Low   
180598           Alaska    99601        USA   19    Male     Low   
155353          Georgia    72130        USA   23    Male    High   
196310             Utah    84691        USA   32    Male  Medium   
11087           England    34174         UK   19  Female  Medium   
158551           Kansas    24948        USA   23  Female    High   
55852   New South Wales    60236  Australia   20    Male  Medium   
101477  New South Wales    68173  Australia   46    Male     Low   
19124        New Mexico    35195        USA   19    Male  Medium   
103767          England    32501         UK   46  Female  Medium   

       Customer_Segment        Date  Year      Month      Time  \
192955              New  03-11-2023  2023      March  16:55:28   
180598          Regular  09-11-2023  2023  September  09:02:38   
155353          Regular  07-02-2023  2023       July  00:51:15   
196310          Premium  11/22/2023  2023   November  23:11:18   
11087           Regular   3/30/2023  2023      March  22:11:31   
158551          Regular  07-03-2023  2023       July  01:42:37   
55852               New  11/23/2023  2023   November  15:21:55   
101477              New   7/30/2023  2023       July  04:53:00   
19124               New  12-01-2023  2023   December  05:55:55   
103767          Premium  02-07-2024  2024   February  22:39:07   

        Total_Purchases      Amount  Total_Amount Product_Category  \
192955                8  485.761484   3886.091872      Electronics   
180598                5   41.429704    207.148520            Books   
155353                7  458.617772   3210.324404      Electronics   
196310                4  326.764066   1307.056265      Electronics   
11087                 8  386.312224   3090.497788            Books   
158551                5  201.445804   1007.229020      Electronics   
55852                 1  328.243360    328.243360            Books   
101477                5  483.885817   2419.429087       Home Decor   
19124                 3  123.556919    370.670757          Grocery   
103767                2  459.937973    919.875947      Electronics   

            Product_Brand Product_Type   Feedback Shipping_Method  \
192955            Samsung       Tablet       Good        Standard   
180598      Penguin Books   Children's  Excellent        Standard   
155353            Samsung       Tablet    Average        Same-Day   
196310              Apple       Laptop        Bad        Same-Day   
11087        Random House      Fiction       Good         Express   
158551              Apple   Smartphone       Good        Standard   
55852       Penguin Books  Non-Fiction    Average         Express   
101477  Bed Bath & Beyond      Bedding  Excellent        Standard   
19124               Pepsi   Soft Drink        Bad        Same-Day   
103767               Sony   Smartphone  Excellent         Express   

       Payment_Method Order_Status  Ratings         products  
192955         PayPal   Processing        4       Lenovo Tab  
180598    Credit Card    Delivered        4          Puzzles  
155353    Credit Card    Delivered        2  Huawei MediaPad  
196310           Cash      Shipped        1     Asus ZenBook  
11087            Cash    Delivered        3  Science fiction  
158551    Credit Card      Shipped        4    Motorola Moto  
55852     Credit Card   Processing        2          Science  
101477    Credit Card      Shipped        4        Bed skirt  
19124      Debit Card    Delivered        1     Energy drink  
103767         PayPal      Shipped        5    Motorola Moto
"""