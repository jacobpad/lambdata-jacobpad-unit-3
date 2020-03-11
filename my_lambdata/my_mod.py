# my_lambdata/my_mod.py

import sklearn
from sklearn.model_selection import train_test_split

    # '''
    # PARAM: 
    # PURPOSE: 
    # RETURNS: 
    # '''


def ten_x(num):
    '''
    PARAM: 'num' is a number (int or float)
    PURPOSE: Takes 'num' and multiplies it by 10
    RETURNS: Another number (int or float)
    '''
    return num * 10

def check_null(df):
    '''
    Checks for null's
    '''
    return df.isnull().sum()

def split_data(df):
    '''
    PARAM: is a data frame
    PURPOSE: preforms train/test/val/split
    RETURNS: sections of data frame
    Split data frame into 70% train, 15% val, 15% test
    '''
    train, test = train_test_split(df, test_size=0.15, train_size=0.85)
    train, val = train_test_split(train, test_size=0.15, train_size=0.85)

    return train, test, val

# def target_features(target):
#     '''
#     Target = target from the dataframe
#     '''
#     target = target
#     features = train.columns.drop(target)

#     X_train = train[features]
#     y_train = train[target]
#     X_val = val[features]
#     y_val = val[target]
#     X_test = test[features]
#     y_test = test[target]

#     return X_train, y_train, X_val, y_val, X_test, y_test

def wrangle(x):
    '''
    PARAM: x = dataframe 
    PURPOSE: Wrangles a function
    RETURNS: A more whole function
    '''
    x = x.copy()
    x.columns = [col.lower() # make col names lower case
                .strip('_')
                .replace('_', ' ')
                .replace('-', ' ')
                .replace('/', ' ')
                for col in x.columns]
    x = x.fillna(value=0)
    return x