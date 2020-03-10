import pandas as pd
import numpy as np
from my_lambdata.my_mod import ten_x, check_null
# from my_lambdata.my_mod import check_null
df = pd.DataFrame({'State':['AZ', 'CT', 'CO', 'CA', 'TX', 'KY', 'NY', 'AL']})
print('\n',ten_x(15),'\n')
print('Null count:',check_null(df),'\n')
print(df.describe,'\n')

# import pandas

# from my_lambdata.my_mod import enlarge


# print("HELLO WORLD")

# df = pandas.DataFrame({"state": ["CT", "CO", "CA", "TX"]})
# print(df.head())

# print("-----------------")


# x = 5
# print("NUMBER", x)
# print("ENLARGED NUMBER", enlarge(x)) # invoking our function!!