import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from my_lambdata.my_mod import ten_x, check_null
# from my_lambdata.my_mod import check_null
df = pd.DataFrame({'State': ['AZ', 'CT', 'CO', 'CA', 'TX', 'KY', 'NY', 'AL']})
print('\n', ten_x(15), '\n')
print('Null count:', check_null(df), '\n')
print(df.describe, '\n')
