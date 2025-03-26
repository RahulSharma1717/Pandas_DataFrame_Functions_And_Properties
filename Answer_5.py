# Check out the data type for each column.

import pandas as pd

df = pd.read_csv('retail_data.csv')
# pd.set_option('display.max_columns', None)
print(df.dtypes)


"""Output:
Transaction_ID        int64
Customer_ID           int64
Name                 object
Email                object
Phone                 int64
Address              object
City                 object
State                object
Zipcode               int64
Country              object
Age                   int64
Gender               object
Income               object
Customer_Segment     object
Date                 object
Year                  int64
Month                object
Time                 object
Total_Purchases       int64
Amount              float64
Total_Amount        float64
Product_Category     object
Product_Brand        object
Product_Type         object
Feedback             object
Shipping_Method      object
Payment_Method       object
Order_Status         object
Ratings               int64
products             object
dtype: object
"""